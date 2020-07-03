#with open('ex22.txt', 'r') as open_file:
#    all_text = open_file.read()
#    print(all_text)

counter_dictionary = {}
with open('ex22.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        line = line.strip()
        if line in counter_dictionary:
                counter_dictionary[line] += 1
        else:
                counter_dictionary[line] = 1
        line = open_file.readline()

print(counter_dictionary)


counter_dictionary = {}
with open('ex22a.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        line = line[3: -26]
        if line in counter_dictionary:
                counter_dictionary[line] += 1
        else:
                counter_dictionary[line] = 1
        line = open_file.readline()

print(counter_dictionary)