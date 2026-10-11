a = int(input("EnterGujarati Marks :)"))
b = int(input("Enter Hindi Marks   :)"))
c = int(input("Enter English Marks :)"))
d = int(input("Enter Maths Marks   :)"))
e = int(input("Enter Science Marks :)"))

Total_Marks = a+b+c+d+e
ave = Total_Marks / 5
per = (Total_Marks / 500) *100

# Pass Or Fail Condition 
if ave >= 40:
    print("Pass")
else:
    print("Fail")

# subject maximum 33 marks pass

if a >= 33 and b >= 33 and c >= 33 and d >= 33 and e >= 33:
    print("Pass")
else:
    print("Fail")


# Grade In Marks based on percentage

if per >= 95:
    print("A+")
elif per >= 90:
    print("A")
elif per >= 85:
    print("B+")
elif per >= 75:
    print("B")
elif per >= 60:
    print("c")
else :
    print("D")



    
print("Total Makrs :)", Total_Marks)
print("Average ",ave)
print("Persentage Is :)",per)

