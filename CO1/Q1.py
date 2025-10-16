y1=int(input("Enter starting year"))
y2=int(input("Enter ending year"))
if y1>y2:
    print("End year must be greater  than starting year")
else:
    print(f"leap years from{y1}to{y2}")
    for year in range(y1,y2+1):
        if(year % 4==0 and year % 100 !=0) or (year % 400 == 0):
           print(year)
