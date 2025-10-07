englishorfrench = []
Ses = 0
Tes = 0
englishorfrench = input("Input your sentence: ")
for char in englishorfrench:
    if char == "S":
        Ses = Ses + 1
    elif char == "s":
        Ses = Ses + 1
    elif char == "T":
        Tes = Tes + 1
    elif char == "t":
        Tes = Tes + 1
if Ses > Tes:
    print ("It's probally French")
elif Ses < Tes:
    print ("It's probally English")
elif Ses == Tes:
    print ("Its probally French")