from Crypto.Cipher import ARC4
from encprovider import EncProvider


class ClientToRosEncProvider(EncProvider):
    def __init__(self):
        super(ClientToRosEncProvider, self).__init__()

    def encrypt(self, data):
        pass

    def decrypt(self, data, session_key=''):
        pkg_rc4key = bytearray(b'')

        # It seems that the algorithm is: read the data from 16 first bytes, xor it with a key that we know.
        # This will be the actual key to decrypt the POST body
        for i in range(0, 16):
            pkg_rc4key.append(data[i] ^ self.decrypted_xorkey[i])

        encrypted_data = data[16:]
        data = ARC4.new(pkg_rc4key).decrypt(encrypted_data)

        return data
