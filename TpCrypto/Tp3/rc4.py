def encryption():
    global key, plain_text, n

    plain_text = "001010010010"
    key = "101001000001"
    n = 3

    print("Plain text : ", plain_text)
    print("Key : ", key)
    print("n : ", n)
    print(" ")

    S = [i for i in range(0, 2**n)]
    print("S : ", S)

    key_list = [key[i:i + n] for i in range(0, len(key), n)]

    for i in range(len(key_list)):
        key_list[i] = int(key_list[i], 2)

    global pt
    pt = [plain_text[i:i + n] for i in range(0, len(plain_text), n)]

    for i in range(len(pt)):
        pt[i] = int(pt[i], 2)

    print("Plain text ( in array form ): ", pt)

    diff = int(len(S)-len(key_list))

    if diff != 0:
        for i in range(0, diff):
            key_list.append(key_list[i])

    print("Key list : ", key_list)
    print(" ")

    def KSA():
        j = 0
        N = len(S)

        for i in range(0, N):
            j = (j + S[i]+key_list[i]) % N
            S[i], S[j] = S[j], S[i]

    print("KSA iterations : ")
    print(" ")
    KSA()
    print(" ")

    def PGRA():
        N = len(S)
        i = j = 0
        global key_stream
        key_stream = []

        for k in range(0, len(pt)):
            i = (i + 1) % N
            j = (j + S[i]) % N
            S[i], S[j] = S[j], S[i]
            t = (S[i]+S[j]) % N
            key_stream.append(S[t])

        print("Key stream : ", key_stream)
        print(" ")

    print("PGRA iterations : ")
    print(" ")
    PGRA()

    def XOR():
        global cipher_text
        cipher_text = []
        for i in range(len(pt)):
            c = key_stream[i] ^ pt[i]
            cipher_text.append(c)

    XOR()

    encrypted_to_bits = ""
    for i in cipher_text:
        encrypted_to_bits += '0'*(n-len(bin(i)[2:]))+bin(i)[2:]

    print(" ")
    print("Cipher text : ", encrypted_to_bits)

encryption()

print("---------------------------------------------------------")

def decryption():
    S = [i for i in range(0, 2**n)]

    key_list = [key[i:i + n] for i in range(0, len(key), n)]

    for i in range(len(key_list)):
        key_list[i] = int(key_list[i], 2)

    global pt
    pt = [plain_text[i:i + n] for i in range(0, len(plain_text), n)]

    for i in range(len(pt)):
        pt[i] = int(pt[i], 2)

    diff = int(len(S)-len(key_list))

    if diff != 0:
        for i in range(0, diff):
            key_list.append(key_list[i])

    print(" ")

    def KSA():
        j = 0
        N = len(S)

        for i in range(0, N):
            j = (j + S[i]+key_list[i]) % N
            S[i], S[j] = S[j], S[i]

    print("KSA iterations : ")
    print(" ")
    KSA()
    print(" ")

    def do_PGRA():
        N = len(S)
        i = j = 0
        global key_stream
        key_stream = []

        for k in range(0, len(pt)):
            i = (i + 1) % N
            j = (j + S[i]) % N
            S[i], S[j] = S[j], S[i]
            t = (S[i]+S[j]) % N
            key_stream.append(S[t])

    print("Key stream : ", key_stream)
    print(" ")

    print("PGRA iterations : ")
    print(" ")
    do_PGRA()

    def do_XOR():
        global original_text
        original_text = []
        for i in range(len(cipher_text)):
            p = key_stream[i] ^ cipher_text[i]
            original_text.append(p)

    do_XOR()

    decrypted_to_bits = ""
    for i in original_text:
        decrypted_to_bits += '0'*(n-len(bin(i)[2:]))+bin(i)[2:]

    print(" ")
    print("Decrypted text : ", decrypted_to_bits)

decryption()


