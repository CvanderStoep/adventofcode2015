import time

# Using `+=`
start_time = time.time()
string = ""
for i in range(10000):
    string += "newstring"
print("Using +=:", time.time() - start_time)

# Using `.join()`
start_time = time.time()
string_list = ["newstring" for i in range(10000)]
string = "".join(string_list)
print("Using join:", time.time() - start_time)
