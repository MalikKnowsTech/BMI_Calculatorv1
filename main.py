height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2)
bmi_as_int = (bmi)

if bmi_as_int <18.5:
    print(f"Your BMI is {bmi_as_int}, you are underweight.")
elif bmi_as_int >18.5:
    print(f"Your BMI is {bmi_as_int}, you have a normal weight.")
elif bmi_as_int <25:
    print(f"Your BMI is {bmi_as_int}, you have a normal weight.")
elif bmi_as_int >25:
    print(f"Your BMI is {bmi_as_int}, you are slightly overweight.")
elif bmi_as_int <35:
    print(f"Your BMI is {bmi_as_int}, you are obese.")
else:
    print:(f"Your BMI is {bmi_as_int}, you are clinically obese.")