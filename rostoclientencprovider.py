import base64

from encprovider import EncProvider
from Crypto.Cipher import ARC4
from Crypto.Hash import SHA1


class RosToClientEncProvider(EncProvider):
    def __init__(self):
        super(RosToClientEncProvider, self).__init__()

    def encrypt(self, data):
        rc4_key = b'0101010101010101'
        xored_rc4_key = bytearray(b'')
        out_data = bytearray(b'')
        enc_data = bytearray(b'')
        blockSize = 2048

        for i in range(0, 16):
            xored_rc4_key.append(rc4_key[i] ^ self.decrypted_xorkey[i])

        # Add key
        out_data.extend(xored_rc4_key)

        # Add block size
        rc4 = ARC4.new(rc4_key)
        out_data.extend(rc4.encrypt(blockSize.to_bytes(4, byteorder='big')))

        # Add block
        enc_data.extend(rc4.encrypt(data))

        # Add block hash
        h = SHA1.new()
        h.update(enc_data)
        h.update(self.decrypted_hashkey)
        enc_data.extend(h.digest())

        out_data.extend(enc_data)

        return out_data

    def decrypt(self, data, session_key=''):
        pkg_rc4key = bytearray(b'')
        decoded_session_key = b''

        if session_key != '':
            decoded_session_key = base64.b64decode(session_key)

        for i in range(0, 16):
            char = data[i] ^ self.decrypted_xorkey[i]

            # If we have a session key and ros-SecurityFlags we xor it with it as well
            if decoded_session_key != b'':
                char = char ^ decoded_session_key[i]

            pkg_rc4key.append(char)

        encrypted_data = data[16:]
        decrypted_data = ARC4.new(pkg_rc4key).decrypt(encrypted_data)
        block_size = decrypted_data[:4]
        block = decrypted_data[4:len(decrypted_data) - 20]
        sha1hash = data[len(data) - 20:]

        h = SHA1.new()

        # we only need an encrypted block without size and key to compare hashes
        h.update(data[20:len(data) - 20])
        h.update(self.decrypted_hashkey)

        print('calculated hash = ' + str(h.digest()))
        print('received hash = ' + str(data[len(data) - 20:]))
        print("SHA1 valid: " + str(bytearray(h.digest()) == sha1hash))

        print(block)

        return decrypted_data
