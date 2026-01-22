hieght= int(input("Enter the height in cm: "))
wieght= int(input("Enter the weight in kg: "))
bmi= wieght/(hieght/100)**2

if bmi<18.5:
    print("You are underweight")
    
elif 18.5<=bmi<24.9:
    print("You are healthy")

elif 29.9<=bmi<30:
    print("You are overweight")
    
elif bmi>=34.9:
    print("You are severely overweight")
    
elif 24.9<=bmi<29.9:
    print("You are slightly overweight")
    
else: 
    print("Invalid Input")
    
