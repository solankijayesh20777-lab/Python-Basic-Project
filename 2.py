a = int(input("EnterGujarati Marks :)"))
b = int(input("Enter Hindi Marks   :)"))
c = int(input("Enter English Marks :)"))
d = int(input("Enter Maths Marks   :)"))
e = int(input("Enter Science Marks :)"))

Total_Marks = a+b+c+d+e
ave = Total_Marks / 5
per = (Total_Marks /5)*100

print("Total Makrs :)", Total_Marks)
print("Average ",ave)
print("Persentage Is :)",per)

print(per >= 35)
print(per >= 75)




