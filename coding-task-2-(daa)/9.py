import random

# Length of OTP and maximum attempts
OTP_LENGTH = 4
MAX_ATTEMPTS = 5

# Function to create a random OTP
def generate_otp():
    number = random.randint(0, 10**OTP_LENGTH - 1)
    return str(number).zfill(OTP_LENGTH)  # makes sure OTP has leading zeros if needed

# Main function
def main():
    otp = generate_otp()
    print("Your OTP (for demo):", otp)  # just to show for testing
    
    for attempt in range(1, MAX_ATTEMPTS + 1):
        guess = input(f"Enter the {OTP_LENGTH}-digit OTP (attempt {attempt}/{MAX_ATTEMPTS}): ")
        
        if guess == otp:
            print("Correct OTP! Verified successfully.")
            return
        else:
            print(" Incorrect OTP. Try again.")
    
    print("Too many wrong attempts. Please try again later.")

# Correct way to check if the file is run directly
if __name__ == "__main__":
    main()
