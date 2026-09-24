#CEASER CIPHER
def caesar_encrypt():
    text = input("ENTER THE PLAIN TEXT: ")
    key = int(input("ENTER THE SHIFT KEY: "))

    result = ""

    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - ord('A') + key) % 26 + ord('A'))

        elif ch.islower():
            result += chr((ord(ch) - ord('a') + key) % 26 + ord('a'))

        else:
            result += ch

    print("\nCIPHER TEXT:", result)


def caesar_decrypt():
    text = input("ENTER THE CIPHER TEXT: ")
    key = int(input("ENTER THE SHIFT KEY: "))

    result = ""

    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - ord('A') - key) % 26 + ord('A'))

        elif ch.islower():
            result += chr((ord(ch) - ord('a') - key) % 26 + ord('a'))

        else:
            result += ch

    print("\nPLAIN TEXT:", result)


def caesar_cipher():
    while True:
        print("\n---------- CAESAR CIPHER ----------")
        print("1. Encryption")
        print("2. Decryption")
        print("3. Back to Main Menu")

        choice = input("ENTER YOUR CHOICE: ")

        if choice == "1":
            caesar_encrypt()

        elif choice == "2":
            caesar_decrypt()

        elif choice == "3":
            break

        else:
            print("INVALID CHOICE!")



#PLAY FAIR CIPHER
def create_matrix(key):

    key = key.upper()
    key = key.replace("J", "I")

    key_matrix = ""

    
    for ch in key:
        if ch.isalpha() and ch not in key_matrix:
            key_matrix += ch

    
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    for ch in alphabet:
        if ch not in key_matrix:
            key_matrix += ch

    
    matrix = []

    for i in range(0, 25, 5):
        matrix.append(list(key_matrix[i:i + 5]))

    return matrix


def print_matrix(matrix):
    print("\nKEY MATRIX:")

    for row in matrix:
        print(" ".join(row))


def find_position(matrix, letter):

    for row in range(5):
        for col in range(5):

            if matrix[row][col] == letter:
                return row, col

    return None


def create_pairs(text):

    text = text.upper()
    text = text.replace(" ", "")
    text = text.replace("J", "I")

    pairs = []

    i = 0

    while i < len(text):

        if i == len(text) - 1:
            pairs.append(text[i] + "X")
            i += 1

        elif text[i] == text[i + 1]:
            pairs.append(text[i] + "X")
            i += 1

        else:
            pairs.append(text[i] + text[i + 1])
            i += 2

    return pairs


def playfair_encrypt():
    pt = input("ENTER THE PLAIN TEXT: ")
    key = input("ENTER THE KEY: ")

    matrix = create_matrix(key)

    print_matrix(matrix)

    pairs = create_pairs(pt)

    print("\nPLAINTEXT PAIRS:")
    print(pairs)

    ct = ""

    for pair in pairs:

        a = pair[0]
        b = pair[1]

        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        
        if row1 == row2:

            new_col1 = (col1 + 1) % 5
            new_col2 = (col2 + 1) % 5

            ct += matrix[row1][new_col1]
            ct += matrix[row2][new_col2]

        
        elif col1 == col2:

            new_row1 = (row1 + 1) % 5
            new_row2 = (row2 + 1) % 5

            ct += matrix[new_row1][col1]
            ct += matrix[new_row2][col2]

        
        else:

            ct += matrix[row1][col2]
            ct += matrix[row2][col1]

    print("\nCIPHERTEXT:")
    print(ct)


