from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
password = f.encrypt("Hello".encode())

with open("config.txt", "w") as f:
    f.write("key," + key.decode())
    f.write("\npassword," + password.decode())

with open("config.txt", "r") as f:
    lines = f.readlines()

read_key = lines[0].split(",")[1]
read_encrypted_pass = lines[1].split(",")[1]

print("read key: " + read_key)
print("read encrypted password: " + read_encrypted_pass)
new_fernet = Fernet(read_key)
read_decrypted_pass = new_fernet.decrypt(read_encrypted_pass.encode()).decode()
print("Read Passowrd: " + read_decrypted_pass)
