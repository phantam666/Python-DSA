f = open("poem.txt", "w")
f.write( '''Whispers of the Starry Night 
In velvet skies, the stars take flight,
Glowing embers in the cloak of night.
Each spark a tale, a distant lore,
Of dreams untold, forevermore.'''
)

f = open("poem.txt", "r")
constant = f.read()


if("Night",constant):
    print("The word 'Night' is present in the file.")
else:
    print("The word 'Night' is not present in the file.")

f.close()

