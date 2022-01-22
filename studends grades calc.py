sub1=int(input("mark of first subject:"))
sub2=int(input("mark of second subject:"))
sub3=int(input("mark of third subject:"))
sub4=int(input("mark of fourth subject:"))
avg =(sub1+sub2+sub3+sub4)/4
if avg >= 91:
    print("grade: AA")
elif (81 <= avg < 90):
    print("grade: AB")
elif (71 <= avg < 80):
    print("grade: BB")
elif (61 <= avg < 70):
    print("grade: BC")
elif (51 <= avg < 60):
    print("grade: CD")
elif (41 <= avg < 50):
    print("grade: DD")
elif avg <= 40:
    print("Fail")