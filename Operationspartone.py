file = open('codingal.txt','r')
print(file.read())
file.close()


print()
print()



file = open('codingal.txt','r')
print("\n read in parts \n")
print(file.read(8))
file.close()




file = open('codingal.txt','r')
file.write('codingal.txt','a')
file.close()


