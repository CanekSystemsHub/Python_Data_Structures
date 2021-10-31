# using a hashtable to count individual items


# define a set of items that we want to count
items = ["apple", "pear", "orange", "banana", "apple", "Tuna",
         "orange", "apple", "pear", "banana", "orange", "Tuna",
         "apple", "kiwi", "pear", "apple", "orange", "Tuna",
         "Tuna", "Tuna", "Tuna",]

# TODO: create a hashtable object to hold the items and counts
counter = dict()

# TODO: iterate over each item and increment the count for each one
for item in items:
    if (item in counter.keys()):
        counter[item] += 1
    else:
        counter[item] = 1


# print the results
print(counter)
