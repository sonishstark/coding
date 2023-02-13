weight = int(input("Weight: "))
measure = input("(K)g or (L)bs: ")
if measure.upper() == str('K'):
    sum = int(weight * 2.20462)
    print("Weight in lbs: " + str(sum))
elif measure.upper() == str('L'):
    sum = int(weight / 2.20462)
    print("weight in Kg: " + str(sum))
else:
    print("Invalid Input")