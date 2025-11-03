import random 
num = int(input("Enter an integer: ")) #ask the user to enter a number

binary=bin(num)[2:]
print("Binary equivalent:", binary)

# Pick a random position from the binary string
position = random.randint(0, len(binary) - 1)
print("Random position chosen:", position)

# Get the bit at that position (from the right)
bit = binary[-(position + 1)]

# Check if the bit is 1 or 0
if bit == '1':
    print("True (bit is 1)")
else:
    print("False (bit is 0)")

#This code takes a number from the user and turns it into binary (a series of 1s and 0s). 
# Then it randomly picks one position in that binary number and checks the bit at that spot. 
# If the bit is 1, it prints “True”; if it’s 0, it prints “False.” It’s a fun way to explore how
#  numbers look in binary and randomly test one of their bits.