dictionary = { 'Aman':'25', 'Rohit':'30', 'Gary':'35', 'Prachi':'42' }

user = input("Enter the student's name: ")

if user in dictionary:
    print(user , "'s Marks: " , dictionary[user])
else:
    print("Student not found")
