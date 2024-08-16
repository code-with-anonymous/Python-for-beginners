set1 = {8, 5, 4, 6432, 21, "harry"}  # Initialize the set with given elements
set1.add("rayyan")  # Add "rayyan" to the set
print(set1)  # Print the set after adding "rayyan"

set1.remove("harry")  # Remove "harry" from the set
print(set1) 

set1.pop()  # Remove and return an arbitrary element from the set
print(set1)  

i = {93, 32}  
union_set = set1.union(i)  # Perform a union with set i
print(union_set)  

intersection_set = set1.intersection(i)  # Perform an intersection with set i
print(intersection_set)  
