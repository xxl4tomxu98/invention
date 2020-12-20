"""A recurring theme in Art+Logic projects is the need to process data that is provided in unusual or proprietary formats, regardless of whether a
project is targeting desktop, mobile, embedded, or the web, so asking applicants to demonstrate their ability to work with low-level data formats is
a traditional initial step.
For this challenge, we'll use a made-up format that encodes bundles of 4 characters by scrambling them into 32-bit integer values for
transmission, then reverses the operation on the receive end to reconstitute the original text.

The below image shows how the individual bits in the original raw text (top row) are mixed together into the 32-bit output value on the bottom row:

NOTE that in this image, the 0-9 and A-X are only used to identify individual bit positions within the 32-bit data. The position labeled 0 is the least
significant bit of the data, X is the most significant bit.
If this exercise seems contrived based on your experience, consider that it's at least vaguely similar to real-world things like Reed-Solomon error
correction codes or some interleaved data formats that might be transmitted by IoT edge devices.
Some examples should make things more clear.
Example 1: Single Character
When singleEncode a chunk with fewer than four characters, the input should be zero-padded to a length of four before singleEncode. The first character in
the input is treated as the least significant byte in the example images:

Example 2: Full Bundle
Here we see a complete chunk of 4-characters—refer to a table of ASCII character values to see how the incoming text data is shifted into the
Decoded/Raw buffer, and follow the individual bits into their final positions.

Example 3: Non-Alphanumerics
Another simple example with some characters outside of the regular alphanumeric range:

More examples

Raw Characters Encoded Value (dec)
"foo" 124807030
" foo" 250662636
"foot" 267939702
"BIRD" 251930706
"...." 15794160
"^^^^" 252706800
"Woot" 266956663
"no" 53490482
The Task
The task for part 1 of this challenge is to write just enough code to unlock the rest of it.
The task for part 2 of this challenge is to create a small application that is able to:
convert a string of arbitrary length into the corresponding list of integer values
convert a list of integer values back into the original string
This program can be a command line application that reads from stdin or a file and writes to stdout or a file, or could be a web page or
mobile/desktop app that uses a text edit box to accept input values by typing or pasting (or loading a file) and a button to convert that input into the
desired output format.
Your code to perform the encoding/decoding of data should be structured as if it were in a library, not tightly coupled to your demo application
(assume that our reviewers will want to call your code from a pre-existing test harness).
Specifically, for any valid string input s and your two functions named e.g. encode and decode, we expect to be able to successfully assert s ==
decode(encode(s)).
Your goal here isn't just to write code that does the barest minimum of work to barf out a correct answer; we're looking to get a taste of what your
habits and instincts are for writing production-quality code.
Example Data
String: tacocat
Encoded: [267487694, 125043731]
String: never odd or even
Encoded: [267657050, 233917524, 234374596, 250875466, 17830160]
String: lager, sir, is regal
Encoded: [267394382, 167322264, 66212897, 200937635, 267422503]
String: go hang a salami, I'm a lasagna hog
Encoded: [200319795, 133178981, 234094669, 267441422, 78666124, 99619077, 267653454, 133178165, 124794470]
String: egad, a base tone denotes a bad age
Encoded: [267389735, 82841860, 267651166, 250793668, 233835785, 267665210, 99680277, 133170194, 124782119]"""

import re


def singleEncode(str):
    str_rev = str[::-1]
    str_bin = [bin(x)[2:].zfill(8) for x in str_rev.encode('UTF-8')]
    result = ''
    for i in range(8):
        if len(str_bin) == 4:
            for j in range(4):
                result += str_bin[j][i]
        elif len(str_bin) < 4:
            for j in range(4-len(str_bin)):
                result += '0'
            for j in range(len(str_bin)):
                result += str_bin[j][i]
    return int(result, 2)


def encode(line):
    return [singleEncode(x) for x in [line[i:i+4] for i in
                                      range(0, len(line), 4)]]


def singleDecode(num):
    num_bin = bin(num)[2:]
    if len(num_bin) % 8 != 0:
        num_bin = '0'*(8-len(num_bin) % 8) + num_bin
    bin_arr = [num_bin[i:i+4] for i in range(0, len(num_bin), 4)]
    raw = ''
    for i in range(4):
        for j in range(8):
            raw += bin_arr[j][i]
    raw_arr = re.findall('.'*8, raw)
    char_arr = [chr(int(i, 2)) for i in raw_arr]
    return ''.join(char_arr)[::-1]


def decode(list1):
    return ''.join([singleDecode(x) for x in list1])


print(singleEncode("A"))
print(singleEncode("a@b."))
print(singleEncode(" foo"))
print(singleEncode("foo"))
print(singleEncode("BIRD"))
print(singleEncode("foot"))
print(singleEncode("...."))
print(singleEncode("^^^^"))
print(singleEncode("Woot"))
print(singleEncode("no"))
print(singleEncode("FRED"))
print(singleEncode("A"))
print(singleEncode(" :^)"))
print(singleEncode("tomx"))
print(singleEncode("taco"))
print(singleEncode("cat"))
print(singleEncode("neve"))
print(singleEncode("r od"))
print(singleEncode("d or"))
print(singleEncode(" eve"))
print(singleEncode("n"))

print(encode("never odd or even"))
print(encode("lager, sir, is regal"))
print(encode("go hang a salami, I'm a lasagna hog"))
print(encode("egad, a base tone denotes a bad age"))

print(singleDecode(16777217))
print(decode([267657050, 233917524, 234374596, 250875466, 17830160]))
print(decode([267394382, 167322264, 66212897, 200937635, 267422503]))
print(decode([200319795, 133178981, 234094669, 267441422, 78666124, 99619077, 267653454, 133178165, 124794470]))
print(decode([267389735, 82841860, 267651166, 250793668, 233835785, 267665210, 99680277, 133170194, 124782119]))


print(decode(encode('Woot')) == 'Woot')
