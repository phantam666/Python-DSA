marks1 = int(input("Enter marks of subject 1: "))
marks2 = int(input("Enter marks of subject 2: "))
marks3 = int(input("Enter marks of subject 3: "))
marks4 = int(input("Enter marks of subject 4: "))

total_percentage = ((marks1 + marks2 + marks3 + marks4) / 400 )* 100

if(total_percentage >= 33 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33 and marks4 >= 33):
    print("You are pass:" , total_percentage)
    if(total_percentage >= 90):
        print("Grade A:", total_percentage)
    elif(total_percentage >= 80):
        print("Grade B:", total_percentage)
    elif(total_percentage >= 70):
        print("Grade C:", total_percentage)
    elif(total_percentage >= 60):
        print("Grade D:", total_percentage)
    elif(total_percentage >= 50):
        print("Grade E:", total_percentage)


else:
    print("You are fail, try next year:", total_percentage)
    