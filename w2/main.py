# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
heightFloat = float(height)
weightInt = int(weight)
BMI = weightInt/(heightFloat**2)
BMI = int(BMI)

# added to code
healthy = True

print(f"\nThe total BMI for this person is {BMI}. ")
healthy = input("Is this BMI healthy? ")

print("\n\nDoctor's Note:")
print(f"\tBMI: {BMI}")
print(f"\tHeathy: {healthy}")
