# Read in user data
print("What is your name?")
name = input()

print("What is your age?")
age = int(input())

print("What is your weight?")
weight = float(input())

print("What is your height?")
height = float(input())

# Calculate bmi
bmi = weight / (height ** 2)

# Display result
print(f"{name} your bmi is {bmi}")



# Read in data
print("Please enter number of lives")
lives = int(input())

print("Please enter energy level")
energy = int(input())

print("Please enter shield level")
shield = int(input())

# Display bot data
print(f"Lives:  {'♥' * lives}")
print(f"Energy: {'♦' * energy}")
print(f"Shield: {'♦' * shield}")

