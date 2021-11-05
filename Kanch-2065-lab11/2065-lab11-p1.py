import random
import string
"""
Kanch Ruansiripiyakul 633040206-5
"""

# characters to generate password from
upper_letter = random.choice(string.ascii_uppercase)
lower_letter = random.choice(string.ascii_lowercase)
characters = list(string.digits + "!@#$%^&*()")
password = ''.join(random.choice(characters)
                   for i in range(7)) + upper_letter + lower_letter
print(f"Random password is: {password}")
