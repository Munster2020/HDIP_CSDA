# Calculate Body Mass Index (BMI)
# Uses centimetres for height and kilograms for weight

height = float(input("Enter your height in cms: "))
weight = float(input("Enter your weight in kg: "))

height = height / 100

bmi = weight / ( height ** 2)

bmi = round(bmi,2)

print ("Your BMI is:", bmi)


