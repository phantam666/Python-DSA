with open("story.txt","w") as f:
    f.write("Donkey Monkey is a brother but Monkey is clever and Donkey is Donkey")

l = ["Donkey", "Monkey"]

with open("story.txt","r") as f:
   constant =  f.read()

for word in l:
    constant = constant.replace(word, "#"*len(word))

    with open("story.txt","w") as f:
        f.write(constant)   

        f.close()

