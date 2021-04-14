from cryptography.fernet import Fernet


def load_key():
    return open("key.key", "rb").read()


def decrypt_file(filename, key):
    f = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    with open(filename, "wb") as file:
        file.write(decrypted_data)


if __name__ == '__main__':
    key = load_key()
    decrypt_file("test_file.txt", key)