def playfair_decrypt():
    ct = input("ENTER THE CIPHER TEXT: ")
    key = input("ENTER THE KEY: ")

    matrix = create_matrix(key)

    print_matrix(matrix)

    ct = ct.upper()
    ct = ct.replace(" ", "")
    ct = ct.replace("J", "I")

    
    if len(ct) % 2 != 0:
        print("INVALID CIPHER TEXT!")
        return

    pairs = []

    for i in range(0, len(ct), 2):
        pairs.append(ct[i:i + 2])

    print("\nCIPHER TEXT PAIRS:")
    print(pairs)

    pt = ""

    for pair in pairs:

        a = pair[0]
        b = pair[1]

        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        
        if row1 == row2:

            new_col1 = (col1 - 1) % 5
            new_col2 = (col2 - 1) % 5

            pt += matrix[row1][new_col1]
            pt += matrix[row2][new_col2]

        
        elif col1 == col2:

            new_row1 = (row1 - 1) % 5
            new_row2 = (row2 - 1) % 5

            pt += matrix[new_row1][col1]
            pt += matrix[new_row2][col2]

        
        else:

            pt += matrix[row1][col2]
            pt += matrix[row2][col1]

    print("\nPLAIN TEXT:")
    print(pt)


def playfair_cipher():
    while True:

        print("\n---------- PLAYFAIR CIPHER ----------")
        print("1. Encryption")
        print("2. Decryption")
        print("3. Back to Main Menu")

        choice = input("ENTER YOUR CHOICE: ")

        if choice == "1":
            playfair_encrypt()

        elif choice == "2":
            playfair_decrypt()

        elif choice == "3":
            break

        else:
            print("INVALID CHOICE!")



#RAIL FENCE CIPHER
def rail_fence_encrypt():

    pt = input("ENTER THE PLAIN TEXT: ")
    R = int(input("ENTER THE NUMBER OF RAILS: "))

    if R <= 1:
        print("NUMBER OF RAILS MUST BE GREATER THAN 1!")
        return

    pt = pt.replace(" ", "")

    rail = [""] * R

    row = 0
    direction = 1

    for ch in pt:

        rail[row] += ch

        if row == 0:
            direction = 1

        elif row == R - 1:
            direction = -1

        row += direction

    ct = ""

    for i in range(R):
        ct += rail[i]

    print("\nCIPHER TEXT:")
    print(ct)


def rail_fence_decrypt():

    ct = input("ENTER THE CIPHER TEXT: ")
    R = int(input("ENTER THE NUMBER OF RAILS: "))

    if R <= 1:
        print("NUMBER OF RAILS MUST BE GREATER THAN 1!")
        return

    ct = ct.replace(" ", "")

    rail = [[""] * len(ct) for _ in range(R)]

    row = 0
    direction = 1

    for i in range(len(ct)):

        rail[row][i] = "*"

        if row == 0:
            direction = 1

        elif row == R - 1:
            direction = -1

        row += direction

    index = 0

    for i in range(R):

        for j in range(len(ct)):

            if rail[i][j] == "*":
                rail[i][j] = ct[index]
                index += 1

    pt = ""

    row = 0
    direction = 1

    for i in range(len(ct)):

        pt += rail[row][i]

        if row == 0:
            direction = 1

        elif row == R - 1:
            direction = -1

        row += direction

    print("\nPLAIN TEXT:")
    print(pt)


def rail_fence_cipher():

    while True:

        print("\n---------- RAIL FENCE CIPHER ----------")
        print("1. Encryption")
        print("2. Decryption")
        print("3. Back to Main Menu")

        choice = input("ENTER YOUR CHOICE: ")

        if choice == "1":
            rail_fence_encrypt()

        elif choice == "2":
            rail_fence_decrypt()

        elif choice == "3":
            break

        else:
            print("INVALID CHOICE!")




while True:


    print("\n       CRYPTOGRAPHY CIPHER MENU")
    print("1. CAESAR CIPHER")
    print("2. PLAYFAIR CIPHER")
    print("3. RAIL FENCE CIPHER")
    print("4. EXIT")

    choice = input("ENTER YOUR CHOICE: ")

    if choice == "1":
        caesar_cipher()

    elif choice == "2":
        playfair_cipher()

    elif choice == "3":
        rail_fence_cipher()

    elif choice == "4":
        print("\nPROGRAM EXITED.")
        break

    else:
        print("\nINVALID CHOICE! PLEASE TRY AGAIN.")

