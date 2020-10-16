while True:
	try:
		test_number = int(input("Enter your age: "))
	except ValueError:
		print("Not a valid number!")
	else:
		print(f"You are {test_number} years old")
		break
