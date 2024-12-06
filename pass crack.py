import itertools
import string
import time

def crack_password(target_password):
    # Define the character set: lowercase, uppercase, and digits
    charset = string.ascii_letters + string.digits

    # Start timing the cracking process
    start_time = time.time()

    # Try all possible lengths starting from 1
    for length in range(1, 9):  # Adjust the max length as needed
        for guess in itertools.product(charset, repeat=length):
            guess_password = ''.join(guess)
            if guess_password == target_password:
                elapsed_time = time.time() - start_time
                print(f'Password "{target_password}" cracked! It took {elapsed_time:.2f} seconds.')
                return guess_password

    print('Password not found.')
    return None

# Example usage
if __name__ == "__main__":
    target = input("Enter the password to crack: ")
    cracked_password = crack_password(target)
