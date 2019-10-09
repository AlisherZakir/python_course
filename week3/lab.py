# 2.1 (A) Check and fix variable name
import re
def is_valid_name(name):
    return not re.search(r"\W", name) and not re.search(r"^[^a-zA-Z_]", name)

def fix_variable(name):
    if not is_valid_name(name):
        return re.sub(r"^[^a-zA-Z_]|\W", "_", name)
    else:
        return name

# (H) Lists

# 1. Create a list containing the strings "football","rugby","hockey" and "tennis".
a = ["football", "rugby", "hockey", "tennis"]
# 2. Print the first and last elements of the list
print(a[0], a[-1])
# 3. Add the element "cycling" to the end of the list.
a.append("cycling")
# 4. Print how many elements the list has.
print(len(a))
# 5. Print the first letter of each element of the list
for i in a:
    print(i[0])
# 6. Remove the element "football".
print(a.remove("football"))
# 7. Create a new list containing only the middle 2 elements of the current list.
b = a[1:3]
print(b)


# pop: removes and returns the removed element
# remove: removes an occurence of x without returning the element

# (H) Iteration
def load(weights):
    capacity = 3000
    loaded = 0
    weight = weights[0]
    i = 0
    while capacity - loaded >= weight and i < len(weights):
        print("%i was loaded" % weight)
        loaded += weight
        i += 1
        weight = weights[i]
    print("total weight: %i" % loaded)


load( [750, 387, 291, 712, 100, 622, 109, 750, 282])
