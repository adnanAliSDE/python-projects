'''The encrypter module is used to encrypt and decrypt textual data using cipher algorithm'''
def encrypt(text, shift=5):
    """This function encrypts the input text by shifting each character by a given number of positions to the right in the
    ASCII table."""
    
    result = ""
    for char in text:
        result += chr((ord(char) + shift) % 256)
    return result


def decrypt(text, shift=5):
    """
    This function decrypts the input text that was encrypted using the `encrypt` function by shifting each character
    back a given number of positions to the left in the ASCII table.
    """
    result = ""
    for char in text:
        result += chr((ord(char) - shift) % 256)
    return result
