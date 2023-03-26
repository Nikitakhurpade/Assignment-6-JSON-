#Assignment 1
# 1.Create a JSON file (employee.json) containing employee information of minimum 5 employees. 
# Each employee information consists of Name, DOB, Height, City, State.
# Write a python program that reads this information from the JSON file and 
# saves the information into a list of objects of Employee class. 
# Finally print the list of the Employee objects.
import json
file = open('C:\\Users\\Assignment_6\\employee.json','r') #change the file path while running the code
data = file.read()
file.close()
user1 = json.loads(data) 
print(user1) 

