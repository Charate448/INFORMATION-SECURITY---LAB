
Ct=input("Enter your Encrypted Code: ")
key=int(input("Enter your shift key: "))
PT=""

for i in Ct:
  if i.isalpha():
    if i.isupper():
      asc= (ord(i)-key)
      if asc < ord('A'):
        asc += 26
      Pt = chr(asc)
    elif i.islower():
      asc = ord(i) - key
      if asc < ord('a'):
        asc += 26
      Pt = chr(asc)
    else:
        Pt += i
        

    PT ="".join([PT,Pt ])
  

print(PT)


