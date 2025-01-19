import time

# Using `+=`
start_time = time.time()
string = ""
for i in range(100000):
    string += "newstring"
print("Using +=:", time.time() - start_time)

# Using `+`
start_time = time.time()
string = ""
for i in range(100000):
    string = string + "newstring"
print("Using +:", time.time() - start_time)

# Using `.join()`
start_time = time.time()
string_list = []
for _ in range(100000):
    string_list.append("newstring")
string = "".join(string_list)
print("Using join:", time.time() - start_time)
