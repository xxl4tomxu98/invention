'''You know how sometimes you write the the same word twice in a sentence,
but then don't notice that it happened? For example, you've been distracted
for a second. Did you notice that *"the"* is doubled in the first
sentence of this description? As as aS you can see, it's not easy to
spot those errors, especially if words differ in case, like *"as"* at
the beginning of the sentence. Write a function that counts the number of
sections repeating the same word (case insensitive). The occurence of
two or more equal words next after each other count as one.
Example:
"dog cat"                 --> 0
"dog DOG cat"             --> 1
"apple dog cat"           --> 0
"pineapple apple dog cat" --> 0
"apple     apple dog cat" --> 1
"apple dog apple dog cat" --> 0
"dog dog DOG dog dog dog" --> 1
"dog dog dog dog cat cat" --> 2
"cat cat dog dog cat cat" --> 3
'''


def count_adjacent_pairs(st):
    st = st.lower()
    st_list = [i for i in st.split(' ')]
    count = 0
    l1 = [st_list[0]]
    for ele in st_list[1:]:
        if ele == l1[-1]:
            if len(l1) == 1 or ele != l1[-2]:
                count += 1
            # don't want to double count when repeat >2
            elif ele == l1[-2]:
                pass
            l1.append(ele)
        else:
            l1.append(ele)
    return count
