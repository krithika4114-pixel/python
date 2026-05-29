new_file = open('new_file.txt', 'x')
new_file.close()


import os

print("checking if my_file exists or not....")

if os.path.exists("my_file.txt"):
  os.remove("my_file.txt")
else:
  print("the file do not exists")



my_file = open("my_file.txt", "w")
my_file.write("Hi! I'm penguin and I am one year old")
my_file.close()