from telethon import TelegramClient
from telethon.sessions import StringSession
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import (pad, unpad)
from base64 import b64encode
from hashlib import sha256
from os import system

class Cipher:
    def __init__(self, Data:str, key:str) -> None:
        self.data = Data.encode('utf-8')
        self.key = sha256(key.encode('utf-8')).digest()

    def encrypt(self):
        IV = get_random_bytes(AES.block_size)
        cipher = AES.new(key = self.key, mode = AES.MODE_CBC, iv = IV)
        PaddedData = pad(self.data, AES.block_size)
        return b64encode(IV + cipher.encrypt(PaddedData)).decode()
    
api_id = input("Enter Your Api ID -> ")
api_hash = input("Enter Your Api HASH -> ")
phone_number = input("Enter Your Phone Number -> ")
SessionKey = input("Enter SessionKey -> ")

client = TelegramClient(StringSession(), api_id, api_hash)

async def main():
    await client.start(phone_number)
    session_string = client.session.save()
    return session_string


SessionStr = client.loop.run_until_complete(main())

ResultData = {
    "Api-ID" : api_id,
    "Api-HASH" : api_hash,
    "Session" : SessionStr
}
system("cls")

Result = Cipher(
    Data = str(ResultData),
    key = SessionKey
).encrypt()


system("cls")

print(Result)

input()
