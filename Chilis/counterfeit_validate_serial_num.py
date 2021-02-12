'''Given a array of string serial numbers, validate how many are valid
by check the following
1. strings are between 10-12 characters long
2. first three characters are distinct uppercase Letters
3. next four chars are digits and the years between 1900-2019 inclusive
4. next 2-4 chars are denomination of notes which says
    they have to be one of following [10, 20, 50, 100, 200,
    500, 1000]
5. The last char is one of the uppercase letters '''


import os


def countCounterfeit(serialNumber):
    # Write your code here
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    valid_values = []  # int array of valid note denominators

    serialNumber1 = [item for item in serialNumber if len(item) >= 10
                     and len(item) <= 12]

    serialNumber2 = [item for item in serialNumber1 if
                     all(char in letters for char in item[0:3])]

    serialNumber3 = [item for item in serialNumber2 if item[0] != item[1] and
                     item[0] != item[2] and item[2] != item[1]]

    serialNumber4 = [item for item in serialNumber3 if
                     all(char in digits for char in item[3:7])]

    serialNumber5 = [item for item in serialNumber4 if int(item[3:7]) >= 1900
                     and int(item[3:7]) <= 2019]

    serialNumber6 = [item for item in serialNumber5 if
                     len(item) == 10 and item[7:9] in ['10, 20', '50'] or
                     len(item) == 11 and item[7:10] in ['100, 200', '500'] or
                     len(item) == 12 and item[7:11] == '1000']

    serialNumber7 = [item for item in serialNumber6 if
                     len(item) == 10 and item[9] in letters or
                     len(item) == 11 and item[10] in letters or
                     len(item) == 12 and item[11] in letters]

    for serial_num in serialNumber7:
        # identify note values and put them
        if len(serial_num) == 10:
            valid_values.append(int(serial_num[7:9]))
        if len(serial_num) == 11:
            valid_values.append(int(serial_num[7:10]))
        if len(serial_num) == 12:
            valid_values.append(int(serial_num[7:11]))
    return sum(valid_values)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = list(map(str, input().rstrip().split()))

    print(countCounterfeit(s))

    # fptr.close()
