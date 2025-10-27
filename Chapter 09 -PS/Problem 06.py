with open("loge.txt","r") as f:
    lines = f.readlines()

lineno  = 1
for line in lines :
    if("in" in line):
        print(f"Yes in is present. line no = {lineno}")

        break
    lineno += 1

else:
     print("No in is present.")