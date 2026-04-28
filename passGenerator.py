import random

# low case letters
alphabet = [chr(i) for i in range(97, 123)]

# upper case letters
alphabet += [chr(i) for i in range(65, 91)]

# digits
alphabet += [str(i) for i in range(10)]

# special characters
alphabet += ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']

# Generate a random password of 18 characters
def passGenerator():
    temp = []
    for _ in range(18):
        temp.append(random.choice(alphabet))

    # make sure the password contains at least one character from each category
    if not any(c.islower() for c in temp):
        temp[random.randint(0, 17)] = random.choice([c for c in alphabet if c.islower()])

    # randomize again the string
    random.shuffle(temp)

    print("Password: " + ''.join(temp))

if __name__ == "__main__":
    passGenerator()