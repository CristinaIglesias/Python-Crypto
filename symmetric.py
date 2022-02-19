
from cryptography.fernet import Fernet

message = "Hello, my name is Carol"

key = Fernet.generate_key()
print(key)

f_object = Fernet(key)

encrypted_message = f_object.encrypt(message.encode())
print(encrypted_message)

decrypted_message = f_object.decrypt(encrypted_message).decode()
print(decrypted_message)

with open ("test.txt", "wb") as file: 
    file.write(encrypted_message)


