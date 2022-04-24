
f = open("table.txt", 'w')
# for i in range(100):
#     f.write(f"{i}\n")

# for change number of column modify code below
f.write("| First Header  | Second Header |")
f.write("\n| ------------- | ------------- |")

# for change number of row modify code below
for i in range(0, 91):
    f.write(f"\n| {i}  |  |")

