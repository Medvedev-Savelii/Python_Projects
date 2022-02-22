import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!$%^&"
t1 = input("What length would you like your password to be: ")
t2 = input("How many passwords would you like: ")

while 1:
	password_len = int(t1)
	password_count = int(t2)
	for x in range(0,password_count):
		password = ""
		for x in range(password_len):
			password_char = random.choice(chars)
			password = password + password_char
		print("Here is your password : ", password)
