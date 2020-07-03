list_a = []
with open('ex23.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        list_a.append(line.strip())

        line = open_file.readline()
print(list_a)

list_b = []
with open('ex23a.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        list_b.append(line.strip())

        line = open_file.readline()
print(list_b)

list_c = []

for i in list_a:
    if i in list_b:
        list_c.append(i)

print(list_c)

overlap_list = [elem for elem in list_a if elem in list_b]
print(overlap_list)