#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_l = int(input("How many letters would you like in your password?\n")) 
nr_s = int(input("How many symbols would you like?\n"))
nr_n = int(input("How many numbers would you like?\n"))

#Method 1 
pw_l = random.sample(letters, nr_l) 
pw_n = random.sample(numbers, nr_n)
pw_s = random.sample(symbols, nr_n)

password = pw_l + pw_n + pw_s
random.shuffle(password)
print("".join(password))



#Method 2
# password = []
# for char in range(1, nr_l + 1):
#   password += random.choice(letters)

# for char in range(1, nr_s + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_n + 1):
#   password += random.choice(numbers)

# random.shuffle(password)
# pass_final = password
# print(''.join(pass_final))   