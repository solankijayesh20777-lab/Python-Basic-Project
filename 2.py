a = int(input("EnterGujarati Marks :)"))
b = int(input("Enter Hindi Marks   :)"))
c = int(input("Enter English Marks :)"))
d = int(input("Enter Maths Marks   :)"))
e = int(input("Enter Science Marks :)"))

Total_Marks = a+b+c+d+e
ave = Total_Marks / 5
per = (Total_Marks / 500) *100

if ave >= 35:
    print("Pass")
else:
    print("Fail")

    
print("Total Makrs :)", Total_Marks)
print("Average ",ave)
print("Persentage Is :)",per)





