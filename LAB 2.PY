PT = input("ENTER THE PLAIN TEXT : ")
R = int(input("ENTER THE NUMBER OF RAILS : "))
CT = ""
rail = [""] * R

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

