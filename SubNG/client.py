from telethon import TelegramClient
from telethon.sessions import StringSession
from InputData import (Channels)
from ConfigWorker import DetectConfig
from ConfigWorker import NameEditor

class CLIENT:
    def __init__(self, Data:dict) -> None:
        self.AccountData:dict = Data

        self.client = TelegramClient(StringSession(self.AccountData["Session"]),
            api_id = self.AccountData["Api-ID"],
            api_hash = self.AccountData["Api-HASH"]
        )

    async def GetConfigs(self, LimitMsg:int = 100):
        await self.client.disconnect()
        #-----------------------------------
        await self.client.start()
        DetectedConfigs = []
        for i in Channels.split("\n"):
            Messages = self.client.iter_messages(
                entity = i,
                limit = LimitMsg,
            )
            Messages = "\n".join(
                [i.text async for i in Messages if i.text != None]
            ) 
            for config in DetectConfig(Messages) : DetectedConfigs.append(config)
        await self.client.disconnect()
        DetectedConfigs = list( dict.fromkeys(DetectedConfigs) ) 
        DetectedConfigs.sort()
        return "\n\n".join(
            [NameEditor(Config = i, NewName = "SOHEIL 🐙") for i in DetectedConfigs]
        )
    