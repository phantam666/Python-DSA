with open("loge.txt", "r") as f:
    constant1 = f.read()

with open("new loge.txt", "r") as f:
    constant2 = f.read()

if(constant1 == constant2):
    print("Yes, this file are indentical")
else:
    print("No, this file are not indentical")