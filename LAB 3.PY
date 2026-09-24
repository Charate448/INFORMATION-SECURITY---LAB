import pandas as pd

pt=input("ENTER THE MESSAGE : ")
key=input("ENTER THE KEY : ")


pt = pt.replace(" ", "")
le=len(pt)
print(le)

key=key.upper()
pt=pt.upper()

key = key.replace("J", "I")
pt = pt.replace("J", "I")



key_matrix = ""

for ch in key:
    if ch.isalpha() and ch not in key_matrix:
        key_matrix += ch


alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

for ch in alphabet:
    if ch not in key_matrix:
        key_matrix += ch

print(key_matrix)

matrix = []

for i in range(0, 25, 5):
    matrix.append(list(key_matrix[i:i+5]))


df = pd.DataFrame(matrix)

print("\nKEY MATRIX:")
print(df)


pairs = []
i = 0

while i < le:
  if i == len(pt) - 1:
        pairs.append(pt[i] + "X")
        i += 1

  elif pt[i] == pt[i + 1]:
      pairs.append(pt[i] + "X")
      i += 1

  else:
      pairs.append(pt[i] + pt[i + 1])
      i += 2

print("PAIRS:", pairs)
print("\nPLAINTEXT PAIRS:")
print(pairs)



def find_position(letter):

    for row in range(5):
        for col in range(5):

            if matrix[row][col] == letter:
                return row, col



ct = ""

for pair in pairs:

    a = pair[0]
    b = pair[1]

    row1, col1 = find_position(a)
    row2, col2 = find_position(b)

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





#decryption
import pandas as pd

ct=input("ENTER THE CIPHER TEXT : ")
key=input("ENTER THE KEY : ")


ct = ct.replace(" ", "")
le=len(ct)
print(le)

key=key.upper()
ct=ct.upper()

key = key.replace("J", "I")
ct = ct.replace("J", "I")



key_matrix = ""

for ch in key:
    if ch.isalpha() and ch not in key_matrix:
        key_matrix += ch


alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

for ch in alphabet:
    if ch not in key_matrix:
        key_matrix += ch

print(key_matrix)

matrix = []

for i in range(0, 25, 5):
    matrix.append(list(key_matrix[i:i+5]))


df = pd.DataFrame(matrix)

print("\nKEY MATRIX:")
print(df)


pairs = []
i = 0

while i < le:
  if i == len(ct) - 1:
        pairs.append(ct[i] + "X")
        i += 1

  elif ct[i] == ct[i + 1]:
      pairs.append(ct[i] + "X")
      i += 1

  else:
      pairs.append(ct[i] + ct[i + 1])
      i += 2

print("PAIRS:", pairs)
print("\nPLAINTEXT PAIRS:")
print(pairs)



def find_position(letter):

    for row in range(5):
        for col in range(5):

            if matrix[row][col] == letter:
                return row, col



pt = ""

for pair in pairs:

    a = pair[0]
    b = pair[1]

    row1, col1 = find_position(a)
    row2, col2 = find_position(b)

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


print("\nPLAINTEXT:")
print(pt)
