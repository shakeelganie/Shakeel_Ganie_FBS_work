'''A list contains sublist with Emp information as follows :
Data = [[101,”Seema”,45000],[340,”Rajani”,13000],
[210,”Tannu”,14000],[320,”Suresh”,35000]]
Write a program to sort the list based on salary.'''

Data = [
    [101, "Seema", 45000],
    [340, "Rajani", 13000],
    [210, "Tannu", 14000],
    [320, "Suresh", 35000]
]

# Sort by salary (3rd element)
sorted_data = sorted(Data, key=lambda x: x[2])  

print("Employees sorted by salary:")
for emp in sorted_data:
    print(emp)
