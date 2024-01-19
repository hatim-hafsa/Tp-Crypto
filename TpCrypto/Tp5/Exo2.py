import hashlib

input_md5 = "hafsa"  

#1:
list_lowercase = [chr(i) for i in range(97, 123)]

for char1 in list_lowercase:
    for char2 in list_lowercase:
        for char3 in list_lowercase:
            for char4 in list_lowercase:
                password = char1 + char2 + char3 + char4
                hashed_password = hashlib.md5(password.encode()).hexdigest()
                if hashed_password == input_md5:
                    print("Password found:", password)
                    exit()

#2:
list_all_letters = [chr(i) for i in range(65, 91)] + list_lowercase

for char1 in list_all_letters:
    for char2 in list_all_letters:
        for char3 in list_all_letters:
            for char4 in list_all_letters:
                password = char1 + char2 + char3 + char4
                hashed_password = hashlib.md5(password.encode()).hexdigest()
                if hashed_password == input_md5:
                    print("Password found:", password)
                    exit()

#3:
list_letters_numbers = [chr(i) for i in range(48, 58)] + list_all_letters

for char1 in list_letters_numbers:
    for char2 in list_letters_numbers:
        for char3 in list_letters_numbers:
            for char4 in list_letters_numbers:
                password = char1 + char2 + char3 + char4
                hashed_password = hashlib.md5(password.encode()).hexdigest()
                if hashed_password == input_md5:
                    print("Password found:", password)
                    exit()

#4: 
list_letters_numbers_8_chars = [chr(i) for i in range(48, 58)] + list_all_letters

for char1 in list_letters_numbers_8_chars:
    for char2 in list_letters_numbers_8_chars:
        for char3 in list_letters_numbers_8_chars:
            for char4 in list_letters_numbers_8_chars:
                password = char1 + char2 + char3 + char4
                hashed_password = hashlib.md5(password.encode()).hexdigest()
                if hashed_password == input_md5:
                    print("Password found:", password)
                    exit()

print("Password not found.")