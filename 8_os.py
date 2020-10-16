import os

print(os.environ)               # print env variables

fd = "test_file"
try:
    os.rename(fd, "error.log")
except FileNotFoundError:
    print("File not found!")    # rename file

os.chdir("C:")                  # change working directory
print(os.getcwd())              # get current working directory

os.system("ipconfig")           # run command

stream = os.popen("ipconfig")   # run command
output = stream.read()          # and capture its output
print(output[:11])
