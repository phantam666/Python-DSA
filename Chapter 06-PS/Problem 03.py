p1 = "lot of money"
p2 = "check earn"
p3 = "buy now"
p4 = "check"

massage = input("Enter a message: ")
if((p1 in massage) or (p2 in massage) or (p3 in massage) or (p4 in massage)):
    print("Spam")
else:(print("Not Spam"))