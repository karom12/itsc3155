# Write a Python program that will find all numbers between two given numbers divisible by 7 but not a multiple of 5. (5 points)
userNum1 = int(input("Please enter first number: "))
userNum2 = int(input("Please enter second number: "))
#initiating result
output = "" 
#Using a loop for the range to get the outputs
for i in range (userNum1, userNum2):
    if(i % 7 == 0 and i % 5 != 0):
        output += str(i) + ","
#output
print(output)

