#(©)Codexbotz

import pyromod.listen
from pyrogram import Client
import sys

from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL2, CHANNEL_ID

class Bot(Client):
    def __init__(self):
        super().__init__(
            "Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()

        if FORCE_SUB_CHANNEL:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB_CHANNEL)
                self.invitelink = link
            except:
                self.LOGGER(__name__).warning("Error, pastikan kamu memberikan izin pada bot untuk membuat invite link pada forcesubs channel")
                self.LOGGER(__name__).warning("Mohon cek ID channel yang akan di subs, pastikan bot sudah jadi admin dengan izin undang pengguna via tautan!")
                self.LOGGER(__name__).info("\nBot berhenti bekerja silakan hibungi ryanx di telegram")
                sys.exit()


        if FORCE_SUB_CHANNEL2:
            try:
                links = await self.export_chat_invite_link(FORCE_SUB_CHANNEL2)
                self.invitelinks = links
            except:
                self.LOGGER(__name__).warning("Error, pastikan kamu memberikan izin pada bot untuk membuat invite link pada forcesubs channel kedua")
                self.LOGGER(__name__).warning("Mohon cek ID channel yang akan di subs, pastikan bot sudah jadi admin dengan izin undang pengguna via tautan pada kedua channel!!")
                self.LOGGER(__name__).info("\nBot berhenti bekerja silakan hibungi ryanx di telegram")
                sys.exit()



        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id = db_channel.id, text = "Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning("Bot wajib dijadikan sebagai admin pada db channel, silakan edit hak akses bot pada channel jadikan bot sebagai admin Channel.")
            self.LOGGER(__name__).info("\nBot berhenti bekerja silakan hibungi ryanx di telegram")
            sys.exit()







        self.set_parse_mode("html")
        self.LOGGER(__name__).info(f"Bot Running!\nSilakan cek bot anda, klik start.\n\nJika butuh bantuan hubuni ryanx di telegram")
        self.username = usr_bot_me.username

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot berhenti bekerja.")
