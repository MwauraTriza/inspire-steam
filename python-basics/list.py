#Name: Triza Mwaura
#Date: 18/02/2026
#program to show lists in python

friends = ["racheal","monica","phiby"]
print(friends)
friends.sort()
print(friends)

friends.reverse()
print(friends)

friends.append("jack")
print(friends)

new_friends=["joy","mary","kesy"]
print(len(new_friends))

#new list of students
students=friends+new_friends
print(students)
students.pop()
print(students)
students.insert(3, "abby")
print(students)
students.extend("Dan")
print(students)

students.remove("monica")
print (students)

new_students = students.copy()
print(new_students)


 