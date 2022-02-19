import rsa

message = "Hello iam chris"

publicKey, privateKey =rsa.newkeys(512)
print(publicKey,privateKey)

encrypt_message = rsa.encrypt(message.encode(),publicKey)
print(encrypt_message)

decrypt_message = rsa.decrypt(encrypt_message, privateKey).decode()
print(decrypt_message)


with open ("testing.txt", "wb") as file: 
    file.write(encrypt_message)