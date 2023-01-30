# Sets and Frozen sets

# Lists and sets are very similar
# Sets are unordered

# Create a set

car_parts = {"wheels", "doors", "exhaust"}
# print(car_parts)

# remove things from a set
car_parts.discard("doors")
# print(car_parts)

# add things to a set
car_parts.add("windows")
print(car_parts)

# Frozen sets

# frozen sets are immutable (cannot be changed or manipulated) versions of a set. Still unordered and un-indexed

x = frozenset([1, 2 ,3 , 4, "Five"])
print(x)