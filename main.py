value = "cynthia"
sub_string = input("enter value of substring: ")
k = value.index(sub_string)
right_values = value[k+1:]
print(right_values)

#fist assignment
value = "cynthia"
sub_string = input("enter value of substring: ")
k = value.index(sub_string)
left_values = value[:k-0]
print(left_values)

#second assignment
name = "amaka"
start = name.index("a")
next = name.find("a", start+2)
print(next)

