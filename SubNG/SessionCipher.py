from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import (unpad)
from base64 import b64encode
from base64 import b64decode
from hashlib import sha256
class Cipher:
    def __init__(self, Data:str, key:str) -> None:
        self.data = Data.encode('utf-8')
        self.key = sha256(key.encode('utf-8')).digest()
    
    def decrypt(self):
        B64DecodedData = b64decode(self.data)
        cipher = AES.new(key = self.key, mode = AES.MODE_CBC, iv = B64DecodedData[:AES.block_size])
        PLainText = cipher.decrypt(B64DecodedData[AES.block_size:])
        return (unpad(PLainText, AES.block_size)).decode()
    