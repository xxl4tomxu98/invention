sequence_num = int(input('please enter the number of Fibonnaci sequence: '))
sequence = []
sequence.append(1)
sequence.append(1)
i = 2
while i <= sequence_num -1 :
    sequence.append(sequence[i-2] + sequence[i-1])
    i += 1
print(sequence)