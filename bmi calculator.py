height = input("Please enter your height. ")
weight = input("Please enter your weight. ")
height = int(height)
weight = int(weight)
height =height / 100
bmi = weight / height /height   # or height ** 2

if bmi < 0.00185:
    print("your bmi is", bmi, "Underweight")
elif bmi > 0.00185 and bmi <= 0.00249:
    print(bmi, "Normal weight")
elif bmi > 0.00249 and bmi <+ 0.00299:
    print(bmi, "Overweight")
else :
    print(bmi, "Obese")
