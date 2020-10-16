f = open("test_file", "w")
for i in range(10):
	f.write(f"This is line {i+1}\n")
	
f.open("test_file", "r")
print(f.read())

f.open("test_file", "r")
for line in f.readlines():
	print(line)
	
f.close()
