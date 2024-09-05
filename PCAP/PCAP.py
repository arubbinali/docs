"""
بسم الله الرحمان الرحيم


--------------------------------------------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------------------------------------------
                                                        Module 1
--------------------------------------------------------------------------------------------------------------------------



1) import <library>, <library>...
        → library.identity()
2) from <library> import *
        → identity() 
        → `from x import y` tries to access y at import time.  `import x .....  def func(): x.y` doesn't access y until the function is run
3) from <library> import <identity>, <identity>...
4) import <library> as <alias>
5) from <library> import <identity> as <alias>, <identity> as <alias>...
6) dir(module)
        → Returns an alphabetically sorted list containing all entities' names available in the module
7) end="\t"
        → tab, moves the cursor (the textual one, like, where text is printed) to the next "tab stop"
8) math functions
        sin(x) → the sine of x
        cos(x) → the cosine of x
        tan(x) → the tangent of x
        asin(x) → the arcsine of x
        acos(x) → the arccosine of x
        atan(x) → the arctangent of x
        pi → a constant with a value that is an approximation of π
        radians(x) → a function that converts x from degrees to radians
        degrees(x) → acting in the other direction (from radians to degrees)
        sinh(x) → the hyperbolic sine
        cosh(x) → the hyperbolic cosine
        tanh(x) → the hyperbolic tangent
        asinh(x) → the hyperbolic arcsine
        acosh(x) → the hyperbolic arccosine
        atanh(x) → the hyperbolic arctangent
        e → a constant with a value that is an approximation of Euler's number (e)
        exp(x) → finding the value of e^x
        log(x) → the natural logarithm of x
        log(x, b) → the logarithm of x to base b
        log10(x) → the decimal logarithm of x (more precise than log(x, 10))
        log2(x) → the binary logarithm of x (more precise than log(x, 2))
        pow(x, y) → finding the value of x^y (mind the domains)
        ceil(x) → the ceiling of x (the smallest integer greater than or equal to x)
        floor(x) → the floor of x (the largest integer less than or equal to x)
        trunc(x) → the value of x truncated to an integer (be careful - it's not an equivalent either of ceil or floor)
        factorial(x) → returns x! (x has to be an integral and not a negative)
        hypot(x, y) → returns the length of the hypotenuse of a right-angle triangle with the leg lengths equal to x and y 
            → (the same as sqrt(pow(x, 2) + pow(y, 2)) but more precise)
10) seed() → to fix the random values for each time the program runs
        → seed() - sets the seed with the current time;
        → seed(int_value) - sets the seed with the integer value int_value
11) random module
        range → 0.0 <= random number < 1.0
        range(end)
        range(beg, end)
        range(beg, end, step)
        randrange(end)
        randrange(beg, end)
        randrange(beg, end, step)
        randint(left, right)
        range(end)
        range(beg, end)
        range(beg, end, step)
            → end is not included
12) choice function
        → inputs a sequence and returns a random number from the sequence
        → choice(sequence)
13) sample function
        → inputs a sequence and returns specified number of non repeating random numbers from the sequence
        → sample(sequence, elements_to_choose
14) platform function
        → to access the underlying platform's data, i.e., hardware, operating system, and interpreter version information
        → platform(aliased = False, terse = True) = platform(0, 1)
        → platform()
        → aliased → when set to True (or any non-zero value) it may cause the function to present the alternative underlying layer names instead of the common ones;
        → terse → when set to True (or any non-zero value) it may convince the function to present a briefer form of the result (if possible)
            → machine function
                → to know the generic name of the processor which runs your OS together with Python and your code
                → machine()
            → processor function
                → returns a string filled with the real processor name (if possible)
                → processor()
            → system function
                → returns the generic OS name as a string
                → system()
            → version function
                → returns OS version as a string
                → version()
            → python version function
                → python_implementation() → returns a string denoting the Python implementation
                → python_version_tuple() → returns a three-element tuple filled with:
                    → the major part of Python's version
                    → the minor part
                    → the patch level number
15) Python Module Index
        → https://docs.python.org/3/py-modindex.html
16) Auto generated module variables
        → when you run a file directly, its __name__ variable is set to __main__;
        → when a file is imported as a module, its __name__ variable is set to the file's name (excluding .py)
17) #!/usr/bin/env python3
18) sys library
        → import sys / from sys import path
19) path.append('..\\modules') / path.insert(index, '..\\modules')
20) pip (ON CMD commands)
        pip --version for current pip version
        pip help
            shows brief pip's description
        pip help <package name>
        pip list
            shows list of currently installed packages
        pip search <anystring>
            searches through PyPI directories in order to find packages which name contains <anystring>
        pip show <package name>
        pip install <package name>
            installs <package name> system-wide (expect problems when you don't have administrative rights)
        pip install --user <package name>
            install <package name> for you only; no other your platform's user will be able to use it
        pip install -U <package name>
            updates previously installed package
        pip install <package name> == <package version>
            e.g: pip install pygame == 1.9.2
        pip uninstall package_name
            uninstalls previously installed package


            
--------------------------------------------------------------------------------------------------------------------------
                                                        Module 2
--------------------------------------------------------------------------------------------------------------------------



21) Character sets / encoding schemes
        → ASCII
            → American Standard Code for Information Interchange
            → used mainly to encode the Latin alphabet and some of its derivates
        → Unicode
            → able to encode virtually all alphabets being used by humans
            → UCS-4 & UTF-8            
22) codepoint
        → a number corresponding to a particular character
23) BOM
        → Byte Order Mark, a special combination of bits announcing the encoding used by a file's contents (e.g. UCS-4 or UTF-8)
24) strings
        → len()
            → returns length of a string
        → backslash (\)
            → used as an escape character
            → e.g: print(len('I\'m')) outputs 3
        → multilines
            → a whitespace would add to the length of the string at every new line added
                multiline = '''Line #1
                Line #2'''
        → concatenation
        → replication
        → ord()
            → as in ordinal, to know a specific character's ASCII/UNICODE code point value
            → print(ord('a')) returns 97
        → chr()
            → takes a code point and returns its character
            → print(chr(97)) returns a
        → iteration through a string (using for loop)
        → slices
            → sample code
                
                alpha = "abdefg"

                print(alpha[1:3])   returns bd
                print(alpha[3:])    returns efg
                print(alpha[:3])    returns abd
                print(alpha[3:-2])  returns e
                print(alpha[-3:4])  returns e
                print(alpha[::2])   returns adf
                print(alpha[1::2])  returns beg

        → not
            → returns the inverse of the truth value of the operand it precedes
        → in
            → returns boolean
            → print("a" in "abc") returns TRUE
        → not in
            → returns boolean
            → print("a" not in "abc") returns FALSE
        → del
            → deletes a string or a list or an element from a list
        → min()
            → min("aA") returns A and not a since ASCII of A is 65 and the ASCII of a is 97
            → min([0, 1, 2]) returns 0
        → max()
            → max("aA") returns a and not A since ASCII of a is 97 and the ASCII of A is 65
            → max([0, 1, 2]) returns 2
        → index()
            → method, not a function
            → searches the sequence from the beginning, in order to find the first element of the value specified in its argument
            → its absence will cause a ValueError exception
            → print("abcabc".index("c")) returns 2
        → list()
            → takes its argument (a string) and creates a new list containing all the string's characters, one per list element
            → list("abcabc") returns ['a', 'b', 'c', 'a', 'b', 'c']
        → count()
            → counts all occurrences of the element inside the sequence
            → counts all occurrences of the element inside the sequence
            → print("abcabc".count("x")) returns 0
        → center()
            → adds spaces before and after a string
            → sample code

                print("[" + "house".center(5) + "]") returns [house]
                    → no spaces as house is 5 letters already

                print("[" + "house".center(10) + "]") returns [  house   ]
                    → 5 spaces left as house is 5 letters, 2 and 2 go on both sides, the 1 left over is added to the end (right)
        → startswith()
            → takes a string and returns boolean
            → checks if a given string starts with the specified substring
        → endswith()
            → takes a string and returns boolean
            → checks if a given string ends with the specified substring
        → find()
            → takes a string and returns the index of the string from where the string to find starts
            → returns -1 if a non existent substring is fed as a parameter
        → rfind()
            → starts the search from the end of the string
            → syntax: string.rfind(search_string, start, end)
            → print("Python is awesome, isn't it?".rfind('is'))         returns 7
            → print("Python is awesome, isn't it?".rfind('is', 7, 18))  returns 19
        → isalnum()
            → as in, is a letter number
            → returns boolean
            → returns True if the string fed only contains digits and letters
        → isalpha()
            → returns boolean
            → returns True only if the string fed only contains letters
        → isdigit()
            → returns boolean
            → returns True only if the string fed only contains digits
        → isspace()
            → returns boolean
            → returns True when the string fed only contains whitespaces
        → islower()
            → returns boolean
            → returns True if the string fed only consists of lower case letters
        → isupper()
            → returns boolean
            → returns True if the string fed only consists of lower case letters
        → join()
            → performs a join, expects one argument as a list and all elements must be strings
            → print(",".join(["a", "b", "c"])) returns a,b,c
        → upper()
            → makes a copy of a source string, replaces all lower-case letters with their upper-case counterparts
        → lower()
            → makes a copy of a source string, replaces all upper-case letters with their lower-case counterparts
        → swapcase()
            → makes a new string by swapping the case of all letters within the source string
        → strip()
            → checks if a given string starts with the specified substring
            → combines the effects caused by rstrip() and lstrip()
            → print("[" + "   abcde   ".strip() + "]") returns [abcde]
        → lstrip()
            → returns a newly created string formed from the original one by removing all leading whitespaces
            → print("[" + " abc ".lstrip() + "]") returns [abc ]
            → print("www.cisco.com".lstrip("w.")) returns cisco.com
            → returns the main string if the substring fed is the last part of the main string
        → rstrip()
            → returns a newly created string formed from the original one by removing all whitespaces from the end of the 
            → print("[" + " abc ".rstrip() + "]") returns [ abc]
            → print("[" + "  a b c d e f  ".rstrip("e f") + "]") returns [a b c d]
            → returns the main string if the substring fed is the first part of the main string
        → replace()
            → print("apple juice".replace("apple", "mango")) returns mango juice
            → print("apple apple apple apple juice".replace("apple", "mango", 2)) returns mango mango apple apple juice
        → split()
            → splits the string and builds a list of all detected substrings, assumes that the substrings are delimited by whitespaces
            → print("a       b\nc".split()) returns ['a', 'b', 'c']
        → title()
            → changes every word's first letter to upper-case, turning all other ones to lower-case
        → capatilize()
            → converts the letter at index 0 to upper case and the rest to lower case
        → comparison operators
            → compares code point values, character by character
            →
                ==  → equals to
                !=  → not equals to
                >   → greater than
                >=  → greater than and equals to
                <   → lesser than
                <=  → lesser than and equals to

            → 'beta' > 'Beta' returns True
            → upper-case letters are taken as lesser than lower-case
            →
            
                '10' == '010'   returns False
                '10' > '010'    returns True
                '10' > '8'      returns False
                '20' < '8'      returns True
                '20' < '80'     returns True
                '10' == 10      returns False
                '10' != 10      returns True
                '10' == 1       returns False
                '10' != 1       returns True
                '10' > 10       TypeError exception
                'smith' > 'Smith'   returns True
                    → 's' > 'S' as 115 > 83
                'Smiths' < 'Smith'  returns False
                    → 's' > '' (an empty string, which is considered to have a value less than any character)
                'Smith' > '1000'    returns True
                    → 'S' > '1' as 83 > 49
                '11' < '8'          returns True
                    → '1' < '8' as 49 < 56

        → sorting 
            → to sort elements in a list
            → sort()
                → list.sort()
                → returns a new list
            → sorted()
                → sorted(list)
                → no new list is created
            → str()
                → converts a number to a string
            → int()
                → converts a string to an integer
            → float()
                → converts a string to a decimal point number
25) Projects:
        1) A LED Display
    
            digits = [ '1111110',  	# 0
            '0110000',	# 1
            '1101101',	# 2
            '1111001',	# 3
            '0110011',	# 4
            '1011011',	# 5
            '1011111',	# 6
            '1110000',	# 7
            '1111111',	# 8
            '1111011',	# 9]


            def print_number(num):
                global digits
                digs = str(num)
                lines = [ '' for lin in range(5) ]
                for d in digs:
                    segs = [ [' ',' ',' '] for lin in range(5) ]
                    ptrn = digits[int(d)]
                    if ptrn[0] == '1':
                        segs[0][0] = segs[0][1] = segs[0][2] = '#'
                    if ptrn[1] == '1':
                        segs[0][2] = segs[1][2] = segs[2][2] = '#'
                    if ptrn[2] == '1':
                        segs[2][2] = segs[3][2] = segs[4][2] = '#'
                    if ptrn[3] == '1':
                        segs[4][0] = segs[4][1] = segs[4][2] = '#'
                    if ptrn[4] == '1':
                        segs[2][0] = segs[3][0] = segs[4][0] = '#'
                    if ptrn[5] == '1':
                        segs[0][0] = segs[1][0] = segs[2][0] = '#'
                    if ptrn[6] == '1':
                        segs[2][0] = segs[2][1] = segs[2][2] = '#'
                    for lin in range(5):
                        lines[lin] += ''.join(segs[lin]) + ' '
                for lin in lines:
                    print(lin)


            print_number(int(input("Enter the number you wish to display: ")))

        2) Split function
            
                def mysplit(string):
                    list_form = list(string)
                    if string.isspace() == True or string == "":
                        return []
                    elif list_form[0].isspace() and list_form[-1].isspace():
                        return string.strip()
                    else:
                        out_list = []        
                        temp_string = ""
                        for element in list_form:
                            if not element.isspace():
                                temp_string = temp_string + element
                            if element.isspace():
                                out_list.append(temp_string)
                                temp_string = ""
                        out_list.append(temp_string)
                        return out_list
                    

                print(mysplit("To be or not to be, that is the question"))
                print(mysplit("To be or not to be,that is the question"))
                print(mysplit("   "))
                print(mysplit(" abc "))
            
            3) Encryption

                def encrypt(line, shift):
                    outline = ""
                    for character in line:
                        outcharacter = character
                        if character.isdigit(): outline += character

                        elif character.isalpha():
                            if character.isupper():
                            outcharacter.upper()
                            ascii = ord(outcharacter) + int(shift)
                            if ascii <= 90: outcharacter = chr(ascii)
                            else: outcharacter = chr(ascii - 26)
                            else:
                            outcharacter.lower()
                            ascii = ord(outcharacter) + int(shift)
                            if ascii <= 122: outcharacter = chr(ascii)
                            else: outcharacter = chr(ascii - 26)

                            outline += outcharacter

                        elif character.isspace(): outline += character
                    print(outline)

                line = input("Enter text: ")

                while True:
                    try:
                        shift = int(input("Enter number of shifts: "))
                        if shift in range(1, 26):
                            break
                    except:
                        print("go again")

                encrypt(line, shift)

            4) Palindromes

                def palindrome(line):
                    count = 0
                    length = len(line) - 1
                    lineupper = line.upper()

                    if (length + 1) % 2 == 1:
                        lineodd = lineupper.replace(lineupper[int(length/2)], "")
                        
                    for letter in range(int((length)/2)):
                    if (length + 1) % 2 == 1:
                        if lineodd[letter] == lineodd[-letter - 1]:
                            count += 1
                    else:
                        if lineupper[letter] == lineupper[-letter - 1]:
                            count += 1
                    
                    if count == int((length)/2):
                        print("It's a palindrome")
                    else:
                        print("It's not a palindrome")
                        
                palindrome("Eleven animals I slam in a net")
            
            5) Anagrams

                def anagram(line1, line2):
                    global count
                
                    line1upper = line1.upper()
                    line2upper = line2.upper()
                    
                    for letter in range(len(line1)):
                        if not line1upper[letter].isspace(): list1.append(line1upper[letter])
                        if not line2upper[letter].isspace(): list2.append(line2upper[letter])
                    
                    if not (line1 == "" and line2 == ""):
                            
                    list1.sort()
                    list2.sort()
                    
                    string1 = "".join(list1)
                    string2 = "".join(list2)

                    if string1 == string2:
                        print("Anagrams")
                    else: print("Not anagrams")

                    else: print("Not anagrams")
                        
                count, list1, list2 = 0, [], []
                first = input()
                second = input()
                anagram(first, second)

                OR (solution):
                str_1 = input("Enter the first string: ")
                str_2 = input("Enter the second string: ")

                strx_1 = ''.join(sorted(list(str_1.upper().replace(' ',''))))
                strx_2 = ''.join(sorted(list(str_2.upper().replace(' ',''))))
                if len(strx_1) > 0 and strx_1 == strx_2:
                    print("Anagrams")
                else:
                    print("Not anagrams")


            6) Sum of dates
                
                def lifedigits(date): #YYYYMMDD
    
                    sum, final = 0, 0
                    
                    for _ in range(len(date)):
                    sum +=  int(date[_])
                    
                    if len(str(sum)) < 10:
                    print(sum)
                    else:
                    nsum = str(sum)
                    for _ in range(len(nsum)):
                        final += int(nsum[_])
                    print(final)
                    
                lifedigits(input())

            7) Finding a word in a string
                
                def wordfind(word, line):
                    found, start = True, 0

                    for character in word:
                        
                        pos = line.find(character, start)
                        
                        if pos == -1:
                            found = False
                            break
                        start = pos + 1

                    if found:        print("Yes")
                    else: print("No")

                word = input().lower()
                line = input().lower()

                wordfind(word, line)
                
            8) Sudoku

                def sudoku(datatype):

                    if datatype == "custom":
                    
                        board = [([[] for _ in range(9)]) for x in range(9)]


                        for row in range(3):
                            line = input()
                            for column in range(3):
                                board[row][column] = line[column]
                    
                    if datatype == "grid":
                        #sample board (correct)
                        board = [
                        ['2', '9', '5', '7', '4', '3', '8', '6', '1'],
                        ['4', '3', '1', '8', '6', '5', '9', '2', '7'],
                        ['8', '7', '6', '1', '9', '2', '5', '4', '3'],
                        ['3', '8', '7', '4', '5', '9', '2', '1', '6'],
                        ['6', '1', '2', '3', '8', '7', '4', '9', '5'],
                        ['5', '4', '9', '2', '1', '6', '7', '3', '8'],
                        ['7', '6', '3', '5', '2', '4', '1', '8', '9'],
                        ['9', '2', '8', '6', '7', '1', '3', '5', '4'],
                        ['1', '5', '4', '9', '3', '8', '6', '7', '2']]


                        numbers, blockcount, rowcount, columncount = [1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 0, 0
                        
                        #rows check
                        row1 = board[0]
                        row2 = board[1]
                        row3 = board[2]
                        row4 = board[3]
                        row5 = board[4]
                        row6 = board[5]
                        row7 = board[6]
                        row8 = board[7]
                        row9 = board[8]

                        for x in range(9):
                            if str(numbers[x]) in str(row1):
                                rowcount += 1

                        for x in range(9):
                            if str(numbers[x]) in str(row2):
                                rowcount += 1

                        for x in range(9):
                            if str(numbers[x]) in str(row3):
                                rowcount += 1

                        for x in range(9):
                            if str(numbers[x]) in str(row4):
                                rowcount += 1

                        for x in range(9):
                            if str(numbers[x]) in str(row5):
                                rowcount += 1

                        for x in range(9):
                            if str(numbers[x]) in str(row6):
                                rowcount += 1

                        for x in range(9):
                            if str(numbers[x]) in str(row7):
                                rowcount += 1

                        for x in range(9):
                            if str(numbers[x]) in str(row8):
                                rowcount += 1

                        for x in range(9):
                            if str(numbers[x]) in str(row9):
                                rowcount += 1

                        #columns check
                        col1, col2, col3, col4, col5, col6, col7, col8, col9 = [], [], [], [], [], [], [], [], []

                        #create columns' lists
                        for _ in range(9):
                            col1.append(board[_][0])

                        for _ in range(9):
                            col2.append(board[_][1])

                        for _ in range(9):
                            col3.append(board[_][2])

                        for _ in range(9):
                            col4.append(board[_][3])

                        for _ in range(9):
                            col5.append(board[_][4])

                        for _ in range(9):
                            col6.append(board[_][5])

                        for _ in range(9):
                            col7.append(board[_][6])

                        for _ in range(9):
                            col8.append(board[_][7])

                        for _ in range(9):
                            col9.append(board[_][8])


                        #check columns
                        for x in range(9):
                            if str(numbers[x]) in str(col1):
                                columncount += 1

                        for x in range(9):
                            if str(numbers[x]) in str(col2):
                                columncount += 1

                        for x in range(9):
                            if str(numbers[x]) in str(col3):
                                columncount += 1

                        for x in range(9):
                            if str(numbers[x]) in str(col4):
                                columncount += 1

                        for x in range(9):
                            if str(numbers[x]) in str(col5):
                                columncount += 1

                        for x in range(9):
                            if str(numbers[x]) in str(col6):
                                columncount += 1

                        for x in range(9):
                            if str(numbers[x]) in str(col7):
                                columncount += 1

                        for x in range(9):
                            if str(numbers[x]) in str(col8):
                                columncount += 1

                        for x in range(9):
                            if str(numbers[x]) in str(col9):
                                columncount += 1


                        #blocks check
                        block1 = board[0][:3],  board[1][:3],   board[2][:3]
                        block2 = board[0][3:6], board[1][3:6],  board[2][3:6]
                        block3 = board[0][6:],  board[1][6:],   board[2][6:]
                        block4 = board[3][:3],  board[4][:3],   board[5][:3]
                        block5 = board[3][3:6], board[4][3:6],  board[5][3:6]
                        block6 = board[3][6:],  board[4][6:],   board[5][6:]
                        block7 = board[6][:3],  board[7][:3],   board[8][:3]
                        block8 = board[6][3:6], board[7][3:6],  board[8][3:6]
                        block9 = board[6][6:],  board[7][6:],   board[8][6:]



                        for x in range(9):
                            if str(numbers[x]) in str((block1)):
                                blockcount += 1

                        for x in range(9):
                            if str(numbers[x]) in str((block2)):
                                blockcount += 1

                        for x in range(9):
                            if str(numbers[x]) in str((block3)):
                                blockcount += 1

                        for x in range(9):
                            if str(numbers[x]) in str((block4)):
                                blockcount += 1
                            
                        for x in range(9):
                            if str(numbers[x]) in str((block5)):
                                blockcount += 1

                        for x in range(9):
                            if str(numbers[x]) in str((block6)):
                                blockcount += 1

                        for x in range(9):
                            if str(numbers[x]) in str((block7)):
                                blockcount += 1

                        for x in range(9):
                            if str(numbers[x]) in str((block8)):
                                blockcount += 1
                            
                        for x in range(9):
                            if str(numbers[x]) in str((block9)):
                                blockcount += 1


                    if rowcount + columncount + blockcount == (9*9*3):
                        print("Yes")
                    else:
                        print("No")

                try:
                    datatype = input("What data do you want to use? Type \"custom\" and hit enter to enter your own sudoku puzzle, or \"grid\" to use an exisent grid:   ")
                    sudoku(datatype)
                except:
                    print("run the program again, either the text or board you entered, was erroneous...")

            OR

                # A function that checks whether a list passed as an argument contains
                # nine digits from '1' to '9'.
                def checkset(digs):
                    return sorted(list(digs)) == [chr(x + ord('0')) for x in range(1, 10)]


                # A list of rows representing the sudoku.
                rows = [ ]
                for r in range(9):
                    ok = False
                    while not ok:
                        row = input("Enter row #" + str(r + 1) + ": ")
                        ok = len(row) == 9 and row.isdigit()
                        if not ok:
                            print("Incorrect row data - 9 digits required")
                    rows.append(row)

                ok = True

                # Check if all rows are good.
                for r in range(9):
                    if not checkset(rows[r]):
                        ok = False
                        break

                # Check if all columns are good.	
                if ok:
                    for c in range(9):
                        col = []
                        for r in range(9):
                            col.append(rows[r][c])
                        if not checkset(col):
                            ok = False
                            break

                # Check if all sub-squares (3x3) are good.
                if ok:
                    for r in range(0, 9, 3):
                        for c in range(0, 9, 3):
                            sqr = ''
                            # Make a string containing all digits from a sub-square.
                            for i in range(3):
                                sqr += rows[r+i][c:c+3]
                            if not checkset(list(sqr)):
                                ok = False
                                break

                # Print the final verdict.
                if ok:
                    print("Yes")
                else:
                    print("No")

26) Execptions:
        ValueError
            raised when a function receives an argument of the correct type but an inappropriate value
            e.g:
                import math
                x = -1
                y = math.sqrt(x)
        ZeroDivisionError
            raised when an attempt is made to divide a number by zero
            e.g:
                value = 1
                value /= 0
        IndexError
            raised when you try to access an index that is out of the range of a sequence (such as a list, tuple, or string)
            e.g:
                my_list = []
                x = my_list[0]

27) Exceptions' mechanism
        1) if an error is encountered inside of the try block, the instructions after the specific line would be ignored:

                try:
                    print("1")
                    x = 1 / 0
                    print("2")
                except:
                    print("Oh dear, something went wrong...")

                print("3")

            output:
                1
                Oh dear, something went wrong...
                3
            
        2) Specifying exceptions
            if the try branch raises the exc1 exception, it will be handled by the except exc1: block;
            similarly, if the try branch raises the exc2 exception, it will be handled by the except exc2: block;
            if the try branch raises any other exception, it will be handled by the unnamed except block:
        
                try:
                    :
                except exc1:
                    :
                except exc2:
                    :
                except:
                    :

                --------------------------------------
                    
                try:
                    x = int(input("Enter a number: "))
                    y = 1 / x
                    print(y)
                except ZeroDivisionError:
                    print("You cannot divide by zero, sorry.")
                except ValueError:
                    print("You must enter an integer value.")
                except:
                    print("Oh dear, something went wrong...")

                print("THE END.")

        3) A drawback of specifying the exception
            e.g:
            
                try:
                    x = int(input("Enter a number: "))
                    y = 1 / x
                    print(y)
                except ValueError:
                    print("You must enter an integer value.")

                print("THE END.")

            the exception raised won't be handled by ValueError - it has nothing to do with it;
            as there's no other branch, you should to see this message:

            Traceback (most recent call last):
            File "exc.py", line 3, in 
            y = 1 / x
            ZeroDivisionError: division by zero

        4) tree-shaped hierarchy of the 63 buuilt in functions python 3 defines

            ZeroDivisionError is a special case of more a general exception class named ArithmeticError;
            ArithmeticError is a special case of a more general exception class named just Exception;
            Exception is a special case of a more general class named BaseException;
            We can describe it in the following way (note the direction of the arrows - they always point to the more general entity):

                BaseException
                    ↑
                Exception
                    ↑
                ArithmeticError
                    ↑
                ZeroDivisionError

        5) the hierarchy, how it functions
            1) e.g:

                    #code 1
                        try:
                            y = 1 / 0
                        except ZeroDivisionError:
                            print("Oooppsss...")

                        print("THE END.")

                    #code 2
                        try:
                            y = 1 / 0
                        except ArithemticError:
                            print("Oooppsss...")

                        print("THE END.")

                    output (both them codes outuput the same result):

                        Oooppsss...
                        THE END.

                to summarize:
                    each exception raised falls into the first matching branch;
                    the matching branch doesn't have to specify the same exception exactly - 
                    it's enough that the exception is more general (more abstract) than the raised one.

            2)e.g:

                #code 1
                    try:
                        y = 1 / 0
                    except ZeroDivisionError:
                        print("Zero Division!")
                    except ArithmeticError:
                        print("Arithmetic problem!")

                    print("THE END.")

                output 1:
                    Zero division!
                    THE END.

                
                #code 2
                    try:
                        y = 1 / 0
                    except ArithmeticError:
                        print("Arithmetic problem!")
                    except ZeroDivisionError:
                        print("Zero Division!")

                    print("THE END.")

                output 2:
                    Arithmetic problem!
                    THE END.
                

            Why, if the exception raised is the same as previously?

            The exception is the same, but the more general exception is now listed first - 
            it will catch all zero divisions too. It also means that there's no chance that any exception hits the ZeroDivisionError branch
            This branch is now completely unreachable

            Remember:

            the order of the branches matters!
            don't put more general exceptions before more concrete ones;
            this will make the latter one unreachable and useless;
            moreover, it will make your code messy and inconsistent;


        6) Handling 2 or more exceptions in one instruction

            try:
                :
            except (exc1, exc2):
                :

        7) Raised exceptions handled inside and outside of functions
            1) exceptions inside of functions
                e.g:

                    def bad_fun(n):
                        try:
                            return 1 / n
                        except ArithmeticError:
                            print("Arithmetic Problem!")
                        return None

                    bad_fun(0)

                    print("THE END.")

                output:
                    Arithmetic problem!
                    THE END.

            2) exceptions outside of functions
                e.g:

                    def bad_fun(n):
                        return 1 / n

                    try:
                        bad_fun(0)
                    except ArithmeticError:
                        print("What happened? An exception was raised!")

                    print("THE END.")

                output:
                    What happened? An exception was raised!
                    THE END.

            the exception raised can cross function and module boundaries, and travel through the invocation chain looking for a 
            matching except clause able to handle it.

            If there is no such clause, the exception remains unhandled, and Python solves the problem in its standard way - 
            by terminating your code and emitting a diagnostic message.

28) raise
        raises the specified exception named exc as if it was raised in a normal (natural) way
        
        The raise instruction may also be utilized in the following way (note the absence of the exception's name):
            raise
        
        There is one serious restriction: 
            this kind of raise instruction may be used inside the except branch only; using it in any other context causes an error.

        The instruction will immediately re-raise the same exception as currently handled.

        e.g:

            code:
                def bad_fun(n):
                    try:
                        return n / 0
                    except:
                        print("I did it again!")
                        raise


                try:
                    bad_fun(0)
                except ArithmeticError:
                    print("I see!")

                print("THE END.")
            
            outputs:

                I did it again!
                I see!
                THE END.

        
        The ZeroDivisionError is raised twice:
            first, inside the try part of the code (this is caused by actual zero division)
            second, inside the except part by the raise instruction.

29) assert
        assert is a statement, tests that a condition is true. If it's false, it raises AssertionError, otherwise nothing happens

        if the condition of the assert is true, the program does nothing on that line and continues running
        only if the assert is false does it raise an exception, which may stop the program if that exception is not caught

        e.g:
            
            import math

            x = int(input("Enter a number: "))
            assert x >= 0
            x = math.sqrt(x)
            print(x)

        output(input: 25):
            5.0
        
        outut(input: -1):
            Traceback (most recent call last):
            File "c:\Users\Micro\Desktop\desk\Code\PCAP\testing.py", line 4, in <module>
                assert x >= 0
                    ^^^^^^
            AssertionError

        e.g:

            def foo(x):
                assert x
                return 1/x


            try:
                print(foo(0))
            except ZeroDivisionError:
                print("zero")
            except:
                print("some")

        output:
            some

        reason:
            assertion error raised since any nunmber != 0 is True and 0 = False, so line 3 is skipped, and since the line's skipped, 
            no ZeroDivisionError either, this leaves us with the except block only since AssertionError isnt specified separately

30) Built-in exceptions
    1) ArithmeticError
        Location: BaseException ← Exception ← ArithmeticError
        Description: an abstract exception including all exceptions caused by arithmetic operations like zero division 
                     or an argument's invalid domain

    2) AssertionError
        Location: BaseException ← Exception ← AssertionError
        Description: a concrete exception raised by the assert instruction when its argument evaluates to False, None, 0, or an empty string
        e.g:    

            from math import tan, radians
            angle = int(input('Enter integral angle in degrees: '))

            # We must be sure that angle != 90 + k * 180
            assert angle % 180 != 90
            print(tan(radians(angle)))

    3) BaseException
        Location: BaseException
        Description: the most general (abstract) of all Python exceptions - all other exceptions are included in this one;
                     it can be said that the following two except branches are equivalent: except: and except BaseException:.
    
    4) IndexError
        Location: BaseException ← Exception ← LookupError ← IndexError
        Description: a concrete exception raised when you try to access a non-existent sequence's element (e.g., a list's element)
        e.g:

                # The code shows an extravagant way of leaving the loop.

                the_list = [1, 2, 3, 4, 5]
                ix = 0
                do_it = True

                while do_it:
                    try:
                        print(the_list[ix])
                        ix += 1
                    except IndexError:
                        do_it = False

                print('Done')

    5) KeyboardInterrupt
        Location: BaseException ← KeyboardInterrupt
        Description: a concrete exception raised when the user uses a keyboard shortcut designed to terminate a  program's execution 
                     (Ctrl-C in most OSs); if handling this exception doesn't lead to program termination,
                     the program continues its execution.
                     Note: this exception is not derived from the Exception class. Run the program in IDLE.
        e.g:

            # This code cannot be terminated by pressing Ctrl-C.

            from time import sleep

            seconds = 0

            while True:
                try:
                    print(seconds)
                    seconds += 1
                    sleep(1)
                except KeyboardInterrupt:
                    print("Don't do that!")

    6) LookupError
        Location: BaseException ← Exception ← LookupError
        Description: an abstract exception including all exceptions caused by errors resulting from invalid references to different 
                     collections (lists, dictionaries, tuples, etc.)

    7) MemoryError
        Location: BaseException ← Exception ← MemoryError
        Description: a concrete exception raised when an operation cannot be completed due to a lack of free memory.
        e.g:

            # This code causes the MemoryError exception.
            # Warning: executing this code may affect your OS.
            # Don't run it in production environments!

            string = 'x'
            try:
                while True:
                    string = string + string
                    print(len(string))
            except MemoryError:
                print('This is not funny!')

    8) OverflowError
        Location: BaseException ← Exception ← ArithmeticError ← OverflowError
        Description: a concrete exception raised when an operation produces a number too big to be successfully stored
        e.g:

            # The code prints subsequent values of exp(k), k = 1, 2, 4, 8, 16, ...

            from math import exp

            ex = 1

            try:
                while True:
                    print(exp(ex))
                    ex *= 2
            except OverflowError:
                print('The number is too big.')

    9) ImportError
        Location: BaseException ← Exception ← StandardError ← ImportError
        Description: a concrete exception raised when an import operation fails
        e.g:

            # One of these imports will fail - which one?

            try:
                import math
                import time
                import abracadabra

            except:
                print('One of your imports has failed.')

    10) KeyError
         Location: BaseException ← Exception ← LookupError ← KeyError
         Description: a concrete exception raised when you try to access a collection's non-existent element (e.g., a dictionary's element)
         e.g:

            # How to abuse the dictionary and how to deal with it?

            dictionary = { 'a': 'b', 'b': 'c', 'c': 'd' }
            ch = 'a'

            try:
                while True:
                    ch = dictionary[ch]
                    print(ch)
            except KeyError:
                print('No such key:', ch)

31) Mini task: Numbers in a range

    def read_int(prompt, min, max):
        run = True
        
        while run:
            try:
                prompt = int(input("Enter a number from -10 to 10: "))
                if min <= prompt <= max:
                        return prompt
                else:
                    print(f"Error: the value is not within permitted range ({min}..{max}) ")
            except ValueError:
                print("Error: wrong input")

    v = read_int("Enter a number from -10 to 10: ", -10, 10)
    print("The number is:", v)

32) Abstract and concrete exceptions
    1) Some abstract built-in Python exceptions are:

        ArithmeticError,
        BaseException,
        LookupError.

    2) Some concrete built-in Python exceptions are:

        AssertionError,
        ImportError,
        IndexError,
        KeyboardInterrupt,
        KeyError,
        MemoryError,
        OverflowError.

33) Exceptions' tree-shaped hierarchy

        BaseException
            Exception
                MemoryError
                AssertionError
                ArithmeticError
                    ZeroDivisionError
                    OverflowError
                LookUpError
                    IndexError
                    KeyError
            StandardError
                ImportError
            KeyboardInterrupt



--------------------------------------------------------------------------------------------------------------------------
                                                        Module 3
--------------------------------------------------------------------------------------------------------------------------



34) Classes & methods
        → A class is an idea (more or less abstract) which can be used to create a number of incarnations,
          such an incarnation is called an object.
        → A class is a set of objects
        → Classes form a hierarchy
        → If we want to hide any of a class's components from the outside world, we should start its name with __.
           Such components are called private.

35) Objects
        → An object is a being belonging to a class
        → An object is an incarnation of the requirements, traits, and qualities assigned to a specific class
        → This may mean that an object belonging to a specific class belongs to all the superclasses at the same time. 
            It may also mean that any object belonging to a superclass may not belong to any of its subclasses
        → Each subclass is more specialized (or more specific) than its superclass. 
            Conversely, each superclass is more general (more abstract) than any of its subclasses.
        → Its 3 group of attributes:
            → a name                                                - a noun
            → a set of individual properties                        - an adjective
            → a set of abilities to perform specific activities     - a verb
        → The part of the Python class responsible for creating new objects is called the constructor,
            and it's implemented as a method of the name __init__.

36) Inheritance
        → Any object bound to a specific level of a class hierarchy inherits all the traits 
            (as well as the requirements and qualities) defined inside any of the superclasses.
        → There's no obstacle to defining new, more precise subclasses. 
            They'll inherit everything from their superclass, so the work that went into its creation isn't wasted.
        → The new class may add new properties and new activities, and therefore may be more useful in specific applications. 
            Obviously, it may be used as a superclass for any number of newly created subclasses.

        → The process doesn't need to have an end. You can create as many classes as you need.
        → The class you define has nothing to do with the object: the existence of a class does not mean that any of the compatible 
            objects will automatically be created. 
        → The class itself isn't able to create an object - you have to create it yourself, and Python allows you to do this.

        → When a class is derived from another class, their relation is named inheritance. 
        → The class which derives from the other class is named a subclass. The second side of this relation is named superclass. 
        → A way to present such a relation is an inheritance diagram, where:
            → superclasses are always presented above their subclasses;
            → relations between classes are shown as arrows directed from the subclass toward its superclass.

37) Encapsulation
        → the ability to hide (protect) selected values against unauthorized access
        → the encapsulated values can be neither accessed nor modified if you want to use them exclusively
        → When any class component has a name starting with two underscores (__), it becomes private - 
            this means that it can be accessed only from within the class.
        → You cannot see it from the outside world. This is how Python implements the encapsulation concept.
    
38) Defining a class and an object

        class TheSimplestClass:
            pass
        
        my_first_object = TheSimplestClass()
        
39) Stacks
        → LIFO
        → An object with 2 elementary operations:
            → push (when a new element is put on the top)
            → pop (when an existing element is taken away from the top)

        → The procedural approach

            code:

                stack = []

                def push(number):
                    stack.append(number)
                def pop():
                    output = stack[-1]
                    del stack[-1]
                    return output

                push(1)
                push(2)
                push(3)

                print(pop())
                print(pop())
                print(pop())

                print(stack)

            output:

                3
                2
                1
                []

        → The object approach
                
            code:

                class Stack():
                    def __init__(self):
                        self.__stack = []

                    def push(self, val):
                        self.__stack.append(val)

                    def pop(self):
                        output = self.__stack[-1]
                        del self.__stack[-1]
                        return output
                    
                    def show(self):
                        print(self.__stack)
                        
                stack_object = Stack()

                stack_object.push(1)
                stack_object.push(2)
                stack_object.push(3)

                print(stack_object.pop())
                print(stack_object.pop())
                print(stack_object.pop())

                stack_object.show()

            output:

                3
                2
                1
                []

40) 2+ objects in a class

    code:

        class Stack:
            def __init__(self):
                self.__stack_list = []

            def push(self, val):
                self.__stack_list.append(val)

            def pop(self):
                val = self.__stack_list[-1]
                del self.__stack_list[-1]
                return val
            
            def show(self):
                print(self.__stack_list)


        stack_object_1 = Stack()
        stack_object_2 = Stack()

        stack_object_1.push(3)
        stack_object_2.push(stack_object_1.pop())

        print(stack_object_2.pop())

        stack_object_1.show()
        stack_object_2.show()

    output:

        3
        []
        []


    code:

        class Stack:
            def __init__(self):
                self.__stack_list = []

            def push(self, val):
                self.__stack_list.append(val)

            def pop(self):
                val = self.__stack_list[-1]
                del self.__stack_list[-1]
                return val
            
            def show(self):
                print(self.__stack_list)


        little_stack = Stack()
        another_stack = Stack()
        funny_stack = Stack()

        little_stack.push(1)
        another_stack.push(little_stack.pop() + 1)
        funny_stack.push(another_stack.pop() - 2)

        print(funny_stack.pop())

        little_stack.show()
        another_stack.show()
        funny_stack.show()


    output:

        0
        []
        []
        []

41) Creating a subclass

        code:

            class Stack:
                def __init__(self):
                    self.__stack_list = []

                def push(self, val):
                    self.__stack_list.append(val)

                def pop(self):
                    val = self.__stack_list[-1]
                    del self.__stack_list[-1]
                    return val


            class AddingStack(Stack):
                def __init__(self):
                    Stack.__init__(self)        # This line ensures the parent class is properly initialized
                    self.__sum = 0

        Contrary to many other languages, Python forces you to explicitly invoke a superclass's constructor. 
        Omitting this point will have harmful effects - the object will be deprived of the __stack_list list. 
        Such a stack will not function properly.

        This is the only time you can invoke any of the available constructors explicitly - it can be done inside the subclass's constructor.

42) Adding 2 methods


        class Stack:
            def __init__(self):
                self.__stackList = []

            def push(self, val):
                self.__stackList.append(val)

            def pop(self):
                val = self.__stackList[-1]
                del self.__stackList[-1]
                return val
            
            def show(self):
                print(self.__stack_list)


        class AddingStack(Stack):
            def __init__(self):
                Stack.__init__(self)            # This line ensures the parent class is properly initialized
                self.__sum = 0

            def push(self, val):
                self.__sum += val
                Stack.push(self, val)

        
    The line Stack.push(self, val) ensures that the push method from the superclass Stack is invoked.
    This preserves the functionality of adding the value to the internal stack list (__stackList) in the superclass,
    while also allowing the subclass AddingStack to add its own additional functionality (such as updating the sum).
        
43) Getting and outputting the sum of the stack

        class Stack:
            def __init__(self):
                self.__stackList = []

            def push(self, val):
                self.__stackList.append(val)

            def pop(self):
                val = self.__stackList[-1]
                del self.__stackList[-1]
                return val
            
            def show(self):
                return self.__stackList


        class AddingStack(Stack):
            def __init__(self):
                Stack.__init__(self)
                self.__sum = 0

            def get_sum(self):
                return self.__sum

            def push(self, val):
                self.__sum += val
                Stack.push(self, val)

            def pop(self):
                val = Stack.pop(self)
                self.__sum -= val
                return val
            

        stack_object = AddingStack()

        for _ in range(5):
            stack_object.push(_)

        print(stack_object.show())
        print(stack_object.get_sum())

        for _ in range(5):
            stack_object.pop()

44) Project: Count the number of elements pushed on and popped from stack (Output 100, count only pop)

        code:

                class Stack:
                    def __init__(self):
                        self.__stk = []

                    def push(self, val):
                        self.__stk.append(val)

                    def pop(self):
                        val = self.__stk[-1]
                        del self.__stk[-1]
                        return val

                class CountingStack(Stack):
                    def __init__(self):
                        Stack.__init__(self)
                        self.__count = 0

                    def get_counter(self):
                        return self.__count

                    def pop(self):
                        self.__count += 1
                        return Stack.pop(self)
                
                stk = CountingStack()
                for i in range(100):
                    stk.push(i)
                    stk.pop()
                print(stk.get_counter())

        output:

            100

45) Project: Create a queue & add validation

        code:

            class QueueError(IndexError):
                pass

            class Queue:
                def __init__(self):
                    self.queue = []

                def put(self, elem):
                    self.queue.insert(0, elem)

                def get(self):
                    if len(self.queue) > 0:
                        val = self.queue[-1]
                        del self.queue[-1]
                        return val
                    else:
                        raise QueueError

            que = Queue()
            que.put(1)
            que.put("dog")
            que.put(False)

            try:
                for i in range(4):
                    print(que.get())
            except:
                print("Queue error")

46) Project: Call a list from the superclass in its subclass

        code:

            class QueueError(IndexError):
                pass

            class Queue:
                def __init__(self):
                    self.queue = []

                def put(self,elem):
                    self.queue.insert(0,elem)

                def get(self):
                    if len(self.queue) > 0:
                        elem = self.queue[-1]
                        del self.queue[-1]
                        return elem
                    else:
                        raise QueueError
                    
            class SuperQueue(Queue):
                def __init__(self):             # This and
                    Queue.__init__(self)        # this line isnt required

                def isempty(self):
                    return len(self.queue) == 0

            que = SuperQueue()
            que.put(1)
            que.put("dog")
            que.put(False)
            for i in range(4):
                if not que.isempty():
                    print(que.get())
                else:
                    print("Queue empty")


        The 2 lines mentioned are not really required since __init__ is automatically inherited from Queue
        This means that when an instance of SuperQueue is created, it will call the __init__ method from Queue,
          initializing self.queue as an empty list.

        Properties and Methods: SuperQueue inherits all the properties and methods of Queue, including put, get, and queue.

        No Need for Redefinition: Redefining the __init__ method in SuperQueue without adding any new functionality is redundant,
          as it simply calls the superclass's __init__ method.

47) Instance variables

        An instance variable is a variable accessible on an instance
            OR:
                An instance variable is a property whose existence depends on the creation of an object. 
                Every object can have a different set of instance variables
        "instance variable" is also known as an attribute
        An instance variable can be private when its name starts with __, but don't forget that such a property
          is still accessible from outside the class using a mangled name constructed as _ClassName__PrivatePropertyName.

        Class variables are shared among all instances of the class. They are defined within the class but outside any instance methods.
        Instance variables are unique to each instance and are typically defined within the __init__ method or elsewhere within the instance.

        The __dict__ attribute of an instance contains only the instance-specific attributes. It does not include class variables.




        code:

            class ExampleClass:
                def __init__(self, val = 1):
                    self.first = val

                def set_second(self, val):
                    self.second = val


            example_object_1 = ExampleClass()
            example_object_2 = ExampleClass(2)

            example_object_2.set_second(3)

            example_object_3 = ExampleClass(4)
            example_object_3.third = 5

            print(example_object_1.__dict__)
            print(example_object_2.__dict__)
            print(example_object_3.__dict__)

        output:

            {'first': 1}
            {'second': 3, 'first': 2}
            {'third': 5, 'first': 4}

        code:

            class Car:

                def __init__(self, make, model, colour):
                    self.make = make
                    self.model = model
                    self.colour = colour


            new_car = Car('Ford', 'Escape', 'Silver')

            print(new_car.__dict__)

        output:

            {'make': 'Ford', 'model': 'Escape', 'colour': 'Silver'}

48) Class variables
        A class variable is a property which exists in exactly one copy and is stored outside any object,
         and doesn't need any created object to be accessible. Such variables are not shown as __dict__ content.
        All a class's class variables are stored inside a dedicated dictionary named __dict__, contained in every class separately.
        
        Class variables are shared among all instances of the class. They are defined within the class but outside any instance methods.
        Instance variables are unique to each instance and are typically defined within the __init__ method or elsewhere within the instance.

        The __dict__ attribute of an instance contains only the instance-specific attributes. It does not include class variables.

        e.g:

            code:

                class ExampleClass:
                    counter = 0
                    def __init__(self, val = 1):
                        self.__first = val
                        ExampleClass.counter += 1


                example_object_1 = ExampleClass()
                example_object_2 = ExampleClass(2)
                example_object_3 = ExampleClass(4)

                print(example_object_1.__dict__, example_object_1.counter)
                print(example_object_2.__dict__, example_object_2.counter)
                print(example_object_3.__dict__, example_object_3.counter)

            output:

                {'_ExampleClass__first': 1} 3
                {'_ExampleClass__first': 2} 3
                {'_ExampleClass__first': 4} 3

        e.g:

            code:

                class ExampleClass:
                    varia = 1
                    def __init__(self, val):
                        ExampleClass.varia = val


                print(ExampleClass.__dict__)
                example_object = ExampleClass(2)

                print(ExampleClass.__dict__)
                print(example_object.__dict__)

            output:

                {'__module__': '__main__', 'varia': 1, '__init__': <function ExampleClass.__init__ at 0x0000028B72D58D60>, '__dict__': <attribute '__dict__' of 'ExampleClass' objects>, '__weakref__': <attribute '__weakref__' of 'ExampleClass' objects>, '__doc__': None}
                {'__module__': '__main__', 'varia': 2, '__init__': <function ExampleClass.__init__ at 0x0000028B72D58D60>, '__dict__': <attribute '__dict__' of 'ExampleClass' objects>, '__weakref__': <attribute '__weakref__' of 'ExampleClass' objects>, '__doc__': None}
                {}

49) Checking an attribute's (instance variable's) existence
        accessing a non-existing object (class) attribute causes an AttributeError exception
        The object created by the constructor can have only one of two possible attributes: a or b

        code:

            class ExampleClass:
                def __init__(self, val):
                    if val % 2 != 0:
                        self.a = 1
                    else:
                        self.b = 1


            example_object = ExampleClass(1)

            print(example_object.a)
            print(example_object.b)

        output:

            1
            Traceback (most recent call last):
            File ".main.py", line 11, in 
                print(example_object.b)
            AttributeError: 'ExampleClass' object has no attribute 'b'

50) hasattr
        checks if any object/class contains a specified property
        expects two arguments to be passed to it:
            the class or the object being checked;
            the name of the property whose existence has to be reported (has to be a string containing the attribute name)
        The function returns True or False
        
        code:

            class ExampleClass:
                def __init__(self, val):
                    if val % 2 != 0:
                        self.a = 1
                    else:
                        self.b = 1


            example_object = ExampleClass(2)
            print(example_object.a)

            if hasattr(example_object, 'b'):
                print(example_object.b)

        output:

            1

            
        the hasattr() function can operate on classes, too. You can use it to find out if a class variable is available
        code:

            class ExampleClass:
                attr = 1

            print(hasattr(ExampleClass, 'attr'))
            print(hasattr(ExampleClass, 'prop'))

        output:

            True
            False
        
        code:

            class ExampleClass:
                a = 1
                def __init__(self):
                    self.b = 2

            example_object = ExampleClass()

            print(hasattr(example_object, 'b'))
            print(hasattr(example_object, 'a'))
            print(hasattr(ExampleClass, 'b'))
            print(hasattr(ExampleClass, 'a'))

        output:

            True
            True
            False
            True

            
        final example:
        code:

            class Sample:
                gamma = 0 # Class variable.
                def __init__(self):
                    self.alpha = 1 # Instance variable.
                    self.__delta = 3 # Private instance variable.


            obj = Sample()
            obj.beta = 2  # Another instance variable (existing only inside the "obj" instance.)
            print(obj.__dict__)

        output:

            {'alpha': 1, '_Sample__delta': 3, 'beta': 2}

51) Methods (basics)
        a function declared/embedded inside the class and able to access all the class's components
        The first (or only) parameter of each method is usually named self, which is designed to identify the object for
          which the method is invoked in order to access the object's properties or invok
        it identifies the object for which the method is invoked.
        If you're going to invoke a method, you mustn't pass the argument for the self parameter - Python will set it for you
        e its methods

        code:

            class Classy:
                def method(self):
                    print("method")

            obj = Classy()
            obj.method()

        output:

            method

        Note the way we've created the object - we've treated the class name like a function, 
        returning a newly instantiated object of the class.

        If you want the method to accept parameters other than self, you should:
            place them after self in the method's definition;
            deliver them during invocation without specifying self (as previously)

        code:

            class Classy:
                def method(self, par):
                    print("method:", par)


            obj = Classy()
            obj.method(1)
            obj.method(2)
            obj.method(3)

        output:

            method: 1
            method: 2
            method: 3

        
        The self parameter is used to obtain access to the object's instance and class variables.

        code:

            class Classy:
                varia = 2
                def method(self):
                    print(self.varia, self.var)


            obj = Classy()
            obj.var = 3
            obj.method()

        output:

            2 3

        code:

            class Classy:
                def other(self):
                    print("other")

                def method(self):
                    print("method")
                    self.other()


            obj = Classy()
            obj.method()

        output:

            method
            other

        If you name a method like this: __init__, it won't be a regular method - it will be a constructor.
        
        The constructor:

            is obliged to have the self parameter (it's set automatically, as usual);
            may (but doesn't need to) have more parameters than just self; if this happens, 
                the way in which the class name is used to create the object must reflect the __init__ definition;
            can be used to set up the object, i.e., properly initialize its internal state,
                create instance variables, instantiate any other objects if their existence is needed, etc.
            if a class contains a constructor (a method named __init__) it cannot return any value and cannot be invoked directly.
            
        code:

            class Classy:
                def __init__(self, value):
                    self.var = value


            obj_1 = Classy("object")

            print(obj_1.var)

        output:

            object

        Note that the constructor:

            cannot return a value, as it is designed to return a newly created object and nothing else;
        
            cannot be invoked directly either from the object or from inside the class
                (you can invoke a constructor from any of the object's subclasses, but we'll discuss this issue later.)

        code:

            class Classy:
                def __init__(self, value = None):
                    self.var = value

            obj_1 = Classy("object")
            obj_2 = Classy()

            print(obj_1.var)
            print(obj_2.var)

        output:

            object
            None

52) Mangling in methods
        property name mangling applies to method names, too - a method whose name starts with __ is (partially) hidden

        code:

            class Classy:
                def visible(self):
                    print("visible")
                def __hidden(self):
                    print("hidden")

            obj = Classy()
            obj.visible()

            try:
                obj.__hidden()
            except:
                print("failed")

            obj._Classy__hidden()

        output:

            visible
            failed
            hidden

        code:

            class Classy:
                varia = 1
                def __init__(self):
                    self.var = 2
                def method(self):
                    pass
                def __hidden(self):
                    pass

            obj = Classy()
            print(obj.__dict__)
            print(Classy.__dict__)

        output:

            {'var': 2}
            {'__module__': '__main__', 'varia': 1, '__init__': <function Classy.__init__ at 0x00000135C8678CC0>, 
            'method': <function Classy.method at 0x00000135C8678D60>, '_Classy__hidden': <function Classy.__hidden at 0x00000135C86FA660>,
            '__dict__': <attribute '__dict__' of 'Classy' objects>, '__weakref__': <attribute '__weakref__' of 'Classy' objects>,
            '__doc__': None}

53) __name__
        a built in property that contains the name of the class
        note: the __name__ attribute is absent from the object - it exists only inside classes.

        code:

            class Classy:
                pass
            print(Classy.__name__)

        output:

            Classy

        note: print(obj.__name__) will cause an error

54) type()
        to find the class of a particular object
        
        code:

            class Classy:
                pass
            obj = Classy()
            print(type(obj).__name__)

        output:

            Classy
    
55) __module__
        it stores the name of the module which contains the definition of the class
        any module named __main__ is actually not a module, but the file currently being run

        code:

            class Classy:
                pass
            print(Classy.__module__)
            obj = Classy()
            print(obj.__module__)

        output:

            __main__
            __main__

56) __bases__
        a tuple containing a class's superclasses
        a tuple that contains classes (not class names) which are direct superclasses for the class
        only classes have this attribute - objects don't
        a class without explicit superclasses points to object (a predefined Python class) as its direct ancestor

        code:
        
            class SuperOne:
                pass


            class SuperTwo:
                pass


            class Sub(SuperOne, SuperTwo):
                pass


            def printBases(cls):
                print('( ', end='')

                for x in cls.__bases__:
                    print(x.__name__, end=' ')

                print(')')

            printBases(SuperOne)
            printBases(SuperTwo)
            printBases(Sub)

        output:

            ( object )
            ( object )
            ( SuperOne SuperTwo )

57) Reflection and introspection
        1) introspection 
            → the ability of a program to examine the type or properties of an object at runtime
        2) reflection
            → which goes a step further, and is the ability of a program to manipulate the values,
               properties and/or functions of an object at runtime.

58) keys()
        a method used with dictionaries to return a view object that displays a list of all the keys in the dictionary
        this view object can be iterated over to access each key individually

59) items()
        this method returns a view object that displays a list of the dictionary’s key-value tuple pairs

        code:

            my_dict = {"name": "Alice", "age": 30, "city": "New York"}

            items_view = my_dict.items()
            print(items_view)

            my_dict["country"] = "USA"
            print(items_view)

            for key, value in items_view:
                print(f"Key: {key}, Value: {value}")
        
        output:

            dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])
            dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York'), ('country', 'USA')])
            Key: name, Value: Alice
            Key: age, Value: 30
            Key: city, Value: New York
            Key: country, Value: USA

60) getattr
        get attribute
        this function is used to retrieve the value of an attribute of an object
        to access an attribute dynamically by name, 
         which is useful when the attribute name is stored in a variable or constructed at runtime

        code:

            class MyClass:
                def __init__(self):
                    self.attribute = "value"

            obj = MyClass()

            # Using getattr to access the 'attribute'
            attr_value = getattr(obj, 'attribute')
            print(attr_value)  # Output: value

            # Using getattr with a non-existent attribute and a default value
            non_existent_attr = getattr(obj, 'non_existent', 'default_value')
            print(non_existent_attr)  # Output: default_value

        output:
        
            value
            default_value

61) setattr
        set attribute
        to set the value of an attribute of an object, dynamically by name

        code:

            class MyClass:
                def __init__(self):
                    self.attribute = "initial value"

            obj = MyClass()

            # Using setattr to set the value of 'attribute'
            setattr(obj, 'attribute', 'new value')
            print(obj.attribute)  # Output: new value

            # Using setattr to create a new attribute
            setattr(obj, 'new_attribute', 'new attribute value')
            print(obj.new_attribute)  # Output: new attribute value

        output:

            new value
            new attribute value

62) isinstance()
        function is used to check if an object is an instance or subclass of a class or a tuple of classe
        returns True if the object is an instance or subclass of the class (or any of the classes in the tuple), and False otherwise
        syntax
            isinstance(object, classinfo)
        
        code:

            # Check if 5 is an instance of int
            print(isinstance(5, int))  # Output: True

            # Check if 'hello' is an instance of str
            print(isinstance('hello', str))  # Output: True

            # Check if 5.0 is an instance of int or float
            print(isinstance(5.0, (int, float)))  # Output: True

            # Custom class example
            class MyClass:
                pass

            obj = MyClass()

            # Check if obj is an instance of MyClass
            print(isinstance(obj, MyClass))  # Output: True

        output:

            True
            True
            True
            True

63) Investigating classes

    code

        class MyClass:
            pass


        obj = MyClass()
        obj.a = 1
        obj.b = 2
        obj.i = 3
        obj.ireal = 3.5
        obj.integer = 4
        obj.z = 5


        def incIntsI(obj):
            for name in obj.__dict__.keys():
                if name.startswith('i'):
                    val = getattr(obj, name)
                    if isinstance(val, int):
                        setattr(obj, name, val + 1)


        print(obj.__dict__)
        incIntsI(obj)
        print(obj.__dict__)

    output:

        {'a': 1, 'integer': 4, 'b': 2, 'i': 3, 'z': 5, 'ireal': 3.5}
        {'a': 1, 'integer': 5, 'b': 2, 'i': 4, 'z': 5, 'ireal': 3.5}

64) examples of predefined properties used in sample programs

        code:

            class Sample:
                def __init__(self):
                    self.name = Sample.__name__
                def myself(self):
                    print("My name is " + self.name + " living in a " + Sample.__module__)


            obj = Sample()
            obj.myself()

        output:

            My name is Sample living in a __main__

        Exercise 1

            The declaration of the Snake class is given below. Enrich the class with a method named increment(),
                adding 1 to the victims property.

            class Snake:
                def __init__(self):
                    self.victims = 0

        Solution 1

            class Snake:
            def __init__(self):
                self.victims = 0

            def increment(self):
                self.victims += 1

        Exercise 2

            Redefine the Snake class constructor so that is has a parameter to initialize the victims field with a value passed to the object during construction.

        Solution 2

            class Snake:
                def __init__(self, victims):
                self.victims = victims

        Exercise 3

            Can you predict the output of the following code?

            class Snake:
                pass

            class Python(Snake):
                pass

            print(Python.__name__, 'is a', Snake.__name__)
            print(Python.__bases__[0].__name__, 'can be a', Python.__name__)

        Solution 3

            Python is a Snake
            Snake can be a Python

65) Project: The timer class

        my code:
    
            class Timer:
                def __init__(self, hours = 0, mins = 0, secs = 0):
                    self.__seconds = (hours * 3600) + (mins * 60) + secs

                def __str__(self):
                    h = self.__seconds // 3600
                    m = (self.__seconds % 3600) // 60
                    s = (self.__seconds % 3600) % 60
                    return f"{h:02}:{m:02}:{s:02}"

                def next_second(self):
                    self.__seconds += 1
                    if self.__seconds == 86400: self.__seconds = 0

                def prev_second(self):
                    self.__seconds -= 1
                    if self.__seconds == -1: self.__seconds += 86400

            timer = Timer(23, 59, 59)
            print(timer)
            timer.next_second()
            print(timer)
            timer.prev_second()
            print(timer)

        their code:

            def two_digits(val):
                s = str(val)
                if len(s) == 1:
                    s = '0' + s
                return s


            class Timer:
                def __init__(self, hours=0, minutes=0, seconds=0):
                    self.__hours = hours
                    self.__minutes = minutes
                    self.__seconds = seconds

                def __str__(self):
                    return two_digits(self.__hours) + ":" + \
                        two_digits(self.__minutes) + ":" + \
                        two_digits(self.__seconds)

                def next_second(self):
                    self.__seconds += 1
                    if self.__seconds > 59:
                        self.__seconds = 0
                        self.__minutes += 1
                        if self.__minutes > 59:
                            self.__minutes = 0
                            self.__hours += 1
                            if self.__hours > 23:
                                self.__hours = 0

                def prev_second(self):
                    self.__seconds -= 1
                    if self.__seconds < 0:
                        self.__seconds = 59
                        self.__minutes -= 1
                        if self.__minutes < 0:
                            self.__minutes = 59
                            self.__hours -= 1
                            if self.__hours < 0:
                                self.__hours = 23


            timer = Timer(23, 59, 59)
            print(timer)
            timer.next_second()
            print(timer)
            timer.prev_second()
            print(timer)

66) Project: Days of the week

        my code:

            class WeekDayError(Exception):
                pass	

            class Weeker:
                def __init__(self, day):
                    self.__week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
                    if day not in self.__week: raise WeekDayError
                    self.__org_index = self.__week.index(day)
                    self.__dif = 0
                    
                def __str__(self):
                    self.__new_index = (self.__org_index + self.__dif) % 7
                    return self.__week[self.__new_index]

                def add_days(self, n):
                    self.__dif += n

                def subtract_days(self, n):
                    self.__dif -= n

            try:
                weekday = Weeker('Mon')
                print(weekday)
                weekday.add_days(15)
                print(weekday)
                weekday.subtract_days(23)
                print(weekday)
                weekday = Weeker('Monday')
            except WeekDayError:
                print("Sorry, I can't serve your request.")

        their code:

            class WeekDayError(Exception):
                pass

            class Weeker:
                __names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

                def __init__(self, day):
                    try:
                        self.__current = Weeker.__names.index(day)
                    except ValueError:
                        raise WeekDayError

                def __str__(self):
                    return Weeker.__names[self.__current]

                def add_days(self, n):
                    self.__current = (self.__current + n) % 7

                def subtract_days(self, n):
                    self.__current = (self.__current - n) % 7

            try:
                weekday = Weeker('Mon')
                print(weekday)
                weekday.add_days(15)
                print(weekday)
                weekday.subtract_days(23)
                print(weekday)
                weekday = Weeker('Monday')
            except WeekDayError:
                print("Sorry, I can't serve your request.")

67) Project: Points on a plane

        my code:

            import math

            class Point:
                def __init__(self, x = 0.0, y = 0.0):
                    self.__firstx = x
                    self.__firsty = y
                    
                def getx(self):
                    return abs(self.__firstx - self.__secondx)
                
                def gety(self):
                    return abs(self.__firsty - self.__secondy)
                
                def distance_from_xy(self, x, y):
                    self.__secondx = x
                    self.__secondy = y
                    distance = math.hypot(self.getx(), self.gety())
                    return distance

                def distance_from_point(self, point):
                    self.__secondx = point.__firstx
                    self.__secondy = point.__firsty
                    distance = math.hypot(self.getx(), self.gety())
                    return distance

            point1 = Point(0, 0)
            point2 = Point(1, 1)
            print(point1.distance_from_point(point2))
            print(point2.distance_from_xy(2, 0))

        their code:

            import math

            class Point:
                def __init__(self, x=0.0, y=0.0):
                    self.__x = x
                    self.__y = y

                def getx(self):
                    return self.__x

                def gety(self):
                    return self.__y

                def distance_from_xy(self, x, y):
                    return math.hypot(abs(self.__x - x), abs(self.__y - y))

                def distance_from_point(self, point):
                    return self.distance_from_xy(point.getx(), point.gety())

            point1 = Point(0, 0)
            point2 = Point(1, 1)
            print(point1.distance_from_point(point2))
            print(point2.distance_from_xy(2, 0))

68) Project: Triangle

        my code:

            import math

            class Point:
                def __init__(self, x = 0.0, y = 0.0):
                    self.__firstx = x
                    self.__firsty = y

                def getx(self):
                    return abs(self.__firstx - self.__secondx)

                def gety(self):
                    return abs(self.__firsty - self.__secondy)

                def distance_from_point(self, point):
                    self.__secondx = point.__firstx
                    self.__secondy = point.__firsty
                    distance = math.hypot(self.getx(), self.gety())
                    return distance
                
            class Triangle:
                def __init__(self, vertice1, vertice2, vertice3):
                    self.__first, self.__second, self.__third, = vertice1, vertice2, vertice3

                def perimeter(self):
                    distance1 = Point.distance_from_point(self.__first, self.__second)
                    distance2 = Point.distance_from_point(self.__second, self.__third)
                    distance3 = Point.distance_from_point(self.__first, self.__third)
                    return distance1 + distance2 + distance3

            triangle = Triangle(Point(4, 5), Point(1, 2), Point(5, 7))
            print(triangle.perimeter())

        gpt code:

            import math

            class Point:
                def __init__(self, x=0.0, y=0.0):
                    self.__x = x
                    self.__y = y

                def distance_from_point(self, point):
                    return math.hypot(self.__x - point.__x, self.__y - point.__y)

            class Triangle:
                def __init__(self, vertice1, vertice2, vertice3):
                    self.__vertice1 = vertice1
                    self.__vertice2 = vertice2
                    self.__vertice3 = vertice3

                def perimeter(self):
                    side1 = self.__vertice1.distance_from_point(self.__vertice2)
                    side2 = self.__vertice2.distance_from_point(self.__vertice3)
                    side3 = self.__vertice3.distance_from_point(self.__vertice1)
                    return side1 + side2 + side3

            # Example usage:
            triangle = Triangle(Point(9, 0), Point(3, 1), Point(0, 1))
            print(triangle.perimeter())  # Output should be the perimeter of the triangle

        their code:

            import math

            class Point:
                def __init__(self, x=0.0, y=0.0):
                    self.__x = x
                    self.__y = y

                def getx(self):
                    return self.__x

                def gety(self):
                    return self.__y

                def distance_from_xy(self, x, y):
                    return math.hypot(abs(self.__x - x), abs(self.__y - y))

                def distance_from_point(self, point):
                    return self.distance_from_xy(point.getx(), point.gety())

            class Triangle:
                def __init__(self, vertice1, vertice2, vertice3):
                    self.__vertices = [vertice1, vertice2, vertice3]

                def perimeter(self):
                    per = 0
                    for i in range(3):
                        per += self.__vertices[i].distance_from_point(self.__vertices[(i + 1) % 3])
                    return per

            triangle = Triangle(Point(4, 5), Point(1, 2), Point(5, 7))
            print(triangle.perimeter())

69) __str__()
        a method defined in a class to control how an instance of that class is converted to a string and printed in a human-readable way
        e.g:

            class Star:
                def __init__(self, name, galaxy):
                    self.name = name
                    self.galaxy = galaxy

                def __str__(self):
                    return self.name + ' in ' + self.galaxy


            sun = Star("Sun", "Milky Way")
            print(sun)

        output:

            Sun in Milky Way

70) Inheritance
        passing attributes and methods from the superclass (defined and existing) to a newly created class, called the subclass
        a way of building a new class, not from scratch, but by using an already defined repertoire of traits

71) issubclass()
        issubclass(ClassOne, ClassTwo)
        The function returns True if ClassOne is a subclass of ClassTwo, and False otherwise
        e.g:

            class Vehicle:
                pass

            class LandVehicle(Vehicle):
                pass

            class TrackedVehicle(LandVehicle):
                pass

            for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
                for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
                    print(issubclass(cls1, cls2), end="\t")
                print()

        output:

            True	False	False	
            True	True	False	
            True	True	True

        more like:

            ↓ is a subclass of →	Vehicle	    LandVehicle	    TrackedVehicle
            Vehicle	                True	    False	        False
            LandVehicle	            True	    True	        False
            TrackedVehicle	        True	    True	        True

73) isinstance()
        isinstance(objectName, ClassName)
        The functions returns True if the object is an instance of the class, or False otherwise.
        e.g:

            class Vehicle:
                pass

            class LandVehicle(Vehicle):
                pass

            class TrackedVehicle(LandVehicle):
                pass

            my_vehicle = Vehicle()
            my_land_vehicle = LandVehicle()
            my_tracked_vehicle = TrackedVehicle()

            for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
                for cls in [Vehicle, LandVehicle, TrackedVehicle]:
                    print(isinstance(obj, cls), end="\t")
                print()

        output:

            True	False	False	
            True	True	False	
            True	True	True	

        more like:

            ↓ is an instance of →	Vehicle	    LandVehicle	    TrackedVehicle
            my_vehicle	            True	    False	        False
            my_land_vehicle	        True	    True	        False
            my_tracked_vehicle	    True	    True	        True
            
74) is
        The is operator checks whether two variables (object_one and object_two here) refer to the same object
        e.g:

            class SampleClass:
                def __init__(self, val):
                    self.val = val


            object_1 = SampleClass(0)
            object_2 = SampleClass(2)
            object_3 = object_1
            object_3.val += 1

            print(object_1 is object_2)
            print(object_2 is object_3)
            print(object_3 is object_1)
            print(object_1.val, object_2.val, object_3.val)

            string_1 = "Mary had a little "
            string_2 = "Mary had a little lamb"
            string_1 += "lamb"

            print(string_1 == string_2, string_1 is string_2)

        output:

            False
            False
            True
            1 2 1
            True False
            
        The results prove that object_1 and object_3 are actually the same objects, while string_1 and string_2 aren't,
          despite their contents being the same
          
75) Inhertiting methods
        As there is no __str__() method within the Sub class, the printed string is to be produced within the Super class.
          This means that the __str__() method has been inherited by the Sub class.

        code:

            class Super:
                def __init__(self, name):
                    self.name = name

                def __str__(self):
                    return "My name is " + self.name + "."

            class Sub(Super):
                def __init__(self, name):
                    Super.__init__(self, name)

            obj = Sub("Andy")

            print(obj)

        output:

            My name is Andy.

76) super()
        This function accesses the superclass without needing to know its name        
        The super() function creates a context in which you don't have to (moreover, you mustn't) pass the self argument
         to the method being invoked - this is why it's possible to activate the superclass constructor using only one argument

        Note: you can use this mechanism not only to invoke the superclass constructor,
         but also to get access to any of the resources available inside the superclass

        code:

            class Super:
                def __init__(self, name):
                    self.name = name

                def __str__(self):
                    return "My name is " + self.name + "."


            class Sub(Super):
                def __init__(self, name):
                    super().__init__(name)


            obj = Sub("Andy")

            print(obj)
            
77) Testing properties: class variables & instance variables
    
        code:
            
            # Testing properties: class variables
            class Super:
                supVar = 1

            class Sub(Super):
                subVar = 2

            obj = Sub()

            print(obj.subVar)
            print(obj.supVar)

        output:

            2
            1

        code:

            # Testing properties: instance variables
            class Super:
                def __init__(self):
                    self.supVar = 11


            class Sub(Super):
                def __init__(self):
                    super().__init__()
                    self.subVar = 12


            obj = Sub()

            print(obj.subVar)
            print(obj.supVar)

        output:

            12
            11

        Note: the existence of the supVar variable is obviously conditioned by the Super class constructor invocation.
                Omitting it would result in the absence of the variable in the created object (try it yourself).


        code:

            class Level1:
                variable_1 = 100
                def __init__(self):
                    self.var_1 = 101

                def fun_1(self):
                    return 102


            class Level2(Level1):
                variable_2 = 200
                def __init__(self):
                    super().__init__()
                    self.var_2 = 201
                
                def fun_2(self):
                    return 202


            class Level3(Level2):
                variable_3 = 300
                def __init__(self):
                    super().__init__()
                    self.var_3 = 301

                def fun_3(self):
                    return 302


            obj = Level3()

            print(obj.variable_1, obj.var_1, obj.fun_1())
            print(obj.variable_2, obj.var_2, obj.fun_2())
            print(obj.variable_3, obj.var_3, obj.fun_3())

        output:

            100 101 102
            200 201 202        
            300 301 302
               
78) Multiple inheritance
        Multiple inheritance occurs when a class has more than one superclass.
        Syntactically,such inheritance is presented as a comma-separated list of superclasses put inside parentheses after
          the new class name - just like here:

                class SuperA:
                    var_a = 10
                    def fun_a(self):
                        return 11


                class SuperB:
                    var_b = 20
                    def fun_b(self):
                        return 21


                class Sub(SuperA, SuperB):
                    pass


                obj = Sub()

                print(obj.var_a, obj.fun_a())
                print(obj.var_b, obj.fun_b())

            The Sub class has two superclasses: SuperA and SuperB.
            This means that the Sub class inherits all the goods offered by both SuperA and SuperB.

            The code prints:

                10 11
                20 21
                
79) Overriding
        The entity defined later (in the inheritance sense) overrides the same entity defined earlier
        Python looks for an entity from bottom to top
        code:
        
            class Level1:
                var = 100
                def fun(self):
                    return 101


            class Level2(Level1):
                var = 200
                def fun(self):
                    return 201


            class Level3(Level2):
                pass


            obj = Level3()

            print(obj.var, obj.fun())

        output:

            200 201

            
        code:

            class Left:
                var = "L"
                var_left = "LL"
                def fun(self):
                    return "Left"

            class Right:
                var = "R"
                var_right = "RR"
                def fun(self):
                    return "Right"

            class Sub(Left, Right):
                pass

            obj = Sub()

            print(obj.var, obj.var_left, obj.var_right, obj.fun())

        output:

            L LL RR Left
            
        When obj.var is accessed, Python first looks in the Sub class,
          then in the Left class (because it's the first in the MRO after Sub), and finds var = "L".
        When obj.var_left is accessed, it follows the same MRO and finds var_left = "LL" in the Left class.
        When obj.var_right is accessed, it follows the MRO and finds var_right = "RR" in the Right class.
        When obj.fun() is called, it follows the MRO and finds the fun method in the Left class and returns "Left".

        the methods are not being overwritten, but instance variables

        Methods are not being overwritten because the method resolution order (MRO) dictates which method is found and called first.
        Instance variables (attributes) are found based on the MRO, so if an attribute is not found in the first class in the MRO,
          Python continues to the next class.
        Thus, attributes like var, var_left, and var_right are accessed based on their presence in the classes according to the MRO, 
          while methods are resolved in a similar manner but are not overwritten unless explicitly done so in a subclass.

80) How to build a hierarchy of classes
        code:

            class One:
                def do_it(self):
                    print("do_it from One")

                def doanything(self):
                    self.do_it()

            class Two(One):
                def do_it(self):
                    print("do_it from Two")

            one = One()
            two = Two()

            one.doanything()
            two.doanything()

        output:

            do_it from One
            do_it from Two
        
        The first invocation seems to be simple, and it is simple,
          actually - invoking doanything() from the object named one will obviously activate the first of the methods.

        The second invocation needs some attention. It's simple, too if you keep in mind how Python finds class components.
        The second invocation will launch do_it() in the form existing inside the Two class,
          regardless of the fact that the invocation takes place within the One class.

81) Abstract methods
        an empty method, as it only demonstrates some possibility which will be instantiated later

82) Inheritance: Vehicles example using inheritance
        code:

            import time

            class Vehicle:
                def change_direction(left, on):
                    pass

                def turn(left):
                    change_direction(left, True)
                    time.sleep(0.25)
                    change_direction(left, False)


            class TrackedVehicle(Vehicle):
                def control_track(left, stop):
                    pass

                def change_direction(left, on):
                    control_track(left, on)


            class WheeledVehicle(Vehicle):
                def turn_front_wheels(left, on):
                    pass

                def change_direction(left, on):
                    turn_front_wheels(left, on)

                    
        The most important advantage (omitting readability issues) is that this form of code enables you to implement a brand new turning
          algorithm just by modifying the turn() method, which can be done in just one place, as all the vehicles will obey it.

        This is how polymorphism helps the developer to keep the code clean and consistent.

83) Composition
        process of composing an object using other different objects

        inheritance extends a class's capabilities by adding new components and modifying existing ones;
          in other words, the complete recipe is contained inside the class itself and all its ancestors;
          the object takes all the class's belongings and makes use of them

        composition projects a class as a container able to store and use other objects (derived from other classes)
          where each of the objects implements a part of a desired class's behavior.

84) Inheritance: Vehicles example using composition
        code:

            import time

            class Tracks:
                def change_direction(self, left, on):
                    print("tracks: ", left, on)

            class Wheels:
                def change_direction(self, left, on):
                    print("wheels: ", left, on)

            class Vehicle:
                def __init__(self, controller):
                    self.controller = controller

                def turn(self, left):
                    self.controller.change_direction(left, True)
                    time.sleep(0.25)
                    self.controller.change_direction(left, False)

            wheeled = Vehicle(Wheels())
            tracked = Vehicle(Tracks())

            wheeled.turn(True)
            tracked.turn(False)

        output:

            wheels:  True True
            wheels:  True False
            tracks:  False True
            tracks:  False False
        
        Classes Defined
    
            Tracks Class:
                Defines a Tracks class with a method change_direction(self, left, on) that prints the direction change for tracks.
        
            Wheels Class:
                Defines a Wheels class with a method change_direction(self, left, on) that prints the direction change for wheels.
            
            Vehicle Class:
                Defines a Vehicle class with an __init__ method that initializes with a controller object (either Wheels or Tracks).
                Contains a turn(self, left) method that simulates the vehicle turning left or right:
                    Calls self.controller.change_direction(left, True) to initiate the turn.
                    Pauses execution for 0.25 seconds (time.sleep(0.25)) to simulate the turn.
                    Calls self.controller.change_direction(left, False) to end the turn.

        Initialization and Usage
            Creates instances of Vehicle named wheeled (with Wheels controller) and tracked (with Tracks controller).
            Calls the turn(True) method on the wheeled instance to simulate turning left using wheels.

        Output Explanation
            When wheeled.turn(True) is called:
            It first calls Wheels.change_direction(True, True) to simulate turning left.
            Pauses for 0.25 seconds.
            Then calls Wheels.change_direction(True, False) to stop the turn.

85) What is Method Resolution Order (MRO) and why is it that not all inheritances make sense?
        code:

            class Top:
                def m_top(self):
                    print("top")


            class Middle(Top):
                def m_middle(self):
                    print("middle")


            class Bottom(Middle):
                def m_bottom(self):
                    print("bottom")


            object = Bottom()
            object.m_bottom()
            object.m_middle()
            object.m_top()

        output:

            bottom
            middle
            top

        code:

            class Top:
                def m_top(self):
                    print("top")


            class Middle(Top):
                def m_middle(self):
                    print("middle")


            class Bottom(Middle, Top):
                def m_bottom(self):
                    print("bottom")


            object = Bottom()
            object.m_bottom()
            object.m_middle()
            object.m_top()

        output:

            bottom
            middle
            top

        code:

            class Top:
                def m_top(self):
                    print("top")


            class Middle(Top):
                def m_middle(self):
                    print("middle")


            class Bottom(Top, Middle):
                def m_bottom(self):
                    print("bottom")


            object = Bottom()
            object.m_bottom()
            object.m_middle()
            object.m_top()

        output:

            TypeError: Cannot create a consistent method resolution order (MRO) for bases Top, Middle

        To anticipate your question, we’ll say that this amendment has spoiled the code, and it won't run anymore. What a pity.
          The order we tried to force (Top, Middle) is incompatible with the inheritance path which is derived from the code's structure.
          Python won't like it.

        We think that the message speaks for itself. Python's MRO cannot be bent or violated, not just because that's the way Python works,
          but also because it's a rule you have to obey.

86) The diamond problem
        code:

            class Top:
                def m_top(self):
                    print("top")


            class Middle_Left(Top):
                def m_middle(self):
                    print("middle_left")


            class Middle_Right(Top):
                def m_middle(self):
                    print("middle_right")


            class Bottom(Middle_Left, Middle_Right):          #class Bottom(Middle_Right, Middle_Left):          gives the same output
                def m_bottom(self):
                    print("bottom")


            object = Bottom()
            object.m_bottom()
            object.m_middle()
            object.m_top()

        output:

            bottom
            middle_left
            top

        The invocation will activate the m_middle() method, which comes from the Middle_Left class
        The explanation is simple: the class is listed before Middle_Right on the Bottom class's inheritance list

87) else (try except)

        code:

            def reciprocal(n):
                try:
                    n = 1 / n
                except ZeroDivisionError:
                    print("Division failed")
                    return None
                else:
                    print("Everything went fine")
                    return n

            print(reciprocal(2))
            print(reciprocal(0))

        output:

            Everything went fine
            It's time to say good bye
            0.5
            Division failed

88) finally (try except)

        code:

            def reciprocal(n):
                try:
                    n = 1 / n
                except ZeroDivisionError:
                    print("Division failed")
                    n = None
                else:
                    print("Everything went fine")
                finally:
                    print("It's time to say goodbye")
                    return n


            print(reciprocal(2))
            print(reciprocal(0))

        output:

            Everything went fine
            It's time to say good bye
            0.5
            Division failed
            It's time to say good bye
            None

89) Exceptions are classes

        code:

            try:
                i = int("Hello!")
            except Exception as e:
                print(e)
                print(e.__str__())
                print(type(e))
                print(type(e.__str__()))


        output:

            invalid literal for int() with base 10: 'Hello!'
            invalid literal for int() with base 10: 'Hello!'
            <class 'ValueError'>
            <class 'str'>

        Note: the identifier's scope covers its except branch, and doesn't go any further

90) The exception tree

        code:

            def print_exception_tree(thisclass, nest = 0):
                if nest > 1:
                    print("   |" * (nest - 1), end="")
                if nest > 0:
                    print("   +---", end="")

                print(thisclass.__name__)

                for subclass in thisclass.__subclasses__():
                    print_exception_tree(subclass, nest + 1)


            print_exception_tree(BaseException)

        output:

            BaseException
                +---Exception
                |   +---TypeError
                |   +---StopAsyncIteration
                |   +---StopIteration
                |   +---ImportError
                |   |   +---ModuleNotFoundError
                |   |   +---ZipImportError
                |   +---OSError
                |   |   +---ConnectionError
                |   |   |   +---BrokenPipeError
                |   |   |   +---ConnectionAbortedError
                |   |   |   +---ConnectionRefusedError
                |   |   |   +---ConnectionResetError
                |   |   +---BlockingIOError
                |   |   +---ChildProcessError
                |   |   +---FileExistsError
                |   |   +---FileNotFoundError
                |   |   +---IsADirectoryError
                |   |   +---NotADirectoryError
                |   |   +---InterruptedError
                |   |   +---PermissionError
                |   |   +---ProcessLookupError
                |   |   +---TimeoutError
                |   |   +---UnsupportedOperation
                |   |   +---herror
                |   |   +---gaierror
                |   |   +---timeout
                |   |   +---Error
                |   |   |   +---SameFileError
                |   |   +---SpecialFileError
                |   |   +---ExecError
                |   |   +---ReadError
                |   +---EOFError
                |   +---RuntimeError
                |   |   +---RecursionError
                |   |   +---NotImplementedError
                |   |   +---_DeadlockError
                |   |   +---BrokenBarrierError
                |   +---NameError
                |   |   +---UnboundLocalError
                |   +---AttributeError
                |   +---SyntaxError
                |   |   +---IndentationError
                |   |   |   +---TabError
                |   +---LookupError
                |   |   +---IndexError
                |   |   +---KeyError
                |   |   +---CodecRegistryError
                |   +---ValueError
                |   |   +---UnicodeError
                |   |   |   +---UnicodeEncodeError
                |   |   |   +---UnicodeDecodeError
                |   |   |   +---UnicodeTranslateError
                |   |   +---UnsupportedOperation
                |   +---AssertionError
                |   +---ArithmeticError
                |   |   +---FloatingPointError
                |   |   +---OverflowError
                |   |   +---ZeroDivisionError
                |   +---SystemError
                |   |   +---CodecRegistryError
                |   +---ReferenceError
                |   +---BufferError
                |   +---MemoryError
                |   +---Warning
                |   |   +---UserWarning
                |   |   +---DeprecationWarning
                |   |   +---PendingDeprecationWarning
                |   |   +---SyntaxWarning
                |   |   +---RuntimeWarning
                |   |   +---FutureWarning
                |   |   +---ImportWarning
                |   |   +---UnicodeWarning
                |   |   +---BytesWarning
                |   |   +---ResourceWarning
                |   +---error
                |   +---Verbose
                |   +---Error
                |   +---TokenError
                |   +---StopTokenizing
                |   +---Empty
                |   +---Full
                |   +---_OptionError
                |   +---TclError
                |   +---SubprocessError
                |   |   +---CalledProcessError
                |   |   +---TimeoutExpired
                |   +---Error
                |   |   +---NoSectionError
                |   |   +---DuplicateSectionError
                |   |   +---DuplicateOptionError
                |   |   +---NoOptionError
                |   |   +---InterpolationError
                |   |   |   +---InterpolationMissingOptionError
                |   |   |   +---InterpolationSyntaxError
                |   |   |   +---InterpolationDepthError
                |   |   +---ParsingError
                |   |   |   +---MissingSectionHeaderError
                |   +---InvalidConfigType
                |   +---InvalidConfigSet
                |   +---InvalidFgBg
                |   +---InvalidTheme
                |   +---EndOfBlock
                |   +---BdbQuit
                |   +---error
                |   +---_Stop
                |   +---PickleError
                |   |   +---PicklingError
                |   |   +---UnpicklingError
                |   +---_GiveupOnSendfile
                |   +---error
                |   +---LZMAError
                |   +---RegistryError
                |   +---ErrorDuringImport
                +---GeneratorExit
                +---SystemExit
                +---KeyboardInterrupt

                
        - a tree is a perfect example of a recursive data structure
        - the root of Python's exception classes is the BaseException class (it's a superclass of all other exceptions)
        - print its name, taken from the __name__ property;
        - iterate through the list of subclasses delivered by the __subclasses__() method,
            and recursively invoke the print_exception_tree() function, incrementing the nesting level respectively

91) Detailed anatomy of exceptions
        The BaseException class introduces a property named args
        a tuple designed to gather all arguments passed to the class constructor
        we don't count the self argument here

        code:

            def print_args(args):
                lng = len(args)
                if lng == 0:
                    print("")
                elif lng == 1:
                    print(args[0])
                else:
                    print(str(args))


            try:
                raise Exception
            except Exception as e:
                print(e, e.__str__(), sep=' : ' ,end=' : ')
                print_args(e.args)

            try:
                raise Exception("my exception")
            except Exception as e:
                print(e, e.__str__(), sep=' : ', end=' : ')
                print_args(e.args)

            try:
                raise Exception("my", "exception")
            except Exception as e:
                print(e, e.__str__(), sep=' : ', end=' : ')
                print_args(e.args)

        output:

             :  :
            my exception : my exception : my exception
            ('my', 'exception') : ('my', 'exception') : ('my', 'exception')

92) How to create your own exception

        code:

            class MyZeroDivisionError(ZeroDivisionError):	
                pass

            def do_the_division(mine):
                if mine:
                    raise MyZeroDivisionError("1")
                else:		
                    raise ZeroDivisionError("2")

            for mode in [False, True]:
                try:
                    do_the_division(mode)
                except ZeroDivisionError:
                    print('3')

            for mode in [False, True]:
                try:
                    do_the_division(mode)
                except MyZeroDivisionError:
                    print('4')
                except ZeroDivisionError:
                    print('5')

        output:

            3
            3
            5
            4

        We've defined our own exception, named MyZeroDivisionError, derived from the built-in ZeroDivisionError. 
          As you can see, we've decided not to add any new components to the class.

        In effect, an exception of this class can be - depending on the desired point of view
        - treated like a plain ZeroDivisionError, or considered separately.

        The do_the_division() function raises either a MyZeroDivisionError or ZeroDivisionError exception,
          depending on the argument's value.

        The function is invoked four times in total, while the first two invocations are handled using only one
          except branch (the more general one) and the last two ones with two different branches,
          able to distinguish the exceptions (don't forget: the order of the branches makes a fundamental difference!)

        code:

            class PizzaError(Exception):
                def __init__(self, pizza, message):
                    Exception.__init__(self, message)
                    self.pizza = pizza


            class TooMuchCheeseError(PizzaError):
                def __init__(self, pizza, cheese, message):
                    PizzaError.__init__(self, pizza, message)
                    self.cheese = cheese


            def make_pizza(pizza, cheese):
                if pizza not in ['margherita', 'capricciosa', 'calzone']:
                    raise PizzaError(pizza, "no such pizza on the menu")
                if cheese > 100:
                    raise TooMuchCheeseError(pizza, cheese, "too much cheese")
                print("Pizza ready!")

            for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
                try:
                    make_pizza(pz, ch)
                except TooMuchCheeseError as tmce:
                    print(tmce, ':', tmce.cheese)
                except PizzaError as pe:
                    print(pe, ':', pe.pizza)

        output:

            Pizza ready!
            too much cheese : 110
            no such pizza on the menu : mafia

        code:

            class PizzaError(Exception):
                def __init__(self, pizza='Invalid Pizza', message='Error'):
                    Exception.__init__(self, message)
                    self.pizza = pizza


            class TooMuchCheeseError(PizzaError):
                def __init__(self, pizza='uknown', cheese='>100', message='Too much cheese'):
                    PizzaError.__init__(self, pizza, message)
                    self.cheese = cheese


            def make_pizza(pizza, cheese):
                if pizza not in ['margherita', 'capricciosa', 'calzone']:
                    raise PizzaError
                if cheese > 100:
                    raise TooMuchCheeseError
                print("Pizza ready!")


            for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
                try:
                    make_pizza(pz, ch)
                except TooMuchCheeseError as tmce:
                    print(tmce, ':', tmce.cheese)
                except PizzaError as pe:
                    print(pe, ':', pe.pizza)



        output:

            Pizza ready!
            Too much cheese : >100
            Error : Invalid Pizza


                      
--------------------------------------------------------------------------------------------------------------------------
                                                        Module 4
--------------------------------------------------------------------------------------------------------------------------



93) Generators
        A Python generator is a piece of specialized code able to produce a series of values, and to control the iteration process
        A function returns one, well-defined value
        A generator returns a series of values

94) Iterator protocol
        The iterator protocol is a way in which an object should behave to conform to the rules imposed
          by the context of the for and in statements
        An object conforming to the iterator protocol is called an iterator
        
        An iterator must provide two methods:

            __iter__() which should return the object itself and which is invoked once (it's needed for Python to
              successfully start the iteration)
            
            __next__() which is intended to return the next value (first, second, and so on) of the desired series - 
              it will be invoked by the for/in statements in order to pass through the next iteration;
            if there are no more values to provide, the method should raise the StopIteration exception.

        code:

            class Fib:
                def __init__(self, nn):
                    print("__init__")
                    self.__n = nn
                    self.__i = 0
                    self.__p1 = self.__p2 = 1

                def __iter__(self):
                    print("__iter__")
                    return self

                def __next__(self):
                    print("__next__")				
                    self.__i += 1
                    if self.__i > self.__n:
                        raise StopIteration
                    if self.__i in [1, 2]:
                        return 1
                    ret = self.__p1 + self.__p2
                    self.__p1, self.__p2 = self.__p2, ret
                    return ret

            for i in Fib(10):
                print(i)

        output:

            __init__
            __iter__
            __next__
            1
            __next__
            1
            __next__
            2
            __next__
            3
            __next__
            5
            __next__
            8
            __next__
            13
            __next__
            21
            __next__
            34
            __next__
            55
            __next__

        the iterator object is instantiated first;
        next, Python invokes the __iter__ method to get access to the actual iterator;
        the __next__ method is invoked eleven times - the first ten times produce useful values,
          while the eleventh terminates the iteration.

        code:

            class Fib:
                def __init__(self, nn):
                    self.__n = nn
                    self.__i = 0
                    self.__p1 = self.__p2 = 1

                def __iter__(self):
                    print("Fib iter")
                    return self

                def __next__(self):
                    self.__i += 1
                    if self.__i > self.__n:
                        raise StopIteration
                    if self.__i in [1, 2]:
                        return 1
                    ret = self.__p1 + self.__p2
                    self.__p1, self.__p2 = self.__p2, ret
                    return ret

            class Class:
                def __init__(self, n):
                    self.__iter = Fib(n)

                def __iter__(self):
                    print("Class iter")
                    return self.__iter;


            object = Class(8)

            for i in object:
                print(i)

        output:

            Class iter
            1
            1
            2
            3
            5
            8
            13
            21

95) yield
        turns the function into a generator:
            code:

                def fun(n):
                    for i in range(n):
                        return i

            to

                def fun(n):
                    for i in range(n):
                        yield i

96) How to build a generator
        code:

            def fun(n):
                for i in range(n):
                    yield i


            for v in fun(5):
                print(v)

        output:

            0
            1
            2
            3
            4

        A generator to produce the first n powers of 2
        code:

            def powers_of_2(n):
                power = 1
                for i in range(n):
                    yield power
                    power *= 2


            for v in powers_of_2(8):
                print(v)

        output:

            1
            2
            4
            8
            16
            32
            64
            128

97) list() function in generators
        The list() function can transform a series of subsequent generator invocations into a real list:
        code:

            def powers_of_2(n):
                power = 1
                for i in range(n):
                    yield power
                    power *= 2


            t = list(powers_of_2(3))
            print(t)

        output:

            [1, 2, 4]

98) The in operator
        the context created by the in operator allows the use of a generator
        code:

            def powers_of_2(n):
                power = 1
                for i in range(n):
                    yield power
                    power *= 2


            for i in range(20):
                if i in powers_of_2(4):
                    print(i)

        output:

            1
            2
            4
            8

99) Fibonacci number generator
        code:

            def fibonacci(n):
                p = pp = 1
                for i in range(n):
                    if i in [0, 1]:
                        yield 1
                    else:
                        n = p + pp
                        pp, p = p, n
                        yield n

            fibs = list(fibonacci(10))
            print(fibs)

        output:

            [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


100) List comprehensions
        A list comprehension becomes a generator when used inside parentheses
        code:

            def powers_of_2(n):
                power = 1
                for i in range(n):
                    yield power
                    power *= 2


            t = [x for x in powers_of_2(5)]
            print(t)

        output:

            [1, 2, 4, 8, 16]
            
        code:

            list_1 = []

            for ex in range(6):
                list_1.append(10 ** ex)

            list_2 = [10 ** ex for ex in range(6)]

            print(list_1)
            print(list_2)

        output:

            [1, 10, 100, 1000, 10000, 100000]
            [1, 10, 100, 1000, 10000, 100000]

        code:

            the_list = []

            for x in range(10):
                the_list.append(1 if x % 2 == 0 else 0)

            print(the_list)

        output:

            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

        code:

            the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
            print(the_list)

        output:

            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

        code:

            the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
            the_generator = (1 if x % 2 == 0 else 0 for x in range(10))
            print(the_generator, the_list)

            for v in the_list:
                print(v, end=" ")
            print()

            for v in the_generator:
                print(v, end=" ")
            print()

        output:

            <generator object <genexpr> at 0x00000218D5EF97D0> [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
            1 0 1 0 1 0 1 0 1 0 
            1 0 1 0 1 0 1 0 1 0

        It's the parentheses. The brackets make a comprehension, the parentheses make a generator.

        How can you know that the second assignment creates a generator, not a list?
        There is some proof we can show you. Apply the len() function to both these entities.

        len(the_list) will evaluate to 10. Clear and predictable. len(the_generator) will raise an exception, 
          and you will see the following message:
            TypeError: object of type 'generator' has no len()

        code:

            for v in [1 if x % 2 == 0 else 0 for x in range(10)]:
                print(v, end=" ")
            print()

            for v in (1 if x % 2 == 0 else 0 for x in range(10)):
                print(v, end=" ")
            print()

        output:

            1 0 1 0 1 0 1 0 1 0 
            1 0 1 0 1 0 1 0 1 0
            
        Note: the same appearance of the output doesn't mean that both loops work in the same way.
        In the first loop, the list is created (and iterated through) as a whole - it actually exists when the loop is being executed.
        In the second loop, there is no list at all - there are only subsequent values produced by the generator, one by one.

101) lambda
        A lambda function is a function without a name (you can also call it an anonymous function)
            lambda parameters: expression
        such a clause returns the value of the expression when taking into account the current value of the current lambda argument
        returns the value of the expression when taking into account the current value of the current lambda argument

        code:

            two = lambda: 2
            sqr = lambda x: x * x
            pwr = lambda x, y: x ** y

            for a in range(-2, 3):
                print(sqr(a), end=" ")
                print(pwr(a, two()))

        output:

            4 4
            1 1
            0 0
            1 1
            4 4

        code:

            def print_function(args, fun):
                for x in args:
                    print('f(', x,')=', fun(x), sep='')

            def poly(x):
                return 2 * x**2 - 4 * x + 2

            print_function([x for x in range(-2, 3)], poly)

        output:

            f(-2)=18
            f(-1)=8
            f(0)=2
            f(1)=0
            f(2)=2

        code:

            def print_function(args, fun):
                for x in args:
                    print('f(', x,')=', fun(x), sep='')

            print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)

        output:

            f(-2)=18
            f(-1)=8
            f(0)=2
            f(1)=0
            f(2)=2

102) map()
        map(function, list)
        applies the function passed by its first argument to all its second argument's elements,
          and returns an iterator delivering all subsequent function results.
          use the resulting iterator in a loop, or convert it into a list using the list() function
        can accept more than 2 arguments

        code:

            def a(c):
                return c * 10
            b = [x for x in range(10)]

            print(list(map(a, b)))

        output:

            [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

        code:

            print(list(map(lambda a: a * 10, [x for x in range(10)])))

        output:

            [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

        code:

            list_1 = [x for x in range(5)]
            list_2 = list(map(lambda x: 2 ** x, list_1))
            print(list_2)

            for x in map(lambda x: x * x, list_2):
                print(x, end=' ')
            print()

        output:

            [1, 2, 4, 8, 16]
            1 4 16 64 256

103) filter()
        filters its second argument while being guided by directions flowing from the function specified as the first argument
        the elements which return True from the function pass the filter - the others are rejected
        returns an iterator
        
        code:

            from random import seed, randint

            seed()
            data = [randint(-10,10) for x in range(5)]
            filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

            print(data)
            print(filtered)

        output:

            [6, 3, 3, 2, -7]
            [6, 2]

104) closures
        closure is a technique which allows the storing of values in spite of the fact that the context in which
          they have been created does not exist anymore
         a function that captures the local variables from its enclosing scope. This means that even after the outer 
          function has finished executing, the inner function retains access to the variables and parameters of the outer function
        code:

            def outer(par):
                loc = par

                def inner():
                    return loc
                return inner


            var = 1
            fun = outer(var)
            print(fun())

        output:

            1

        A closure has to be invoked in exactly the same way in which it has been declared

        code:

            def make_closure(par):
                loc = par

                def power(p):
                    return p ** loc
                return power


            fsqr = make_closure(2)
            fcub = make_closure(3)

            for i in range(5):
                print(i, fsqr(i), fcub(i))

        output:

            0 0 0
            1 1 1
            2 4 8
            3 9 27
            4 16 64

        You can create as many closures as you want using one and the same piece of code
        This is done with a function named make_closure()

105) Streams
        an abstraction used to read from or write to files.
        streams represent the flow of data to or from a storage medium, such as a file on disk
        The opening of the stream is not only associated with the file, 
          but should also declare the manner in which the stream will be processed. This declaration is called an open mode
        If the opening is successful, 
          the program will be allowed to perform only the operations which are consistent with the declared open mode

        There are two basic operations performed on the stream:

            read from the stream: the portions of the data are retrieved from the file and placed in a memory area 
              managed by the program (e.g., a variable);
            write to the stream: the portions of the data from the memory (e.g., a variable) are transferred to the file.

        3 basic modes:

            read
                read operations only
                trying to write to the stream will cause UnsupportedOperation, which inherits OSError and ValueError, from the io module
            write
                write operations only
                attempting to read the stream will cause the exception mentioned above
            update
                both

106) File handles
        Python assumes that every file is hidden behind an object of an adequate class
        An object of an adequate class is created when you open the file and annihilate it at the time of closing
        The operations you're allowed to use are imposed by the way in which you've opened the file

                    IOBase
                 /    |      \
                /     |       \
               /      |        \
              /       |         \
        RawIOBase BufferedIOBase TextIOBase

        you never use constructors to bring these objects to life. The only way you obtain them is to invoke the function named open()
        the function analyses the arguments you've provided, and automatically creates the required object
        
        if you want to get rid of the object, you invoke the method named close()
        the invocation will sever the connection to the object, and the file and will remove the object

        the end of line is marked by a pair of characters, CR and LF (ASCII codes 13 and 10) which can be encoded as \r\n

        portability
            If you create a program responsible for processing a text file, and it is written for Windows, you can recognize the 
              ends of the lines by finding the \r\n characters, but the same program running in a Unix/Linux environment will be 
                completely useless, and vice versa: the program written for Unix/Linux systems might be useless in Windows.

            Such undesirable features of the program, which prevent or hinder the use of the program in different environments, 
              are called non-portability.

            Similarly, the trait of the program allowing execution in different environments is called portability.
              A program endowed with such a trait is called a portable program.

        when the stream is open & advised that the data in the associated file will be processed as text, it is switched into text mode

        during reading/writing of lines from/to the associated file, a translation of newline characters occurs:
            during read operations, every pair of \r\n characters is replaced with a single \n character
            during write operations, every \n character is replaced with a pair of \r\n characters
    
107) Opening the streams & selecting text and binary modes
        stream = open(file, mode = 'r', encoding = None)
        FileNotFoundError if the file you're going to read doesn't exist
        The default opening mode is reading in text mode, while the default encoding depends on the platform used
        
        Opening the streams: modes
            r   read mode
                file associated with the stream must exist and has to be readable, othwewise open() raises an exception
            w   write mode
                file associated with the stream doesn't need to exist, will be created if it doesnt exist,
                will be tranculated to length 0 if exists (will be erased), otherwise open() raises an exception if creation impossible
            a   append mode
                file associated with the stream doesn't need to exist, will be created if it doesnt exist,
                if exists, virtual recording head will be set at the end of the file (previous content of the file remains untouched)
            r+  read and update mode
                file associated with the stream must exist and has to be writeable, othwewise open() raises an exception
                both read and write operations are allowed for the stream
            w+  write and update mode
                file associated with the stream doesn't need to exist, will be created if it doesnt exist, 
                previous content of the file remains untouched
                both read and write operations are allowed for the stream
                
        Selecting text and binary modes
            if b at the end of a stream mode, the stream is to be opened in the binary mode
            if the mode string ends with a letter t the stream is opened in the text mode
            Text mode is the default behaviour assumed when no binary/text mode specifier is used
             the successful opening of the file will set the current file position (the virtual reading/writing head) before the
               first byte of the file if the mode is not a and after the last byte of file if the mode is set to a

            Text        mode    	Binary mode	Description
            rt	        rb	            read
            wt	        wb          	write
            at	        ab	            append
            r+t	        r+b	            read and update
            w+t	        w+b         	write and update

            extra
                You can also open a file for its exclusive creation. You can do this using the x open mode.
                  If the file already exists, the open() function will raise an exception

108) Opening the stream for the first time
        code:

            try:
                stream = open("C:\\Users\\Micro\\Desktop\\desk\Code\\PCAP\\file.txt", "rt")
                # Processing goes here.
                stream.close()
            except Exception as exc:
                print("Cannot open the file:", exc)

109) Pre-opened streams
        import sys

        sys.stdin
            stdin (as standard input)
            the stdin stream is normally associated with the keyboard, 
              pre-open for reading and regarded as the primary data source for the running programs;
            the well-known input() function reads data from stdin by default.

        sys.stdout
            stdout (as standard output)
            the stdout stream is normally associated with the screen,
              pre-open for writing, regarded as the primary target for outputting data by the running program;
            the well-known print() function outputs the data to the stdout stream
        
        sys.stderr
            stderr (as standard error output)
            the stderr stream is normally associated with the screen, pre-open for writing,
              regarded as the primary place where the running program should send information on the errors encountered during its work
            the separation of stdout (useful results produced by the program) from the stderr (error messages, undeniably useful but does
              not provide results) gives the possibility of redirecting these two types of information to the different targets

110) Closing streams
        stream.close()
        the function returns nothing but raises IOError exception in case of error

111) Diagnosing stream problems
        The IOError object is equipped with a property named errno (the name comes from the phrase error number)
          and you can access it as follows:
            
            code:

                try:
                    # Some stream operations.
                except IOError as exc:
                    print(exc.errno)

        errno.EACCES → Permission denied
            The error occurs when you try, for example, to open a file with the read only attribute for writing.
        errno.EBADF → Bad file number
            The error occurs when you try, for example, to operate with an unopened stream.
        errno.EEXIST → File exists
            The error occurs when you try, for example, to rename a file with its previous name.
        errno.EFBIG → File too large
            The error occurs when you try to create a file that is larger than the maximum allowed by the operating system.
        errno.EISDIR → Is a directory
            The error occurs when you try to treat a directory name as the name of an ordinary file.
        errno.EMFILE → Too many open files
            The error occurs when you try to simultaneously open more streams than acceptable for your operating system.
        errno.ENOENT → No such file or directory
            The error occurs when you try to access a non-existent file/directory.
        errno.ENOSPC → No space left on device
            The error occurs when there is no free space on the media    

        code:
            
                import errno

                try:
                    s = open("C:\\Users\\Micro\\Desktop\\desk\Code\\PCAP\\file.txt", "rt")
                    # Actual processing goes here.
                    s.close()
                except Exception as exc:
                    if exc.errno == errno.ENOENT:
                        print("The file doesn't exist.")
                    elif exc.errno == errno.EMFILE:
                        print("You've opened too many files.")
                    else:
                        print("The error number is:", exc.errno)

112) strerror()
        comes from the os module and expects just one argument - an error number
        give an error number and get a string describing the meaning of the error
        if you pass a non-existent error code, the function will raise ValueError exception

        code:

            from os import strerror

            try:
                s = open("C:\\Users\\Micro\\Desktop\\desk\Code\\PCAP\\file.txt", "rt")
                # Actual processing goes here.
                s.close()
            except Exception as exc:
                print("The file could not be opened:", strerror(exc.errno))

113) Processing text files
        encoding = ""
            If your text files contain some national characters not covered by the standard ASCII charset,
              you may need an additional step. Your open() function invocation may require an argument denoting specific text encoding.
            For example, if you're using a Unix/Linux OS configured to use UTF-8 as a system-wide setting,
              the open() function may look as follows:

              code:

                    stream = open('file.txt', 'rt', encoding='utf-8')

            code:

            # Opening tzop.txt in read mode, returning it as a file object:
            stream = open("tzop.txt", "rt", encoding = "utf-8")
            print(stream.read()) # printing the content of the file
        
114) read()
        read a desired number of characters (including just one) from the file, and return them as a string
        read all the file contents, and return them as a string
        if there is nothing more to read (the virtual reading head reaches the end of the file), the function returns an empty string

        code:

            from os import strerror

            try:
                cnt = 0
                s = open('C:\\Users\\Micro\\Desktop\\desk\Code\\PCAP\\file.txt', "rt")
                ch = s.read(1)
                while ch != '':
                    print(ch, end='')
                    cnt += 1
                    ch = s.read(1)
                s.close()
                print("\n\nCharacters in file:", cnt)
            except IOError as e:
                print("I/O error occurred: ", strerror(e.errno))

        output:

            Beautiful is better than ugly.
            Explicit is better than implicit.
            Simple is better than complex.
            Complex is better than complicated.

            Characters in file: 131

        code:

            from os import strerror

            try:
                cnt = 0
                s = open('text.txt', "rt")
                content = s.read()
                for ch in content:
                    print(ch, end='')
                    cnt += 1
                s.close()
                print("\n\nCharacters in file:", cnt)
            except IOError as e:
                print("I/O error occurred: ", strerr(e.errno))

        output:

            Beautiful is better than ugly.
            Explicit is better than implicit.
            Simple is better than complex.
            Complex is better than complicated.

            Characters in file: 131

115) readline()
        treats the file's contents as a set of lines instead of a set of characters
        the method tries to read a complete line of text from the file, and returns it as a string in the case of success.
          otherwise, it returns an empty string

        code:

            from os import strerror

            try:
                ccnt = lcnt = 0
                s = open('C:\\Users\\Micro\\Desktop\\desk\Code\\PCAP\\file.txt', 'rt')
                line = s.readline()
                while line != '':
                    lcnt += 1
                    for ch in line:
                        print(ch, end='')
                        ccnt += 1
                    line = s.readline()
                s.close()
                print("\n\nCharacters in file:", ccnt)
                print("Lines in file:     ", lcnt)
            except IOError as e:
                print("I/O error occurred:", strerror(e.errno))

        output:

            Beautiful is better than ugly.
            Explicit is better than implicit.
            Simple is better than complex.
            Complex is better than complicated.

            Characters in file: 131
            Lines in file:      4
                        
116) readlines()
        treats the file's contents as a set of lines instead of a set of characters
        when invoked without arguments, tries to read all the file contents, and returns a list of strings, one element per file line

        code:

            from os import strerror
            name = "C:\\Users\\Micro\\Desktop\\desk\Code\\PCAP\\file.txt"

            try:
                ccnt = lcnt = 0
                s = open(name, 'rt')
                lines = s.readlines(20)
                while len(lines) != 0:
                    for line in lines:
                        lcnt += 1
                        for ch in line:
                            print(ch, end='')
                            ccnt += 1
                    lines = s.readlines(10)
                s.close()
                print("\n\nCharacters in file:", ccnt)
                print("Lines in file:     ", lcnt)
            except IOError as e:
                print("I/O error occurred:", strerror(e.errno))

        output:

            Beautiful is better than ugly.
            Explicit is better than implicit.
            Simple is better than complex.
            Complex is better than complicated.

            Characters in file: 131
            Lines in file:      4

        code:

            name = "C:\\Users\\Micro\\Desktop\\desk\Code\\PCAP\\file.txt"
            from os import strerror

            try:
                ccnt = lcnt = 0
                for line in open(name, 'rt'):
                    lcnt += 1
                    for ch in line:
                        print(ch, end='')
                        ccnt += 1
                print("\n\nCharacters in file:", ccnt)
                print("Lines in file:     ", lcnt)
            except IOError as e:
                print("I/O error occurred: ", strerror(e.errno))

        output:

            Beautiful is better than ugly.
            Explicit is better than implicit.  
            Simple is better than complex.     
            Complex is better than complicated.

            Characters in file: 131
            Lines in file:      4

        a trait of the object returned by the open() function in text mode
        the object is an instance of the iterable class
        The iteration protocol defined for the file object is very simple - its __next__ method just returns
          the next line read in from the file

117) write()
        expects just one argument, a string that will be transferred to an open file
        writing a file opened in read mode won't succeed
        no newline character is added, add manually for file to be filled with multiple lines
        the open mode w ensures that the file will be created from scratch, even if it exists and contains data) 
        
        code:

            from os import strerror

            try:
                fo = open('newtext.txt', 'wt') # A new file (newtext.txt) is created.
                for i in range(10):
                    s = "line #" + str(i+1) + "\n"
                    for ch in s:
                        fo.write(ch)
                fo.close()
            except IOError as e:
                print("I/O error occurred: ", strerror(e.errno))

        file (newtext.txt):

            line #1
            line #2
            line #3
            line #4
            line #5
            line #6
            line #7
            line #8
            line #9
            line #10

        code:

            from os import strerror

            try:
                fo = open('newtext.txt', 'wt')
                for i in range(10):
                    fo.write("line #" + str(i+1) + "\n")
                fo.close()
            except IOError as e:
                print("I/O error occurred: ", strerror(e.errno))

        file (newtext.txt):

            line #1
            line #2
            line #3
            line #4
            line #5
            line #6
            line #7
            line #8
            line #9
            line #10

        Note: you can use the same method to write to the stderr stream, but don't try to open it, as it's always open implicitly.
        For example, if you want to send a message string to stderr to distinguish it from normal program output, it may look like this:

        code:

            import sys
            sys.stderr.write("Error message")

118) Bytearrays
        a mutable sequence of bytes
        an array containing (amorphous) bytes
        setting a byte array element with a value which is not an integer will raise the TypeError exception
        setting a byte array element with a value which is outside 0-225 will raise the ValueError exception

        code:

            data = bytearray(10)
            print(data)

        output:

            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

        Such an invocation creates a bytearray object able to store ten bytes
        Note: such a constructor fills the whole array with zeros

        code:

            data = bytearray(10)

            for i in range(len(data)):
                data[i] = 10 - i
            print(data)
            for b in data:
                print(hex(b))

        output:

            bytearray(b'\n\t\x08\x07\x06\x05\x04\x03\x02\x01')
            0xa
            0x9
            0x8
            0x7
            0x6
            0x5
            0x4
            0x3
            0x2
            0x1

        we've used two methods to iterate the byte arrays, and the hex() function to see the elements printed as hexadecimal values
            
119) Writing a byte array to a file
        code:

            from os import strerror

            data = bytearray(10)
            for i in range(len(data)):
                data[i] = 10 + i
            try:
                bf = open('file.bin', 'wb')
                bf.write(data)
                bf.close()
            except IOError as e:
                print("I/O error occurred:", strerror(e.errno))

120) readinto()
        Reading bytes from a stream (to a binary file)
        code:

            from os import strerror

            data = bytearray(10)

            try:
                bf = open('file.bin', 'rb')
                bf.readinto(data)
                bf.close()

                for b in data:
                    print(hex(b), end=' ')
            except IOError as e:
                print("I/O error occurred:", strerror(e.errno))

        output:
            
            0xa 0xb 0xc 0xd 0xe 0xf 0x10 0x11 0x12 0x13

        read()
            tries to read all the contents of the file into the memory, making them a part of a newly created object of the bytes class
            this class has some similarities to bytearray, with the exception of one significant difference - it's immutable
        
        code:

            from os import strerror

            try:
                bf = open('file.bin', 'rb')
                data = bytearray(bf.read())
                bf.close()

                for b in data:
                    print(hex(b), end=' ')

            except IOError as e:
                print("I/O error occurred:", strerror(e.errno))

        output:

            0xa 0xb 0xc 0xd 0xe 0xf 0x10 0x11 0x12 0x13

        don't use this kind of read if you're not sure that the file's contents will fit the available memory

        if the read() method is invoked with an argument, it specifies the maximum number of bytes to be read

        code:

            try:
                bf = open('file.bin', 'rb')
                data = bytearray(bf.read(5))
                bf.close()

                for b in data:
                    print(hex(b), end=' ')

            except IOError as e:
                print("I/O error occurred:", strerror(e.errno))

        output:

            0xa 0xb 0xc 0xd 0xe 

        the first five bytes of the file have been read by the code - the next five are still waiting to be processed

121) Copying files

        code:

            from os import strerror

            srcname = input("Enter the source file name: ")
            try:
                src = open(srcname, 'rb')
            except IOError as e:
                print("Cannot open the source file: ", strerror(e.errno))
                exit(e.errno)	

            dstname = input("Enter the destination file name: ")
            try:
                dst = open(dstname, 'wb')
            except Exception as e:
                print("Cannot create the destination file: ", strerror(e.errno))
                src.close()
                exit(e.errno)	

            buffer = bytearray(65536)
            total  = 0
            try:
                readin = src.readinto(buffer)
                while readin > 0:
                    written = dst.write(buffer[:readin])
                    total += written
                    readin = src.readinto(buffer)
            except IOError as e:
                print("Cannot create the destination file: ", strerror(e.errno))
                exit(e.errno)	
                
            print(total,'byte(s) succesfully written')
            src.close()
            dst.close()

        lines 3 through 8: ask the user for the name of the file to copy, and try to open it to read; terminate the program execution if 
          the open fails; note: use the exit() function to stop program execution and to pass the completion code to the OS; any completion 
          code other than 0 says that the program has encountered some problems; use the errno value to specify the nature of the issue;
        lines 10 through 16: repeat nearly the same action, but this time for the output file;
        line 18: prepare a piece of memory for transferring data from the source file to the target one; such a transfer area is often 
          called a buffer, hence the name of the variable; the size of the buffer is arbitrary - in this case, we decided to use 64 
          kilobytes; technically, a larger buffer is faster at copying items, as a larger buffer means fewer I/O operations; actually, there 
          is always a limit, the crossing of which renders no further improvements; test it yourself if you want.
        line 19: count the bytes copied - this is the counter and its initial value;
        line 21: try to fill the buffer for the very first time;
        line 22: as long as you get a non-zero number of bytes, repeat the same actions;
        line 23: write the buffer's contents to the output file (note: we've used a slice to limit the number of bytes being written,
          as write() always prefer to write the whole buffer)
        line 24: update the counter;
        line 25: read the next file chunk;
        lines 30 through 32: some final cleaning - the job is done.

        if the buffer automatically takes in 65536 bytes already, why do i have to limit the write to readin in the next line?
            The reason you need to limit the write to the number of bytes actually read (readin) is because the last read operation
              might not fill the entire buffer. When you reach the end of the source file, the number of bytes read could be less than
              the buffer size (65536 bytes). 
            Therefore, you need to ensure that only the valid portion of the buffer is written to the destination file.

122) Project: Character frequency histogram

        my code:

            dictionary = {}
            src = "C:\\Users\\Micro\\Desktop\\desk\\Code\\PCAP\\file.txt"  # input("Enter source file name:   ")
            readfrom = open(src, "rt")
            text = readfrom.read()

            for char in text:
                char = char.lower()
                if (char in dictionary) and (char.isalpha() == True) and (len(char) == 1):
                    dictionary[char] += 1
                elif (char.isalpha() == True) and (len(char) == 1):
                    dictionary[char] = 1
                    
            sorted_dictionary =  sorted(dictionary)

            for key in sorted_dictionary:
                if dictionary[key] != 0:
                    print(f"{key} -> {dictionary[key]}")

            readfrom.close()
        
        their code:

            from os import strerror

            # Initialize 26 counters for each Latin letter.
            # Note: we've used comprehension to do that.
            counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
            file_name = input("Enter the name of the file to analyze: ")
            try:
                f = open(file_name, "rt")
                for line in f:
                    for char in line:
                        # If it is a letter...
                        if char.isalpha():
                            # ... we'll treat it as lower-case and update the appropriate counter.
                            counters[char.lower()] += 1
                f.close()
                # Let's output the counters.
                for char in counters.keys():
                    cnt = counters[char]
                    if cnt > 0:
                        print(char, '->',cnt)
            except IOError as e:
                print("I/O error occurred: ", strerror(e.errno))

123) Project: Sorted character frequency histogram

        my code:

            dictionary, sorted_dictionary = {}, {}
            src = "C:\\Users\\Micro\\Desktop\\desk\\Code\\PCAP\\file.txt"  # input("Enter source file name:   ")
            dst = "C:\\Users\\Micro\\Desktop\\desk\\Code\\PCAP\\file.hist"
            readfrom = open(src, "rt")
            writeto = open(dst, "wt")
            readfile = readfrom.read()

            for char in readfile:
                char = char.lower()
                if (char in dictionary) and (char.isalpha() == True) and (len(char) == 1):
                    dictionary[char] += 1
                elif (char.isalpha() == True) and (len(char) == 1):
                    dictionary[char] = 1

            sorted_items = sorted(dictionary.items(), key = lambda item: item[1], reverse = True)
            sorted_dictionary = {key: value for key, value in sorted_items}

            for key, value in sorted_dictionary.items():
                writeto.write(f"{key} -> {value}\n")

            readfrom.close()
            writeto.close()

        their code:
        
            from os import strerror

            counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
            file_name = input("Enter the name of the file to analyze: ")
            try:
                f = open(file_name, "rt")
                for line in f:
                    for char in line:
                        if char.isalpha():
                            counters[char.lower()] += 1
                f.close()
                f = open(file_name + '.hist', 'wt')
                # Note: we've used lambda to access the directory's elements and set reverse to get a valid order.
                for char in sorted(counters.keys(), key=lambda x: counters[x], reverse=True):
                    cnt = counters[char]
                    if cnt > 0:
                        f.write(char + ' -> ' + str(cnt) + '\n')
                f.close()
            except IOError as e:
                print("I/O error occurred: ", strerror(e.errno))
        
124) Project: Evaluating students' results

        my code:

            from os import strerror
            import errno

            class StudentsDataException(Exception):
                pass

            class BadLine(StudentsDataException):
                def __init__(self, error_line, error_string):
                    super().__init__(self)
                    self.error_line = error_line
                    self.error_string = error_string
                    

            class FileEmpty(StudentsDataException):
                def __init__(self):
                    super().__init__(self)

            src = "C:\\Users\\Micro\\Desktop\\desk\\Code\\PCAP\\samplefile.txt"  # input("Enter Prof. Jekyll's file name:   ")
            results = {}

            try:
                source = open(src, "rt")
                info = source.readlines()
                if not info:
                    raise FileEmpty()

                for errorcase, line in enumerate(info, start=1):
                    if "\t" not in line:
                        raise BadLine(errorcase, line)

                    name, score = line[:line.rfind("\t")].replace("\t", " "), float(line[line.rfind("\t") + 1:])
                    if name not in results:
                        results[name] = score
                    else:
                        results[name] += score
                
                for key in sorted(results.keys()):
                    print(key + "\t" + str(results[key]))

            except IOError as exception:
                print("File I/O error occurred:", strerror(exception.errno))
            except BadLine as exception:
                print("Bad line #" + str(exception.error_line) + " in source file:" + exception.error_string)
            except FileEmpty:
                print("Source file empty")

        their code:

            # A base exception class for our code:
            class StudentsDataException(Exception):
                pass


            # An exception for erroneous lines:
            class BadLine(StudentsDataException):
                def __init__(self, line_number, line_string):
                    super().__init__(self)
                    self.line_number = line_number
                    self.line_string = line_string


            # An exception for an empty file.
            class FileEmpty(StudentsDataException):
                def __init__(self):
                    super().__init__(self)


            from os import strerror

            # A dictionary for students' data:
            data = { }

            file_name = input("Enter student's data filename: ")
            line_number = 1
            try:
                f = open(file_name, "rt")
                # Read the whole file into list.
                lines = f.readlines()
                f.close()
                # Is the file empty?
                if len(lines) == 0:
                    raise FileEmpty()
                # Scan the file line by line.
                for i in range(len(lines)):
                    # Get the i'th line.
                    line = lines[i]
                    # Divide it into columns.
                    columns = line.split()
                    # There shoule be 3 columns - are they there?
                    if len(columns) != 3:
                        raise BadLine(i + 1, line)
                    # Build a key from student's given name and surname.
                    student = columns[0] + ' ' + columns[1]
                    # Get points.
                    try:
                        points = float(columns[2])
                    except ValueError:
                        raise BadLine(i + 1, line)
                    # Update dictionary.
                    try:
                        data[student] += points
                    except KeyError:
                        data[student] = points
                # Print results.
                for student in sorted(data.keys()):
                    print(student,'\t', data[student])

            except IOError as e:
                print("I/O error occurred: ", strerror(e.errno))
            except BadLine as e:
                print("Bad line #" + str(e.line_number) + " in source file:" + e.line_string)
            except FileEmpty:
                print("Source file empty")

125) Getting information about the os
        os module provides a function called uname, which returns an object containing the following attributes:
            systemname — stores the name of the os;
            nodename — stores the machine name on the network;
            release — stores the os release;
            version — stores the os version;
            machine — stores the hardware identifier, e.g., x86_64.
        
        unix:
        
            code:
                
                import os
                print(os.uname())

        windows:

            code:

                import platform
                print(platform.uname())
            
            output:

                uname_result(system='Windows', node='DESKTOP-ED2OOO9', release='10', version='10.0.19045', machine='AMD64')
            
        The os module allows you to quickly distinguish the operating system using the name attribute, which supports one of the following names:
            posix — you'll get this name if you use Unix
            nt — you'll get this name if you use Windows
            java — you'll get this name if your code is written in Jython
                
                code:

                    import os
                    print(os.name)

                output:

                    nt

126) Creating directories in Python
        mkdir → creates a directory in the specified path. Note that running the program twice will raise a FileExistsError
        listdir → returns a list containing the names of the files and directories that are in the path passed as an argument
                    if no argument is passed to it, the current working directory will be used
                    the listdir function omits the entries '.' and '..', which are displayed, for example, when using the ls -a command on Unix systems. 
                    If the path isn't passed, the result will be returned for the current working directory

        my_first_directory
            relative path which will create the my_first_directory directory in the current working directory;
        ./my_first_directory
            relative path that explicitly points to the current working directory. It has the same effect as the path above;
        ../my_first_directory
            relative path that will create the my_first_directory directory in the parent directory of the current working directory;
        /python/my_first_directory
            absolute path that will create the my_first_directory directory, exists in the python directory in the root directory.

        chmod function → to change directory permissions

        code:

            import os

            os.mkdir("my_first_directory")
            print(os.listdir())

127) Recursive directory creation
        makedirs → create a directory recursively
        chdir → to move between directories, changes the current working directory to the specified path

        code:

            import os

            os.makedirs("my_first_directory/my_second_directory")
            os.chdir("my_first_directory")
            print(os.listdir())

        output:            

            ['my_second_directory']

        equivalent to:

            mkdir my_first_directory/my_second_directory

128) Get current working directory
        getcwd  → get current working directory

        code:

            import os

            os.makedirs("my_first_directory/my_second_directory")
            os.chdir("my_first_directory")
            print(os.getcwd())
            os.chdir("my_second_directory")
            print(os.getcwd())

        output:

            .../my_first_directory
            .../my_first_directory/my_second_directory

129) Deleting directories
        rmdir → delete an empty directory
              → if one of the directories doesn't exist or isn't empty, an exception will be raised
        removedirs → removes all directories specified in the given path

        code:

            import os

            os.mkdir("my_first_directory")
            print(os.listdir())
            os.rmdir("my_first_directory")
            print(os.listdir())

        code:

            import os

            os.makedirs("my_first_directory/my_second_directory")
            os.removedirs("my_first_directory/my_second_directory")
            print(os.listdir())

130) system()
        to execute a command in the underlying operating system's shell, python passes the command string to the os, which executes it as if
            it were run from the command line or terminal
        returns the exit status code of the command executed, a return value of 0 indicates that the command executed successfully,
            while a non-zero value indicates an error
        
        code:

            import os

            returned_value = os.system("mkdir my_first_directory")
            print(returned_value)

        output:

            0

131) Project: The os module

        their code:

            import os

            class DirectorySearcher:
                def find(self, path, dir):
                    try:
                        os.chdir(path)
                    except OSError:
                        return
                    current_dir = os.getcwd()
                    for entry in os.listdir("."):
                        if entry == dir:
                            print(os.getcwd() + "/" + dir)
                        self.find(current_dir + "/" + entry, dir)
            directory_searcher = DirectorySearcher()
            directory_searcher.find("./tree", "python")

132) Getting the current local date and creating date objects
        datetime module provides classes for working with date and time, one of its classes is called date

        code:

            from datetime import date

            today = date.today()

            print("Today:", today)
            print("Year:", today.year)
            print("Month:", today.month)
            print("Day:", today.day)


        output:

            Today: 2024-07-20
            Year: 2024
            Month: 7
            Day: 20

        The today method returns a date object representing the current local date, the date object has three attributes: year, month, and day

        code:

            from datetime import date

            my_date = date(2019, 11, 4)
            print(my_date)


        output:

            2019-11-04

        When creating a date object, keep the following restrictions in mind:
            Parameters & Restrictions
                year	
                    The year parameter must be greater than or equal to 1 (MINYEAR constant) and less than or equal to 9999 (MAXYEAR constant).

                month	
                    The month parameter must be greater than or equal to 1 and less than or equal to 12.

                day	
                    The day parameter must be greater than or equal to 1 and less than or equal to the last day of the given month and year.

133) Creating a date object from a timestamp
        time() returns num of seconds from January 1, 1970 to the current moment in the form of a float number
        timestamp is the dif bw a particular date (including time) and January 1, 1970
        code:

            from datetime import date
            import time

            timestamp = time.time()
            print("Timestamp:", timestamp)

            d = date.fromtimestamp(timestamp)
            print("Date:", d)


        output:

            Timestamp: 1721491077.66011
            Date: 2024-07-20

134) Creating a date object using the ISO format
        fromisoformat method → takes a date in the YYYY-MM-DD format compliant with the ISO 8601 standard
        code:

            from datetime import date
            d = date.fromisoformat('2019-11-04')
            print(d)


        output:

            2019-11-04

135) The replace() method
        returns a changed date object, and needs to be assigned to a variable
        code:

            from datetime import date

            d = date(1991, 2, 5)
            print(d)

            d = d.replace(year=1992, month=1, day=16)
            print(d)

        output:

            1991-02-05
            1992-01-16

136) weekday() & isodayweek()
        weekday returns the day of the week as an integer, where 0 is Monday and 6 is Sunday
        isoweekday() returns the day of the week as an integer, but 1 is Monday, and 7 is Sunday
            for the same date we get a different integer, but expressing the same day of the week, the integer returned by the isodayweek
              method follows the ISO 85601 specification
        code:

            from datetime import date

            d = date(2019, 11, 4)
            print(d.weekday())
            print(d.isoweekday())

        output:

                0
                1

137) Creating time objects
        time(hour, minute, second, microsecond, tzinfo, fold)
        The time class constructor accepts the following optional parameters:

        Parameters	& Restrictions
            hour	
                The hour parameter must be greater than or equal to 0 and less than 23.
            minute	
                The minute parameter must be greater than or equal to 0 and less than 59.
            second	
                The second parameter must be greater than or equal to 0 and less than 59.
            microsecond	
                The microsecond parameter must be greater than or equal to 0 and less than 1000000.
            tzinfo
                The tzinfo parameter must be a tzinfo subclass object or None (default).
            fold	
                The fold parameter must be 0 or 1 (default 0).

        The tzinfo parameter is associated with time zones, while fold with wall times

        code:

            from datetime import time

            t = time(14, 53, 20, 1)

            print("Time:", t)
            print("Hour:", t.hour)
            print("Minute:", t.minute)
            print("Second:", t.second)
            print("Microsecond:", t.microsecond)

        output:

            Time: 14:53:20.000001
            Hour: 14
            Minute: 53
            Second: 20
            Microsecond: 1

        In the example, we passed four parameters to the class constructor: hour, minute, second, and microsecond.
          Each of them can be accessed using the class attributes.

138) sleep()
        suspends program execution for the given number of seconds
        the sleep function accepts only an integer or a floating point number
        code:

            import time

            class Student:
                def take_nap(self, seconds):
                    print("I'm very tired. I have to take a nap. See you later.")
                    time.sleep(seconds)
                    print("I slept well! I feel great!")

            student = Student()
            student.take_nap(5)

        output:

            I'm very tired. I have to take a nap. See you later.
            I slept well! I feel great!                                 (Output after a 5 second delay)

139) ctime()
         converts the time in seconds since January 1, 1970 (Unix epoch) to a string
         code:

            import time
            from datetime import date

            timestamp = time.time()
            seconds = time.ctime(timestamp)

            print(f"{timestamp}\n{seconds}")
            print(f"\n{time.ctime()}")

        output:

            1721506087.4283576
            Sat Jul 20 23:08:07 2024

            Sat Jul 20 23:08:07 2024

140) gmtime() & localtime()
        Some of the functions available in the time module require knowledge of the struct_time class, the class looks like this:

            time.struct_time:
                tm_year   # specifies the year
                tm_mon    # specifies the month (value from 1 to 12)
                tm_mday   # specifies the day of the month (value from 1 to 31)
                tm_hour   # specifies the hour (value from 0 to 23)
                tm_min    # specifies the minute (value from 0 to 59)
                tm_sec    # specifies the second (value from 0 to 61 )
                tm_wday   # specifies the weekday (value from 0 to 6)
                tm_yday   # specifies the year day (value from 1 to 366)
                tm_isdst  # specifies whether daylight saving time applies (1 - yes, 0 - no, -1 - it isn't known)
                tm_zone   # specifies the timezone name (value in an abbreviated form)
                tm_gmtoff # specifies the offset east of UTC (value in seconds)

        The struct_time class also allows access to values using indexes. Index 0 returns the value in tm_year,
          while 8 returns the value in tm_isdst
        The exceptions are tm_zone and tm_gmoff, which cannot be accessed using indexes

        code:

            import time

            timestamp = time.time()
            print(time.gmtime(timestamp))
            print(time.localtime(timestamp))

        output:

            time.struct_time(tm_year=2024, tm_mon=7, tm_mday=20, tm_hour=20, tm_min=32, tm_sec=11, tm_wday=5, tm_yday=202, tm_isdst=0)
            time.struct_time(tm_year=2024, tm_mon=7, tm_mday=20, tm_hour=23, tm_min=32, tm_sec=11, tm_wday=5, tm_yday=202, tm_isdst=0)

        For the gmtime function, the tm_isdst attribute is always 0

141) asctime() & mktime()
        asctime() → converts a struct_time object or a tuple to a string
            if no arguments are passed, time returned by localtime is used
        mktime() → converts a struct_time obkect or a tuple that expressed the local time to the number of seconds since the Unix epoch

        code:

            import time

            timestamp = 1572879180
            st = time.gmtime(timestamp)

            print(time.asctime(st))
            print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))

        output:

            Mon Nov  4 14:53:00 2019
            1572879180.0

142) Creating datetime objects
        In the datetime module, date & time are represented as separate objects or as one. The class that combines date & time is called datetime
        datetime(year, month, day, hour, minute, second, microsecond, tzinfo, fold)

        code:

            from datetime import datetime

            dt = datetime(2019, 11, 4, 14, 53)

            print("Datetime:", dt)
            print("Date:", dt.date())
            print("Time:", dt.time())

        output:

            Datetime: 2019-11-04 14:53:00
            Date: 2019-11-04
            Time: 14:53:00

        All parameters passed to the constructor go to read-only class attributes.
          They're year, month, day, hour, minute, second, microsecond, tzinfo, and fold.

        The example shows two methods that return two different objects. The method called date returns the date object with the given
          year, month, and day, while the method called time returns the time object with the given hour and minute

143) Methods that return the current date and time
        today()  →  returns the current local date and time with the tzinfo attribute set to None;
        now()  →    returns the current local date and time the same as the today method, unless we pass the optional argument tz to it.
                        The argument of this method must be an object of the tzinfo subclass;
        utcnow() →  returns the current UTC date and time with the tzinfo attribute set to None.

        code:

            from datetime import datetime

            print("today:", datetime.today())
            print("now:", datetime.now())
            print("utcnow:", datetime.utcnow())

        output:

            today: 2024-07-20 20:47:27.591619
            now: 2024-07-20 20:47:27.592013
            utcnow: 2024-07-20 20:47:27.592256

        the result of all the three methods is the same. The small differences are caused by the time elapsed between subsequent calls

144) Getting a timestamp - timestamp()
        The timestamp method returns a float value expressing the number of seconds elapsed between the date and time indicated by the datetime object
          and January 1, 1970, 00:00:00 (UTC)
        
        code:

            from datetime import datetime

            dt = datetime(2024, 7, 20, 23, 52)
            print("Timestamp:", dt.timestamp())

        output:

            Timestamp: 1721508720.0

145) Date & time formatting - strftime()
        allows us to return the date and time in the format we specify
        takes only one argument in the form of a string specifying the format that can consist of directives
        A directive is a string consisting of the character % (percent) and a lowercase or uppercase letter,
          e.g., the directive %Y means the year with the century as a decimal number.
        
        code:
            
            from datetime import date

            d = date(2024, 7, 20)
            print(d.strftime('%Y/%m/%d'))

        output:

            2024/07/20

        all available directives: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

        code:

            from datetime import time
            from datetime import datetime

            t = time(14, 53)
            print(t.strftime("%H:%M:%S"))

            dt = datetime(2020, 11, 4, 14, 53)
            print(dt.strftime("%y/%B/%d %H:%M:%S"))

        output:

            14:53:00
            20/November/04 14:53:00

146) strftime() in the time module
        code:

            import time

            timestamp = 1572879180
            st = time.gmtime(timestamp)

            print(st)
            print(time.strftime("%Y/%m/%d %H:%M:%S", st))
            print(time.strftime("%Y/%m/%d %H:%M:%S"))
        
        output:

            time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=0)
            2019/11/04 14:53:00
            2024/07/21 00:16:19

        all available directives in the time module: https://docs.python.org/3/library/time.html#time.strftime

147) strptime()


        code:

            from datetime import datetime
            print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))

        output:

            2019-11-04 14:53:00

        code:

            import time
            print(time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))

        output:

            time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=-1)

        datetime.strptime: Converts a string representing a date and time into a datetime object
        time.strptime: Converts a string representing a time into a struct_time object

148) Date & time operations - timedelta()
        The timedelta class in the datetime module allows for date and time calculation,
          such as subtracting two date or datetime objects to get the difference in days, hours, minutes, and seconds
        
        code:

            from datetime import date
            from datetime import datetime

            d1 = date(2020, 11, 4)
            d2 = date(2019, 11, 4)

            print(d1 - d2)

            dt1 = datetime(2020, 11, 4, 0, 0, 0)
            dt2 = datetime(2019, 11, 4, 14, 53, 0)

            print(dt1 - dt2)

        output:

            366 days, 0:00:00
            365 days, 9:07:00

        The difference in outputs arises because date subtraction yields days only,
          while datetime subtraction includes differences in days, hours, minutes, and seconds

149) Creating timedelta objects
        arguments accepted by the class constructor:
        days, seconds, microseconds, milliseconds, minutes, hours, and weeks

        code:

            from datetime import timedelta

            delta = timedelta(weeks=2, days=2, hours=3)
            print(delta)

        output:

            16 days, 3:00:00

        code:

            from datetime import timedelta

            delta = timedelta(weeks=2, days=2, hours=3)
            print("Days:", delta.days)
            print("Seconds:", delta.seconds)
            print("Microseconds:", delta.microseconds)

        output:

            Days: 16
            Seconds: 10800
            Microseconds: 0

        code:

            from datetime import timedelta
            from datetime import date
            from datetime import datetime

            delta = timedelta(weeks=2, days=2, hours=2)
            print(delta)

            delta2 = delta * 2
            print(delta2)

            d = date(2019, 10, 4) + delta2
            print(d)

            dt = datetime(2019, 10, 4, 14, 53) + delta2
            print(dt)

        output:

            16 days, 02:00:00
            32 days, 04:00:00
            2019-11-05
            2019-11-05 18:53:00

150) Project: The datetime and time modules

        my code:

            from datetime import datetime

            object = datetime(2020, 11, 4, 14, 53)

            print(object.strftime("%Y/%m/%d %H:%M:%S"))
            print(object.strftime("%y/%B/%d %H:%M:%S %p"))
            print(object.strftime("%a, %Y %B %d"))
            print(object.strftime("%A, %Y %B %d"))
            print(object.strftime("Weekday: %w"))
            print(object.strftime("Day of the year: %j"))
            print(object.strftime("Week number of the year: %U"))

        their code:

            from datetime import datetime

            my_date = datetime(2020, 11, 4, 14, 53)

            print(my_date.strftime("%Y/%m/%d %H:%M:%S"))
            print(my_date.strftime("%y/%B/%d %H:%M:%S %p"))
            print(my_date.strftime("%a, %Y %b %d"))
            print(my_date.strftime("%A, %Y %B %d"))
            print(my_date.strftime("Weekday: %w"))
            print(my_date.strftime("Day of the year: %j"))
            print(my_date.strftime("Week number of the year: %W"))

151) the calendar module
        Day of the week	       Integer value	    Constant
        Monday	                    0	        calendar.MONDAY
        Tuesday         	        1	        calendar.TUESDAY
        Wednesday       	        2	        calendar.WEDNESDAY
        Thursday	                3	        calendar.THURSDAY
        Friday	                    4	        calendar.FRIDAY
        Saturday        	        5	        calendar.SATURDAY
        Sunday          	        6	        calendar.SUNDAY

        The first day of the week (Monday) is represented by  0 & the calendar.MONDAY constant, while the last day of the week (Sunday) is 
        represented by 6 & the calendar.SUNDAY constant.

        For months, integer values are indexed from 1, i.e., January is represented by 1, and December by 12

        w - date column width (default 2)
        l - number of lines per week (default 1)
        c - number of spaces between month columns (default 6)
        m - number of columns (default 3)

        prcal() → has the same parameters as calendar(), but doesn't require printing to display the calendar:

            import calendar
            calendar.prcal(2020)

        code:

            import calendar
            print(calendar.calendar(2020))

        output:

                                            2020

                January                   February                   March
            Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2  3  4  5                      1  2                         1
            6  7  8  9 10 11 12       3  4  5  6  7  8  9       2  3  4  5  6  7  8
            13 14 15 16 17 18 19      10 11 12 13 14 15 16       9 10 11 12 13 14 15
            20 21 22 23 24 25 26      17 18 19 20 21 22 23      16 17 18 19 20 21 22
            27 28 29 30 31            24 25 26 27 28 29         23 24 25 26 27 28 29
                                                                30 31

                April                      May                       June
            Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2  3  4  5                   1  2  3       1  2  3  4  5  6  7
            6  7  8  9 10 11 12       4  5  6  7  8  9 10       8  9 10 11 12 13 14
            13 14 15 16 17 18 19      11 12 13 14 15 16 17      15 16 17 18 19 20 21
            20 21 22 23 24 25 26      18 19 20 21 22 23 24      22 23 24 25 26 27 28
            27 28 29 30               25 26 27 28 29 30 31      29 30

                    July                     August                  September
            Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2  3  4  5                      1  2          1  2  3  4  5  6
            6  7  8  9 10 11 12       3  4  5  6  7  8  9       7  8  9 10 11 12 13
            13 14 15 16 17 18 19      10 11 12 13 14 15 16      14 15 16 17 18 19 20
            20 21 22 23 24 25 26      17 18 19 20 21 22 23      21 22 23 24 25 26 27
            27 28 29 30 31            24 25 26 27 28 29 30      28 29 30
                                    31

                October                   November                  December
            Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                    1  2  3  4                         1          1  2  3  4  5  6
            5  6  7  8  9 10 11       2  3  4  5  6  7  8       7  8  9 10 11 12 13
            12 13 14 15 16 17 18       9 10 11 12 13 14 15      14 15 16 17 18 19 20
            19 20 21 22 23 24 25      16 17 18 19 20 21 22      21 22 23 24 25 26 27
            26 27 28 29 30 31         23 24 25 26 27 28 29      28 29 30 31
                                    30

152) Calendar for a specific month
        w - date column width (default 2)
        l - number of lines per week (default 1)
        prmonth() → has the same parameters as month(), but doesn't require printing to display the calendar:

            import calendar
            calendar.prmonth(2024, 7)

        code:

            import calendar
            print(calendar.month(2024, 7))

        output:

                 July 2024      
            Mo Tu We Th Fr Sa Su
            1  2  3  4  5  6  7
            8  9 10 11 12 13 14
            15 16 17 18 19 20 21
            22 23 24 25 26 27 28
            29 30 31

153) setfirstweekday()
        change the first day of the week from monday to any other day

        code:

            import calendar
            calendar.prmonth(2024, 7)
            calendar.setfirstweekday(calendar.SUNDAY)
            print()
            calendar.prmonth(2024, 7)

        output:

                 July 2024      
            Mo Tu We Th Fr Sa Su
            1  2  3  4  5  6  7
            8  9 10 11 12 13 14
            15 16 17 18 19 20 21
            22 23 24 25 26 27 28
            29 30 31

                July 2024      
            Su Mo Tu We Th Fr Sa
                1  2  3  4  5  6
            7  8  9 10 11 12 13
            14 15 16 17 18 19 20
            21 22 23 24 25 26 27
            28 29 30 31

154) weekday()
        returns the day of the week as an integer value for the given year, month, and day

        code:

            import calendar
            print(calendar.weekday(2020, 12, 24))

        outuput:

            3

        the weekday function returns 3, which means that December 24, 2020 is a Thursday

155) weekheader()
        takes in 1 argument; width of the week header and returns the shortened week name

        code:

            import calendar
            print(calendar.weekheader(2))

        output:

            Mo Tu We Th Fr Sa Su

156) isleap()
        returns boolean, True, if the only argument passed; year, is a leap year

        code:

            import calendar

print(calendar.isleap(2020))
print(calendar.leapdays(2010, 2021))  # Up to but not including 2021.

        output:

            True
157) leapyears
        returns integer, number of leap years inside the range of the 2 passed arguments; start & end year, end year is excluded from the range

        code:

            import calendar

            print(calendar.leapdays(2010, 2021))  # Up to but not including 2021.

        output:
        
            3
        
158) Classes for creating calendars
        calendar.Calendar -             provides methods to prepare calendar data for formatting;
        calendar.TextCalendar -         is used to create regular text calendars;
        calendar.HTMLCalendar -         is used to create HTML calendars;
        calendar.LocalTextCalendar -    is a subclass of the calendar.TextCalendar class. The constructor of this class takes the locale parameter,
          which is used to return the appropriate months and weekday names.
        calendar.LocalHTMLCalendar - is a subclass of the calendar.HTMLCalendar class. The constructor of this class takes the locale parameter,
          which is used to return the appropriate months and weekday names

159) Creating a Calendar object
        The Calendar class constructor takes one optional parameter named firstweekday, by default equal to 0 (Monday), must be bw 0-6
        iterweekdays()  →  class method that returns an iterator for week day numbers

        code:

            import calendar  

            c = calendar.Calendar(calendar.SUNDAY)

            for weekday in c.iterweekdays():
                print(weekday, end=" ")
                
        output:

            6 0 1 2 3 4 5

        The first value returned is always equal to the value of the firstweekday property

160) itermonthdates()
        the method takes in 2 arguments, year and month
        all days in the specified month and year are returned,
          as well as all days before the beginning of the month or the end of the month that are necessary to get a complete week
        each day is represented by a datetime.date object

        code:

            import calendar  

            c = calendar.Calendar()

            for date in c.itermonthdates(2019, 11):
                print(date, end=" ")
            
            print()
            print()

            cal = calendar.TextCalendar()
            print(cal.formatmonth(2019, 11))

        output:

            2019-10-28 2019-10-29 2019-10-30 2019-10-31 2019-11-01 2019-11-02 2019-11-03 2019-11-04 2019-11-05 2019-11-06 2019-11-07 2019-11-08
              2019-11-09 2019-11-10 2019-11-11 2019-11-12 2019-11-13 2019-11-14 2019-11-15 2019-11-16 2019-11-17 2019-11-18 2019-11-19 2019-11-20
                2019-11-21 2019-11-22 2019-11-23 2019-11-24 2019-11-25 2019-11-26 2019-11-27 2019-11-28 2019-11-29 2019-11-30 2019-12-01 
                
               November 2019    
            Mo Tu We Th Fr Sa Su
                        1  2  3
            4  5  6  7  8  9 10
            11 12 13 14 15 16 17
            18 19 20 21 22 23 24
            25 26 27 28 29 30  

161) Other methods that return iterators
        itermonthdates()  →  takes year & month as parameters, returns the iterator to the days of the week represented by numbers
        itermonthdays() works too

        code:

            import calendar  

            c = calendar.Calendar()

            for iter in c.itermonthdates(2019, 11):
                print(iter, end=" ")

            print()
            print()

            cal = calendar.TextCalendar()
            print(cal.formatmonth(2019, 11))

        output:

            0 0 0 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 0 

            November 2019    
            Mo Tu We Th Fr Sa Su
                        1  2  3
            4  5  6  7  8  9 10
            11 12 13 14 15 16 17
            18 19 20 21 22 23 24
            25 26 27 28 29 30  

        three other similar methods in the Calendar class that differ in data returned:

        itermonthdates2  →  returns days in the form of tuples consisting of a day of the month number and a week day number
        itermonthdates3  →  returns days in the form of tuples consisting of a year, a month, and a day of the month numbers
        itermonthdates4  →  returns days in the form of tuples consisting of a year, a month, a day of the month, and a day of the week numbers

        code:

            import calendar  

            c = calendar.Calendar()

            for iter in c.itermonthdays2(2019, 11):
                print(iter, end=" ")

            print()
            print()

            for iter in c.itermonthdays3(2019, 11):
                print(iter, end=" ")

            print()
            print()

            for iter in c.itermonthdays4(2019, 11):
                print(iter, end=" ")

        output:

            (0, 0) (0, 1) (0, 2) (0, 3) (1, 4) (2, 5) (3, 6) (4, 0) (5, 1) (6, 2) (7, 3) (8, 4) (9, 5) (10, 6) (11, 0) (12, 1) (13, 2) (14, 3)
              (15, 4) (16, 5) (17, 6) (18, 0) (19, 1) (20, 2) (21, 3) (22, 4) (23, 5) (24, 6) (25, 0) (26, 1) (27, 2) (28, 3) (29, 4) (30, 5)
                (0, 6)

            (2019, 10, 28) (2019, 10, 29) (2019, 10, 30) (2019, 10, 31) (2019, 11, 1) (2019, 11, 2) (2019, 11, 3) (2019, 11, 4) (2019, 11, 5)
              (2019, 11, 6) (2019, 11, 7) (2019, 11, 8) (2019, 11, 9) (2019, 11, 10) (2019, 11, 11) (2019, 11, 12) (2019, 11, 13) (2019, 11, 14)
              (2019, 11, 15) (2019, 11, 16) (2019, 11, 17) (2019, 11, 18) (2019, 11, 19) (2019, 11, 20) (2019, 11, 21) (2019, 11, 22)
              (2019, 11, 23) (2019, 11, 24) (2019, 11, 25) (2019, 11, 26) (2019, 11, 27) (2019, 11, 28) (2019, 11, 29) (2019, 11, 30)
              (2019, 12, 1)

            (2019, 10, 28, 0) (2019, 10, 29, 1) (2019, 10, 30, 2) (2019, 10, 31, 3) (2019, 11, 1, 4) (2019, 11, 2, 5) (2019, 11, 3, 6)
              (2019, 11, 4, 0) (2019, 11, 5, 1) (2019, 11, 6, 2) (2019, 11, 7, 3) (2019, 11, 8, 4) (2019, 11, 9, 5) (2019, 11, 10, 6)
              (2019, 11, 11, 0) (2019, 11, 12, 1) (2019, 11, 13, 2) (2019, 11, 14, 3) (2019, 11, 15, 4) (2019, 11, 16, 5) (2019, 11, 17, 6)
              (2019, 11, 18, 0) (2019, 11, 19, 1) (2019, 11, 20, 2) (2019, 11, 21, 3) (2019, 11, 22, 4) (2019, 11, 23, 5) (2019, 11, 24, 6)
              (2019, 11, 25, 0) (2019, 11, 26, 1) (2019, 11, 27, 2) (2019, 11, 28, 3) (2019, 11, 29, 4) (2019, 11, 30, 5) (2019, 12, 1, 6)

162) monthdays2calendar()
        calendar docs: https://docs.python.org/3/library/calendar.html
        takes year & month, returns a list of weeks in a specific month, each week is a tuple consisting of day numbers and weekday numbers
        
        code:

            import calendar  

            c = calendar.Calendar()

            for data in c.monthdays2calendar(2020, 12):
                print(data)

            print()

            cal = calendar.TextCalendar()
            print(cal.formatmonth(2019, 11))

    output:

            [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]
            [(7, 0), (8, 1), (9, 2), (10, 3), (11, 4), (12, 5), (13, 6)]
            [(14, 0), (15, 1), (16, 2), (17, 3), (18, 4), (19, 5), (20, 6)]
            [(21, 0), (22, 1), (23, 2), (24, 3), (25, 4), (26, 5), (27, 6)]
            [(28, 0), (29, 1), (30, 2), (31, 3), (0, 4), (0, 5), (0, 6)]

            November 2019
            Mo Tu We Th Fr Sa Su
                        1  2  3
            4  5  6  7  8  9 10
            11 12 13 14 15 16 17
            18 19 20 21 22 23 24
            25 26 27 28 29 30

163) Project: LAB: the calendar module

        my code:

            import calendar

            class MyCalendar(calendar.Calendar):
                def count_weekday_in_year(self, year, weekday):
                    data, self.sum  = calendar.Calendar(), 0

                    for month in range(1, 13):
                        for line in data.monthdays2calendar(year, month):
                            if list(line[weekday])[0] != 0: self.sum += 1

                def __str__(self):
                    return str(self.sum)

            object = MyCalendar()
            object.count_weekday_in_year(2000, 6)
            print(object)

        output:

            import calendar

            class MyCalendar(calendar.Calendar):
                def count_weekday_in_year(self, year, weekday):
                    current_month = 1
                    number_of_days = 0
                    while (current_month <= 12):
                        for data in self.monthdays2calendar(year, current_month):
                            if data[weekday][0] != 0:
                                number_of_days = number_of_days + 1

                        current_month = current_month + 1
                    return number_of_days

            my_calendar = MyCalendar()
            number_of_days = my_calendar.count_weekday_in_year(2019, calendar.MONDAY)

            print(number_of_days)



--------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------






1.4.1.18
Where does the name "The Cheese Shop" come from?
    It's a reference to an old Monty Python's sketch of the same name.
Why should I ensure which one of pip and pip3 works for me?
    When Python 2 and Python 3 coexist in your OS, it's likely that pip identifies the instance of pip working with Python 2 packages only.
How can I determine if my pip works with either Python 2 or Python 3?
    pip --version will tell you that.
Unfortunately, I don't have administrative right. What should I do to install a package system-wide?
    You have to ask your sysadmin - don't try to hack your OS!

4.3.1.18
What do we expect from the readlines() method when the stream is associated with an empty file?
    An empty list (a zero-length list).

"""