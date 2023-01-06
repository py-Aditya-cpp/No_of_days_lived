def no_of_days_lived():
    bd = input("Enter your DOB (in DDMMYYYY): ")
    cd = input("Enter today's date (in DDMMYYYY): ")

    y1=int(bd[-4:])
    y2=int(cd[-4:])
    m1=int(bd[2:4])
    m2=int(cd[2:4])
    d1=int(bd[:2])
    d2=int(cd[:2])

    def is_leap(year):
        c=0
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    count+=1
            else:
                c+=1
        return(c)

    count=0            
    for i in range(y1, y2):
        if is_leap(i)==1:
            count+=1
    days_in_year=(y2-y1)*365+count

    m=[31,28,31,30,31,30,31,31,30,31,30,31]
    days_in_month=0
    for i in m[:m2-1]:
        days_in_month+=i

    if is_leap(y2)==1:
        if m2>1:
            days_in_month+=1

    days_to_sub=0
    for i in m[:m1-1]:
        days_to_sub+=i

    days_alive = days_in_year + days_in_month - days_to_sub + d2 - d1
    
    print("You've lived",days_alive,"days!")

no_of_days_lived()
z=input("Do you want to check another age?(y/n)")
while z=="y" or z=="Y":
    no_of_days_lived()
    z=input("Do you want to check another age?(y/n)")
