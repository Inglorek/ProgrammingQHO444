# Retrieve what the user heard
print("What did I hear?")
heard = input()

# Retrieve what the user saw
print("What did I see?")
saw = input()

# Decide the outcome - both conditions must be true
if (heard == "grrr") and (saw == "two red eyes"):
    print("There is a scary creature. I should get out of here!")
else:
    print("I am a little scared but I will continue.")