#name:triza mwaura
#date:24/02/2026
#program to show file handling in Python


#create new file 
import os


new_file = open("newfile.txt", "r+")

#write to new file
new_file.write("student name: triza mwaura ,ID:22202666 , email:trizamwaura@gmail.com,course:law ")
new_file.close()


#read from file
new_file = open("newfile.txt", "r")
data=new_file.read()
print(data)
new_file.close()

#delete file
#import os
os.remove("remove.txt")


#delete folder