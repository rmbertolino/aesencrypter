from aesencrypter import EncryptString, DecryptString

plain_string = "Hello, World!!"
secret_key = "9ka87c30-9889-77a4-24-7ce56a47-6718-41a4-8677-52fe438d4f7b"
e = EncryptString(plain_string, secret_key)
d = DecryptString(e, secret_key)
print("Plain String.......: " + plain_string)
print("Encrypted String...: " + e)
print("Decrypted String...: " + d)