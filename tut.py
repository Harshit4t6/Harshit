"""This is a BMI Calculator"""
print("This is BMI Calculator")
name=str(input("Enter Your Name"))
mass=int(input("Enter your weight in Kg's : "))
height=float(input("Enter your height in meters : "))
#maths starts
BMI=mass/(height*height)
print(f'Hey {name}, your Height is {height} ,your weight is {mass}, your BMI is {BMI}')