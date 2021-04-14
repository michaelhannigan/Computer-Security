from cryptography.fernet import Fernet

# creates a key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


# gets the key from our saved file
def load_key():
    return open("key.key", "rb").read()


def encrypt_file(filename, key):

    f = Fernet(key)
    with open(filename, "rb") as file:
        file_contents = file.read()

    encrypted_contents = f.encrypt(file_contents)
    with open(filename, "wb") as file:
        file.write(encrypted_contents)





if __name__ == '__main__':
    write_key()
    key = load_key()
    encrypt_file("test_file.txt", key)




