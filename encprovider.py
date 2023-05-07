import base64
from Crypto.Cipher import ARC4


class EncProvider():
    def __init__(self):
        self.PLATFORM_KEY = "C4AaRpadRR2hApFvyl6fJDHShJIa/K76qSPt+2wTcox6C4Yn2X82ubbT79Rg/Ci2bTedR/1PzOaYMWM0TLT82m0=" # PS3
        #self.PLATFORM_KEY = "C4pWJwWIKGUxcHd69eGl2AOwH2zrmzZAoQeHfQFcMelybd32QFw9s10px6k0o75XZeB5YsI9Q9TdeuRgdbvKsxc=" # PC

        self.platformStr = base64.b64decode(self.PLATFORM_KEY)
        self.rc4key = self.platformStr[1:33]
        self.xorkey = self.platformStr[33:49]
        self.hashkey = self.platformStr[49:]

        # At least xorkey is used upon the ticket request
        self.decrypted_xorkey = ARC4.new(self.rc4key).decrypt(self.xorkey)
        self.decrypted_hashkey = ARC4.new(self.rc4key).decrypt(self.hashkey)

    def encrypt(self, data):
        pass

    def decrypt(self, data, session_key=''):
        pass
