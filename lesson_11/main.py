import random

N = 20

list_ = []

for element in range(N):
    list_.append(random.randint(1, 1000))

print(list_)

list_.sort(reverse=True)

print(list_)



sorted_list = sorted(list_, reverse=True)

print(sorted_list)

list_of_names = [
    "John Doe",
    "Jane Smith",
    "Alice Johnson",
    "Bob Brown",
    "Charlie Davis",
    "Eve White",
    "Frank Black",
    "Grace Green",
    "Hannah Blue",
    "Ian Gray",
    ]


sorted_names = sorted(list_of_names, key=lambda x: x.split(' ')[1])
print(sorted_names)

dictionary = {
    'Jane': 90,
    'John': 85,
    'Alice': 95,
    'Bob': 80,
    'Charlie': 88,
    'Eve': 92,
    'Frank': 87,
    'Grace': 67,
    'Hannah': 89,
    'Ian': 84,
    'Walter': 72,
}

sorted_dict = dict(sorted(dictionary.items(), key=lambda x: x[1]))
print(dictionary)
print(sorted_dict)



# Bubble Sort

unsorted_data = [897,2,75,5,3,7,8,3,5,7,1,2,23,56,234]
length = len(unsorted_data)

for i in range(length):
    for j in range(length-i-1):
        if unsorted_data[j] < unsorted_data[j+1]:
            unsorted_data[j], unsorted_data[j+1] = unsorted_data[j+1], unsorted_data[j]

print(unsorted_data)

