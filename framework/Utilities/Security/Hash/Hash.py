import hashlib
import binascii
import random
import string

from framework.Utilities.Misc.Utils import path_join
from framework.Data.File.JSONFile import JSONFile


class Hash:
    @staticmethod
    def make(text, hash_name='sha256', iterations=500000):
        s_file_path = path_join('config', 'app.json')
        a_data = JSONFile(s_file_path, "r").read()
        app_key = a_data['APP_KEY']
        return binascii.hexlify(hashlib.pbkdf2_hmac(hash_name, str.encode(text), str.encode(app_key), iterations)).decode()
    
    @staticmethod
    def generate_key(size=48):
        return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits + '&^%$#@!') for _ in range(size))
    
    @staticmethod
    def verify(text, hashed):
        hashed_text = Hash.make(text)
        return hashed_text == hashed
