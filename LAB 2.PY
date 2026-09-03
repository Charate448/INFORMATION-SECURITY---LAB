#encryption

PT = input("ENTER THE PLAIN TEXT : ")
R = int(input("ENTER THE NUMBER OF RAILS : "))
CT = ""
rail = [""] * R
PT= PT.replace(" ","")


row = 0
direction = 1


for ch in PT:
    rail[row] = rail[row] + ch

    if row == 0:
        direction = 1
    elif row == R - 1:
        direction = -1

    row = row + direction

for i in range(R):
    CT = CT + rail[i]

print("CIPHER TEXT :", CT)



#decryption
CT = input("ENTER THE CIPHER TEXT : ")
R = int(input("ENTER THE NUMBER OF RAILS : "))
PT = ""
rail = [""] * R
CT= CT.replace(" ","")

row = 0
direction = 1

for ch in CT:
    rail[row] = rail[row] + " "


    if row == 0:
        direction = 1
    elif row == R - 1:
        direction = -1

    row = row + direction




ct = 0

for i in range(R):
    for j in range(len(rail[i])):
        rail[i] = rail[i][:j] + CT[ct] + rail[i][j + 1:]
        ct = ct + 1
        



row = 0
direction = 1

for ch in CT:
    PT = PT + rail[row][0]
    rail[row] = rail[row][1:]

    if row == 0:
        direction = 1
    elif row == R - 1:
        direction = -1

    row = row + direction


print("PLAIN TEXT :", PT)