#qno1
items=[3,2,2,4,9,5,6]
r_items=items.pop(4)
items.insert(2,r_items)
items.append(10)
print(items)

#qno2
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
common_elements=first_set.intersection(second_set)
if common_elements:
    first_set.difference(second_set)
    print(f'common elements: {common_elements}')
else:
    print('no common elements')

#qno3
first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}
if first_set.issubset(second_set):
    print('first set is subset of second set')
else:
    print('first set is not subset of second set')

 #qno4
month= {'jan':47, 'feb':52, 'mar':47, 'apr':44, 'may':52, 'jun':53, 'jul':54, 'aug':44, 'sep':54,}
list[set(month.values())]
print(list(set(month.values())))

#qno5
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
a=set(sample_list)
print(tuple(a))

#qno6
club_A = {'ram', 'hari', 'shyam'}
club_B ={'ram', 'gita', 'hari'}
common_members = club_A.intersection(club_B)
if common_members:
    print(f'common members: {common_members}')
else:
    print('no common members')
    
#qno7
required_tasks = {"Email", "Report","Meeting"}
completed_tasks = {"Email", "Report"}
if required_tasks.issubset(completed_tasks):
    print("All tasks are completed.")
else:
    remaining_tasks = required_tasks.difference(completed_tasks)
    print("Remaining tasks:", remaining_tasks)


#qno 8

students = {'alice': 'alice67@gmail.com', 'bob': 'bob45@gmail.com', 'charlie': 'charlie33@gmail.com'}
name = input("Enter the name of the student: ")
if name in students:
    print(f'The student email is: {students[name]}')
else:
    print("Student not found.")


#qno 9

shopping_list = { 'Milk', 'Bread', 'Eggs'}
bought = {'Bread', 'Eggs'}
if shopping_list.intersection(bought):
    remaining_items = shopping_list.difference(bought)
    print("Remaining items to buy:", remaining_items)
else:
    print("Shopping complete.")

#qno 10

class_list = ['ram','sita','laxman']
name = input("Enter the name of the student: ")
if name in class_list:
    print(f'{name} is already present in the class list.')
else:
    class_list.append(name)
    print(f'{name} has been added to the class list.')

#qno 11
votes = ['Blue','Red','Blue','Green','Blue']
vote_count = votes.count('Blue')
if vote_count >= 3:
    print("Blue Wins")
else:
    print("Blue did not win")

#qno 12
grades = {'Ram': 92, 'Sita': 88}
name = input("Enter the name of the student: ")
if name in grades:
    print(f'{name}: {grades[name]}')
else:
    print("Grade is not available.")


#qno 13

applicant = {'name': 'Priya', 'skills': ['Java', 'SQL'],'experience': 1}
required_skills = {'Python', 'Java'}
if required_skills.intersection(applicant['skills']) and applicant['experience'] >= 2:
    print("Priya is qualified.")
else:
    print("Priya is not qualified.")


#qno 14

banned_items = {'scissors', 'knife', ' lighter'}
items = input("Enter the items you want to bring: ").lower()
weight = float(input("Enter the total weight of the bag: "))
if items not in banned_items and weight <= 7:
    print("Bag is allowed." )
else:
    print("Bag is not allowed.")

#qno 15

emp1 = {'name': 'John', 'salary': 7500}
emp2 = {'name': 'Emma', 'salary': 8000}
emp3 = {'name': 'Shyam', 'salary': 500}
emp3['salary'] = 8500
print(emp1)
print(emp2)
print(emp3)


#qno 16

ram = {"chocolate", 'ice cream', 'cookies'}
laxman = {"chocolate", 'pasta', 'cookies'}
if ram.intersection(laxman):
    print("Ram and Laxman have similar tastes in food.")
else:
    print("Ram and Laxman have different tastes in food.")


