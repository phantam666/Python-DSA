with open("story.txt", "r") as f:
    constent = f.read()

    with open("note.txt","w") as f:
        f.write(constent)
        f.close()