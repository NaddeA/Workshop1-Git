
import string

class Caesar:
    
    def __init__(self, shift):
        self.shift = shift
    
        alphabet = string.ascii_lowercase
        shifted_alphabet = alphabet[shift:] + alphabet[:shift]

        self._encrypt_table = alphabet.maketrans(alphabet, shifted_alphabet)
        self._decrypt_table = {v: k for k, v in self._encrypt_table.items()}

    


    def encrypt(self, plaintext):
    
        as_lower = plaintext.lower()

        return str.translate(as_lower, self._encrypt_table)


    def decrypt(self, cipher):
    
        decrypt_lower = cipher.lower()

        return str.translate(decrypt_lower, self._decrypt_table)





