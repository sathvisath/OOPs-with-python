def marks(sub1,sub2,sub3,sub4,sub5):
    return sub1+sub2+sub3+sub4+sub5
def cal_percentage(total):
    return (total/150)*100
sub1 = int(input("Enter sub1 marks: "))
sub2 = int(input("Enter sub2 marks: "))
sub3 = int(input("Enter sub3 marks: "))
sub4 = int(input("Enter sub4 marks: "))
sub5 = int(input("Enter sub5 marks: "))
 
total = marks(sub1,sub2,sub3,sub4,sub5)
percentage = cal_percentage(total)

print("Total marks are : ", total)
print("Percentage is: ",percentage)

if percentage<=40:
    print("You are fail")
else:
    print("You are pass")
