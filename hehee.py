file_name = "shopping_list.txt"
shopping_file = open(file_name, "w")
shopping_file.write("shopping list\n")
shopping_file.write("1. milk\n")
shopping_file.write("2. bread\n")
shopping_file.write("3. eggs\n")
shopping_file.write("4. apples\n")
shopping_file.close()


print("shopping list created successfully!")

shopping_file = open(file_name, "r")
print("\n==== full shopping list ====")
content = shopping_file.read()
print(content)

shopping_file.close()


shopping_file = open(file_name, "a")
shopping_file.write("5. rice\n")
shopping_file.write("6. butter\n")
shopping_file.write("7. juice\n")

shopping_file.close()


print("new item added to the shopping list!")

shopping_file = open(file_name, "r")


print("/n==== reading shopping list line by line ====")

line_number = 1


for line in shopping_file:
    print("line", line_number, ":", line.strip())
    line_number = line_number + 1

shopping_file.close()

