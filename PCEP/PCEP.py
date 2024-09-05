"""
بسم الله الرحمان الرحيم
a
------------------------------

1) end="" > To prevent output in next line
    1) Type anything between "" to join 2 lines with that text

2) \n > Next line

3) sep="" > print gives gaps by default
    1) Seperate elements

4) Underscore > Ease in representing numbers
    1) 105_007 Views > Underscores used instead of commas in numbers

5) 0O/0o/zero-o > Octal values start with these prefixes, digits taken from the [0..7] range only

6) 0X/0x/zero-x > Hexadecimal numbers start with these prefixes

7) E/e > Exponent
    1) 3e8 = 3E8 = 3 * 10^8
    2) 3E8 = 300000000.0
    3) 4e2 = 400.0

8) \ > Escape character
    1) print("Me \"Arub\"") = Me "Arub"
    2) print('Me "Arub"') = Me "Arub"
    3) print("Me 'Arub'") = Me 'Arub'

9) +, -, *, /, //, %, ** > Basic Operators
    1) +   > Addition 
    2) -   > Subtraction
    3) *   > Multiplication
    4) /   > Division
        1) 6 / 3 = 2.0
        2) 6 / 3. = 2.0
        3) 6. / 3 = 2.0
        4) 6. / 3. = 2.0

    5) //  > DIV > Integer result
        1) 6 // 3 = 2
        2) 6 // 3. = 2.0
        3) 6. // 3 = 2.0
        4) 6. // 3. = 2.0
        5) 6 // 4 = 1
        6) 6. // 4 = 1.0
        7) Negative Values effect results by rounding as shown below
        8) -6 // 4 = -2 
        9) 6. // -4 = -2.0

    6) %   > Modulo > Remainder
        1) Left sided binding
        2) 9 % 6 % 2 = 1

    7) **  > Exponentiation
        1) 2 ** 3 = 8
        2) 2 ** 3. = 8.0
        3) 2. ** 3 = 8.0
        4) 2. ** 3. = 8.0
        5) Right sided binding

10) A unary operator is an operator with only one operand
    1) -1
    2) +3

11) A binary operator is an operator with two operands
    1) 4 + 5
    2) 12 % 5

12) Variable Names
    1) Upper-case or lower-case letters, digits, and the character _ (underscore)
    2) Begin with a letter
    3) Underscore character is a letter
    4) Upper- and lower-case letters are treated as different
    5) Must not be any of Python's reserved words

13) Invalid Variable Names
    ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class',
     'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for',
     'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
     'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

14) Powers & Incrementation
    1) variable = variable op expression
    2) variable op= expression
        1) x = x * 2               ⇒    x *= 2
        2) x = x + 1               ⇒    x += 1
        3) i = i + 2 * j           ⇒    i += 2 * j
        4) var = var / 2           ⇒    var /= 2
        5) rem = rem % 10          ⇒    rem %= 10
        6) j = j - (i + var + rem) ⇒    j -= (i + var + rem)
        7) x = x ** 2              ⇒    x **= 2

15) Round (Decimal Points)
    1) round(23.834,1) = 23.8
    2) round(23.289405,3) = 23.289

16) CTRL + / > Hash all lines to comment

17) type() > Tells the type of data

18) = > assignment operator

19) == > comparison operator

20) != > not equals to

21) Priority	Operator	
        1	+, -	            unary
        2	**	                unary
        3	*, /, //, %	        unary
        4	+, -	            binary
        5	<, <=, >, >=	    binary
        6	==, !=	            binary
22)  Indentation > 1 Tab click = 4 Space clicks

23) If & Else

24) Elif 

25) max() > Find largest number

26) min() > Find smallest number

27) While loop
    1) while True > Is an infinite or endless loop
    2) Break by CTRL + C or CTRL + BREAK
    3) while number > For e.g number is input, while will stop loop if number = 0

28) For loop

29) Syntactic candy/syntactic sugar > Additions that simply the work

30) break > exits the loop immediately
    1) break - example

        print("The break instruction:")
        for i in range(1, 6):
            if i == 3:
                break
            print("Inside the loop.", i)
        print("Outside the loop.")

31) continue > behaves as if the program has suddenly reached the end of the body
    1) continue - example

        print("\nThe continue instruction:")
        for i in range(1, 6):
            if i == 3:
                continue
            print("Inside the loop.", i)
        print("Outside the loop.")

32) While & Else

33) For & Else

34) Conjuction > and

35) Disjunction > or

36) Logical operators > and, or, not

37) Bitwise operators
        1) & (ampersand) - bitwise conjunction;    AND
                1) & Does a bitwise and, e.g., x & y = 0, which is 0000 0000 in binary
                2) i = 15
                3) j = 22
                4) i:                      00000000000000000000000000001111
                5) j:                      00000000000000000000000000010110
                6) bit = i & j         =   00000000000000000000000000000110    =   6
                7) log = i and j       =   log : True 

        2) | (bar) - bitwise disjunction;          OR
                1) | Does a bitwise or, e.g., x | y = 31, which is 0001 1111 in binary

        3) ~ (tilde) - bitwise negation;           NOT
                1) Does a bitwise not, e.g., ~ x = 240*, which is 1111 0000 in binary
                2) logneg = not i
                3) bitneg = ~i
                4) i	                    00000000000000000000000000001111
                5) bitneg = ~i	            11111111111111111111111111110000
                6) Therefore: i = -16

        4) ^ (caret) - bitwise exclusive or (xor) XOR
                1) ^ Does a bitwise xor, e.g., x ^ y = 31, which is 0001 1111 in binary
		
	SUMMARY (IMPORTANT)
	        In the table below: Let x = 10 (0000 1010 in binary) and y = 4 (0000 0100 in binary)

            Operator	    Meaning	Example
                &	        Bitwise AND	            x & y = 0 (0000 0000)
                |	        Bitwise OR	            x | y = 14 (0000 1110)
                ~	        Bitwise NOT	            ~x = -11 (1111 0101)
                ^	        Bitwise XOR	            x ^ y = 14 (0000 1110)
                >>	        Bitwise right shift	    x >> 2 = 2 (0000 0010)
                <<	        Bitwise left shift	    x << 2 = 40 (0010 1000)

38) Abbreviated form
        x = x & y	x &= y
        x = x | y	x |= y
        x = x ^ y	x ^= y

39) Binary left shift >     <<
        << Does a bitwise left shift, e.g., y << 3 = , which is 1000 0000 in binary
        Shifting a value one bit to the left thus corresponds to multiplying it by two
        17 << 2 = 68

40) Binary right shift >    >>
        >> Does a bitwise right shift, e.g., y >> 1 = 8, which is 0000 1000 in binary
        Shifting one bit to the right is like dividing by two
        17 >> 1 = 8 (Integer Division)

41) Updated priority table
    Priority	Operator	
        1)	~, +, -	unary
        2)	**	
        3)	*, /, //, %	
        4)	+, -	binary
        5)	<<, >>	
        6)	<, <=, >, >=	
        7)	==, !=	
        8)	&	
        9)	|	
        10	=, +=, -=, *=, /=, %=, &=, ^=, |=, >>=, <<=

42) Lists
        1) Consists of elements
        2) Can be scalar

43) Indexing > The operation of selecting an element from the list

44) len() > Length of a list or string

45) del > Deletes elements in a list
        1) If used to delete the entire list, it deletes the list itself, not its content
        2) del my_list[:] >     OUTPUT = []

46) Negative indices
        1) -1 > Last element

47) Functions vs Methods
    1) Function doesn't belong to any data, it gets data, may create new data, then outputs it
       A method does all these things, but is also able to change the internal state of a selected entity

    2)  function is owned by the whole code
       A method is owned by the data it works for

    3) A typical function invocation may look like this
            result = function(arg)
            The function takes an argument, does something, and returns a result
       A typical method invocation usually looks like this:
            result = data.method(arg)
                1) Name of the data which owns the method
                2) Dot
                3) Method name
                4) A pair of parenthesis enclosing the arguments

48) append() > To glue a new element in the end of a list
        1) list.append(value)

49) insert() > To add a new element at any place in the list
        1) list.insert(location, value)

50) Swapping values of 2 variables
        1) Right value is assigned to left, however, both have the same value in the end
        2)  a = 1
            b = 2

            auxiliary = a
            a = b
            b = auxiliary
        3)  An easier method
                a = 1
                b = 2

                a, b = b, a

51) The bubble sort
        1)  On site:
            my_list = [8, 10, 6, 2, 4]  # list to sort
            swapped = True  # It's a little fake, we need it to enter the while loop.

            while swapped:
                swapped = False  # no swaps so far
                for i in range(len(my_list) - 1):
                    if my_list[i] > my_list[i + 1]:
                        swapped = True  # a swap occurred!
                        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

            print(my_list)

        2) Mine:
            list = [2, 4, 1, 5, 9, 11, 3, 93, 24, 82]
            swap = True
            while swap:
                swap = False
                for x in range((len(list) - 1)):
                    if list[x] > list[x + 1]:
                        list[x], list[x + 1] = list[x + 1], list[x]
                        swap = True
            print(list)

52) sort() > To sort elements in a list

53) reverse() > To reverse the elements in a list

54) A variable is the name of it's content
    A lists name is the name of the memory location where the list is stored
        1)  list_1 = [1]
            list_2 = list_1
            list_1[0] = 2
            print(list_2)

            OUTPUT = [2]
        2)  var_1 = 1
            var_2 = var_1
            var_1 = 2
            print(var_2)

            OUTPUT = 1

55) Slices > Copying an entire list or parts of a list

        1)  list[start:end]
            start is the index of the first element included in the slice
            end is the index of the first element not included in the slice

        2)  list[start:end] = list[:end] = list[0:end]
            list[:end] = list[:len(list)]

56) in & not in > Checks if a certain element is in a list and returns boolean

        1)  my_list = [0, 3, 12, 8, 2]

            print(5 in my_list)
            print(5 not in my_list)
            print(12 in my_list)

            OUTPUT = False, True, True

57) List comprehension

        1)  Allows you to create new lists from existing ones in a concise and elegant way
            Created on-the-fly during program execution, and is not described statically

        2) Syntax
            1)  [expression for element in list if conditional]
            2)  for element in list:
                if conditional:
                    expression

        3) Examples
            1) row = [WHITE_PAWN for i in range(8)]
            2) squares = [x ** 2 for x in range(10)]
            3) twos = [2 ** i for i in range(8)]
            4) odds = [x for x in squares if x % 2 != 0]

58) 2D Arrays

        1) A four-column/four-row table - a two dimensional array (4x4)

            table = [[":(", ":)", ":(", ":)"],
                    [":)", ":(", ":)", ":)"],
                    [":(", ":)", ":)", ":("],
                    [":)", ":)", ":)", ":("]]

            print(table)
            print(table[0][0])  # outputs: ':('
            print(table[0][3])  # outputs: ':)'

        2) Example of Chess board
            1)  board = [[EMPTY for i in range(8)] for j in range(8)]
                EQUALS:
                for j in range(8):
                    for i in range(8):
                        EMPTY

            2)  Printing an empty board

                EMPTY = "-"
                ROOK = "ROOK"
                board = []

                for i in range(8):
                    row = [EMPTY for i in range(8)]
                    board.append(row)
                print(board)

            3)  Printing the 4 ROOKS

                EMPTY = "-"
                ROOK = "ROOK"
                board = []

                for i in range(8):
                    row = [EMPTY for i in range(8)]
                    board.append(row)
                
                board[0][0] = ROOK
                board[0][7] = ROOK
                board[7][0] = ROOK
                board[7][7] = ROOK

                print(board)

            4)  To find any element of a two-dimensional list, you have to use two coordinates:

                    1)  A vertical one (row number)
                    2)  A horizontal one (column number)

59) 3D Arrays

        1) Cube - a three-dimensional array (3x3x3)

            cube = [[[':(', 'x', 'x'],
                    [':)', 'x', 'x'],
                    [':(', 'x', 'x']],

                    [[':)', 'x', 'x'],
                    [':(', 'x', 'x'],
                    [':)', 'x', 'x']],

                    [[':(', 'x', 'x'],
                    [':)', 'x', 'x'],
                    [':)', 'x', 'x']]]

            print(cube)
            print(cube[0][0][0])  # outputs: ':('
            print(cube[2][2][0])  # outputs: ':)'

        2) Example of 3 buildings with 15 floors each with 20 rooms on each floor

            1) Assigning all rooms as False (Meaning vacant)
                rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

            2) Now you can book a room for two newlyweds: in the 2nd building, on the 10th floor, room 14:
                rooms[1][9][13] = True

            3) Release the second room on the fifth floor located in the first building:
                rooms[0][4][1] = False

            4) Check if there are any vacancies on the 15th floor of the third building:
                vacency = 0

                for room_number in range(20):
                    if not rooms[2][14][room_number]:
                        vacency += 1

60) Functions
        1) Syntax
            
            def function_name():
                function_body
                    
        2) To run it

            function_name()

        3) Types of functions:
            
            1) Built-in functions
                Example: print()
            
            2) Pre-installed modules

            3) user-defined functions

            4) Lambda functions
            
61) Parameterized functions
        1) Syntax

            def function(parameter):
                ###
            
        2)  Parameters live inside functions (this is their natural environment)
            Arguments exist outside functions, and are carriers of values passed to corresponding parameters

        3)  Example:
                def message(number):
                    print("Enter a number:", number)
                message(534)

                OUTPUTS Enter a number: 534

        4)  Positional parameter passing
                A technique which assigns the ith (first, second, and so on) argument to
                the ith (first, second, and so on) function parameter  

            Example:
                def my_function(a, b, c):
                    print(a, b, c)

                my_function(1, 2, 3)

        5)  Default (predefined) values
                1) Default values are taken into consideration when their corresponding arguments have been omitted

                2) Example:
                    def introduction(first_name, last_name="Smith"):
                        print("Hello, my name is", first_name, last_name)
                    introduction("Arub")
                    introduction("Arub", "Ali")

62) Keyword argument passing (Functions)
        1) The meaning of the argument is dictated by its name, not by its position

        2)  Example:
                def introduction(first_name, last_name):
                    print("Hello, my name is", first_name, last_name)

                introduction(first_name = "James", last_name = "Bond")
                introduction(last_name = "Skywalker", first_name = "Luke")

        3) A non-default argument (c) can not follow a default argument (b=2)!

        4)  Example:
                def add_numbers(a, b=2, c):
                    print(a + b + c)
                add_numbers(a=1, c=3)

                def add_numbers(a, b=2, c=1):
                    print(a + b + c)
                add_numbers(a=1, c=3)


63) return
        1) A python keyword to get functions to return a value

        2) Return without an expression
            1)  When used inside a function, it causes the immediate termination of the function's execution,
                and an instant return (hence the name) to the point of invocation.

            2)  Example:
                    def happy_new_year(wishes = True):
                        print("Three...")
                        print("Two...")
                        print("One...")
                        if not wishes:
                            return
                        
                        print("Happy New Year!")
                    
                ************************************************************************************************
                        When invoked without any arguments:

                            happy_new_year()

                        OUTPUT:

                            Three...
                            Two...
                            One...
                            Happy New Year!

                ************************************************************************************************
                        Providing False as an argument:

                            happy_new_year(False)

                        OUTPUT:

                            Three...
                            Two...
                            One...
                            
        3) Return with an expression
            1)  causes the immediate termination of the function's execution (nothing new compared to the first variant)
                Will evaluate the expression's value and will return (the name once again) it as the function's result
            
            
            2)  Example:
                    def function():
                        return expression

            3)  Example:
                    def boring_function():
                        return 123
                    x = boring_function()

                    print("The boring_function has returned its result. It's:", x)

                    OUTPUT: The boring_function has returned its result. It's: 123

            4)  Example:
                    def boring_function():
                        print("a")
                        return 123

                    print("b")
                    boring_function()
                    print("c")

                    OUTPUT: 
                        b
                        a
                        c

64) None

        1)  There are only two kinds of circumstances when None can be safely used:
                1) when you assign it to a variable (or return it as a function's result)
                2) when you compare it with a variable to diagnose its internal state.

        2)  Example:
                value = None
                if value is None:
                    print("Sorry, you don't carry any value")

        3)  If a function doesn't return a certain value using a return expression clause, it is assumed that it implicitly returns None            

        4)  Example:
                def strange_function(n):
                    if(n % 2 == 0):
                        return True

                strange_function(5)         #OUTPUT: (NOTHING)

                print(strange_function(4))  #OUTPUT: True
                print(strange_function(5))  #OUTPTU: None

65) Lists in Functions

    1) A list can be sent to a function as an argument:

            def num_sum(listx):
            sumx = 0

            for element in listx:
                sumx += element
            return sumx

            print(num_sum([1, 1, 1, 1, 1, 1, 1, 1]))



                

    2) A list can be a function result:

            def strange_list_fun(n):
                strange_list = []
                
                for i in range(0, n):
                    strange_list.insert(0, i)
                
                return strange_list

            print(strange_list_fun(5))

            OUTPUT: [4, 3, 2, 1, 0]

66) Days in a year:
        def is_year_leap(year):
            if year % 400 == 0:
                return True
            elif year % 100 == 0:
                return False
            elif year % 4 == 0:
                return True
            else:
                return False

        def days_in_month(year, month):
            if month in (1, 3, 5, 7, 8, 10, 12):
                return 31
            elif month in (4, 6, 9, 11):
                return 30
            elif month == 2:
                if is_year_leap(year):
                    return 29
                else:
                    return 28

        def day_of_year(year, month, day):
            days = day
            for m in range(1, month):
                days += days_in_month(year, m)
            return days
        print(day_of_year(2000, 12, 31))

67) Prime numbers
        def is_prime(num):
            prime = 0
            if num <= 1:
                return False
            for x in range(1, num + 1):
                check = num % x
                if check == 0:
                    prime += 1
                if prime > 2:
                    return False
            return True

        for i in range(1, 20):
            if is_prime(i + 1):
                    print(i + 1, end=" ")
        print()

68) Liters per 100km to miles per gallons & vice versa
        def liters_100km_to_miles_gallon(liters):   #EU
            y =  62.137119224 / (liters / 3.785411784)
            return y

        def miles_gallon_to_liters_100km(miles):    #US
            y = (3.785411784 / miles) * 62.137119224
            return y


        print(liters_100km_to_miles_gallon(3.9))
        print(liters_100km_to_miles_gallon(7.5))
        print(liters_100km_to_miles_gallon(10.))
        print(miles_gallon_to_liters_100km(60.3))
        print(miles_gallon_to_liters_100km(31.4))
        print(miles_gallon_to_liters_100km(23.5))

69) Functions and Scopes
        1)  Scope > The scope of a name (e.g., a variable name) is the part of a code where the name is properly recognizable 
                A variable existing outside a function has a scope inside the functions' bodies
                Excluding those of them which define a variable of the same name
                It also means that the scope of a variable existing outside a function is supported only when getting its value(reading)
                Assigning a value forces the creation of the function's own variable

        2)  Example:
                def scope_test():
                    x = 123
                scope_test()
                print(x)

            OUTPUT: x aint defined
            
        3)  Example:
                def my_function():
                    print("Do I know that variable?", var)
                var = 1
                my_function()
                print(var)
            
            OUTPUT: DO I know that variable? 1

        4)  Example:
                def my_function():
                    var = 2
                    print("Do I know that variable?", var)
                var = 1
                my_function()
                print(var)
                
            OUTPUT: Do I know that variable? 2
                    1
        
70) global > Extends a variable's scope in a way which includes the functions' bodies
        
        1)  Example:
                def my_function():
                    global var
                    var = 2
                    print("Do I know that variable?", var)
                var = 1
                my_function()
                print(var)
        
            OUTPUT: Do I know that variable? 2
                    2
71) A function receives the argument's value, not the argument itself
        1)  Example:
                def my_function(my_list_1):
                    print("Print #1:", my_list_1)
                    print("Print #2:", my_list_2)
                    my_list_1 = [0, 1]
                    print("Print #3:", my_list_1)
                    print("Print #4:", my_list_2)
                my_list_2 = [2, 3]
                my_function(my_list_2)
                print("Print #5:", my_list_2)
        
            OUTPUT: Print #1: [2, 3]
                    Print #2: [2, 3]
                    Print #3: [0, 1]
                    Print #4: [2, 3]
                    Print #5: [2, 3]
        
        2)  Example:
                def my_function(my_list_1):
                    print("Print #1:", my_list_1)
                    print("Print #2:", my_list_2)
                    del my_list_1[0]  # Pay attention to this line.
                    print("Print #3:", my_list_1)
                    print("Print #4:", my_list_2)
                my_list_2 = [2, 3]
                my_function(my_list_2)
                print("Print #5:", my_list_2)
        
            OUTPUT: Print #1: [2, 3]
                    Print #2: [2, 3]
                    Print #3: [3]
                    Print #4: [3]
                    Print #5: [3]
        
72) Evaluating BMI

        def ft_and_inch_to_m(ft, inch = 0.0):
            return ft * 0.3048 + inch * 0.0254


        def lb_to_kg(lb):
            return lb * 0.45359237


        def bmi(weight, height):
            if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
                return None
            
            return weight / height ** 2


        print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))
            
73) Backslash(\) > To continue the line of code in the next line of code

74) Can three sides of given lengths build a triangle?
    (The sum of the lengths of any two sides of a triangle must always be greater than the length of the remaining side)

        Program 1:

            def is_a_triangle(a, b, c):
                if a + b <= c:
                    return False
                if b + c <= a:
                    return False
                if c + a <= b:
                    return False
                return True

        Program 2:

            def is_a_triangle(a, b, c):
                if a + b <= c or b + c <= a or c + a <= b:
                    return False
                return True
                
        Program 3:

            def is_a_triangle(a, b, c):
                return a + b > c and b + c > a and c + a > b
        
75) Pythagorean theorem:

        def is_a_triangle(a, b, c):
            return a + b > c and b + c > a and c + a > b


        def is_a_right_triangle(a, b, c):
            if not is_a_triangle(a, b, c):
                return False
            if c > a and c > b:
                return c ** 2 == a ** 2 + b ** 2
            if a > b and a > c:
                return a ** 2 == b ** 2 + c ** 2


        print(is_a_right_triangle(5, 3, 4))
        print(is_a_right_triangle(1, 3, 4))
        
76) A triangle's area (Heron's formula)

        def is_a_triangle(a, b, c):
            return a + b > c and b + c > a and c + a > b


        def heron(a, b, c):
            p = (a + b + c) / 2
            return (p * (p - a) * (p - b) * (p - c)) ** 0.5


        def area_of_triangle(a, b, c):
            if not is_a_triangle(a, b, c):
                return None
            return heron(a, b, c)


        print(area_of_triangle(1., 1., 2. ** .5))
        
77) Factorials
        
        def factorial_function(n):
            if n < 0:
                return None
            if n < 2:
                return 1
            
            product = 1
            for i in range(2, n + 1):
                product *= i
            return product


        for n in range(1, 6):  # testing
            print(n, factorial_function(n))

78) Fibonacci numbers
        (Fibi = Fibi-1 + Fibi-2)
        fib_1 = 1
        fib_2 = 1
        fib_3 = 1 + 1 = 2
        fib_4 = 1 + 2 = 3
        fib_5 = 2 + 3 = 5
        fib_6 = 3 + 5 = 8
        fib_7 = 5 + 8 = 13

        def fib(n):
            if n < 1:
                return None
            if n < 3:
                return 1

            elem_1 = elem_2 = 1
            the_sum = 0
            for i in range(3, n + 1):
                the_sum = elem_1 + elem_2
                elem_1, elem_2 = elem_2, the_sum
            return the_sum


        for n in range(1, 10):  # testing
            print(n, "->", fib(n))

79) Recursion
        A technique where a function invokes itself

        1)  Factorials
                def factorial_function(n):
                    if n < 0:
                        return None
                    if n < 2:
                        return 1
                    return n * factorial_function(n - 1)

            *** Negative factorials (By me, not tested!)

                    def factorial_function(n):
                        if n == 0:
                            return 1
                        return n * factorial_function(n + 1)

                    print(factorial_function(-5))

        2)  Fibonacci numbers
                def fib(n):
                    if n < 1:
                        return None
                    if n < 3:
                        return 1
                    return fib(n - 1) + fib(n - 2)

80) Sequence
        Data which can be scanned by the for loop

81) Mutability
        1) Mutable
            Mutable data can be freely updated at any time
                E.g list.append(1)

        2) Immutable
            Immutable data cannot be modified in this way
            These are tuples

82) Tuples
        1) An immutable sequence type
        2) Prefer to use parenthesis
        3) Also possible to create a tuple just from a set of values separated by commas


            tuple_1 = (1, 2, 4, 8)
            tuple_2 = 1., .5, .25, .125

            print(tuple_1)
            print(tuple_2)

                This is what you should see in the console:

                (1, 2, 4, 8)
                (1.0, 0.5, 0.25, 0.125)

        4) Each tuple element may be of a different type (floating-point, integer, or any other not-as-yet-introduced kind of data)
        5) Empty tuple
            1) A pair of empty parenthesis
                empty_tuple = ()

        6) One-element tuple
            1) The value must end with a comma due to syntax reasons
            2) Otherwise it'll be a variable instead of a tuple

                one_element_tuple_1 = (1, )
                one_element_tuple_2 = 1.,

        7) How to use a tuple

                my_tuple = (1, 10, 100, 1000)

                print(my_tuple[0])
                print(my_tuple[-1])
                print(my_tuple[1:])
                print(my_tuple[:-2])

                for elem in my_tuple:
                    print(elem)
        
        8) All these are not valid and will give an error

                my_tuple = (1, 10, 100, 1000)

                my_tuple.append(10000)
                del my_tuple[0]
                my_tuple[1] = -10

        9) All these are allowed:
            1) +
            2) *
            3) len
            4) in
            5) not in


                my_tuple = (1, 10, 100)

                t1 = my_tuple + (1000, 10000)
                t2 = my_tuple * 3

                print(len(t2))
                print(t1)
                print(t2)
                print(10 in my_tuple)
                print(-10 not in my_tuple)

        10) A tuples elements can be variables
            1) Values stored "circulate". t1 becomes t2, t2 becomes t3 and t3 becomes t1

                var = 123

                t1 = (1, )
                t2 = (2, )
                t3 = (3, var)

                t1, t2, t3 = t2, t3, t1

                print(t1, t2, t3)

        11) tuple() > Create a tuple / Convert a data type to a tuple

        12) Unpacking of a tuple:

                tup = 1, 2, 3
                a, b, c = tup
                print(a * b * c)

            OUTPUT:

                6

83) Dictonaries
        1) A data strcutre, not a sequence
        2) Mutable
        3) The word you look for is named a key
        4) The word you get from the dictionary is called a value
        5) Bilingual
        6) Key must be unique
        7) Key may be any immutable type of object
        8) len() in dictionaries returns the numbers of key-value elements in the dictionary
        9) A one-way tool (value from keys, not keys from values)

                dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
                phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
                empty_dictionary = {}

                print(dictionary)
                print(phone_numbers)
                print(empty_dictionary)
            
        10) Hanging indent:

                dictionary = {
                            "cat": "chat",
                            "dog": "chien",
                            "horse": "cheval"
                            }

                phone_numbers = {'boss': 5551234567,
                                'Suzy': 22657854310
                                }

        11) list() > Create a list / Convert a data type to a list

        12) keys() > Returns an iterable object consisting of all the keys gathered within the dictionary
                
                        dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
                        for key in dictionary.keys():
                            print(key, "->", dictionary[key])

                    OUTPUT:

                        horse -> cheval
                        dog -> chien
                        cat -> chat

        13) sorted() > To sort the output 

                        for key in sorted(dictionary.keys()):
                        
                        (I think its already sorted hmm)

        14) items() > Returns tuples where each tuple is a key-value pair

                        dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
                        for english, french in dictionary.items():
                            print(english, "->", french)

                    OUTPUT:

                        cat -> chat
                        dog -> chien
                        horse -> cheval
                
        15) values() > Returns values

                        dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
                        for french in dictionary.values():
                            print(french)

                    OUTPUT:

                        cheval
                        chien
                        chat
            
        16) Modifying and adding values to dictionaries
                1) Fully mutable
                2) 
                        dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
                        dictionary['cat'] = 'minou'
                        print(dictionary)

                    OUTPUT:

                        {'cat': 'minou', 'dog': 'chien', 'horse': 'cheval'}

                3) Adding a new key
                        Assign a value to a new, previously non-existent key

                            dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
                            dictionary['swan'] = 'cygne'
                            print(dictionary)

                        OUTPUT:

                            {'cat': 'chat', 'dog': 'chien', 'horse': 'cheval', 'swan': 'cygne'}

                4) update() > You can also insert an item to a dictionary

                            dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
                            dictionary.update({"duck": "canard"})
                            print(dictionary)

                        OUTPUT: 

                            {'cat': 'chat', 'dog': 'chien', 'horse': 'cheval', 'duck': 'canard'}

                5) del > Removing a key
                            
                            dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
                            del dictionary['dog']
                            print(dictionary)

                        OUTPUT:

                            {'cat': 'chat', 'horse': 'cheval'}

                6) clear() > Remove all the dictionary's items, NOT THE DICTIONARY!

                7) popitem() > To remove the last item in a dictionary

                            dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
                            dictionary.popitem()
                            print(dictionary)
                            
                        OUTPUT:
                            
                            {'cat': 'chat', 'dog': 'chien'}

                8) Average score of each student

                            school_class = {}

                            while True:
                                name = input("Enter the student's name: ")
                                if name == '':
                                    break
                                
                                score = int(input("Enter the student's score (0-10): "))
                                if score not in range(0, 11):
                                    break
                                
                                if name in school_class:
                                    school_class[name] += (score,)
                                else:
                                    school_class[name] = (score,)
                                    
                            for name in sorted(school_class.keys()):
                                adding = 0
                                counter = 0
                                for score in school_class[name]:
                                    adding += score
                                    counter += 1
                                print(name, ":", adding / counter)

                9) get() > Get the value of a kwy from a dictionary

                            dict = {
                                "a" : "1",
                                "b" : "2"
                            }

                            item = dict.get("a")
                            print(item)

                        OUTPUT:

                            1

                10) copy() > Copy a dictionary

84) Exceptions
        1) is > Check if a value is of a specific data type
                type(value) is int > True/False
        2) Try-Except
                1) An exception is raised
                2) The try keyword marks the place where you try to do something without permission
                3) The except keyword starts a location where you can show off your apology talents

                    try:
                        value = int(input('Enter a natural number: '))
                        print('The reciprocal of', value, 'is', 1/value)        
                    except:
                        print('I do not know what to do.')    
                
                4) Two exceptions after one try
                    Only one of all branches can intercept the control - if one of the branches is executed,
                    all the other branches remain idle

                        try:
                            value = int(input('Enter a natural number: '))
                            print('The reciprocal of', value, 'is', 1/value)        
                        except ValueError:
                            print('I do not know what to do.')    
                        except ZeroDivisionError:
                            print('Division by zero is not allowed in our Universe.')

                5) The default exception
                    1) Last one
                    2) Should only be "except:"
                    3) Aka the default or generic exception

                        try:
                            value = int(input('Enter a natural number: '))
                            print('The reciprocal of', value, 'is', 1/value)        
                        except ValueError:
                            print('I do not know what to do.')    
                        except ZeroDivisionError:
                            print('Division by zero is not allowed in our Universe.')    
                        except:
                            print('Something strange has happened here... Sorry!')

                6)  Specify and handle multiple built-in exceptions within a single except clause

                        while True:
                            try:
                                number = int(input("Enter an int number: "))
                                print(5/number)
                                break
                            except (ValueError, ZeroDivisionError):
                                print("Wrong value or No division by zero rule broken.")
                            except:
                                print("Sorry, something went wrong...")

        3) Some useful exceptions
            1) ZeroDivisionError > Division in which the divider is zero
            2) ValueError > When a function like int() or str() recieves an unnaceptable value
            3) TypeError > When type of dadta is used which can't be accepted in the context

                    short_list = [1]
                    one_value = short_list[0.5]

            4) AttributeError > When a method which doesn't exist in an item is used

                    short_list = [1]
                    short_list.append(2)
                    short_list.depend(3)

                (Nothing known as depend)

            5) SyntaxError > Wrong syntax or errors in syntax/grammer of the python code
            6) KeyboardInterrupt > When the user hits the interrupt key (CTRL-C or Delete)

85) Bugs
    1) A debugger is used against a bug
    2) Debugging > The process during which bugs are removed from the code
    3) Using a debugger:
        1) The code can be executed line by line
        2) Variables' states can be inspected and values can be changed without modifying the source code
        3) Stop program execution when certain conditions are or aren't met
    4) Interactive debugging > Needs the developers interaction to be performed
        1)  print debugging 
                Insert several additional print() invocations inside your code to
                output data which illustrates the path your code is currently negotiating

86) Project: Tic Tac toe
"""



#Initial board
board = [
            ["1", "2", "3"],
            ["4", "X", "6"], 
            ["7", "8", "9"]
        ]

#User friendly row & column index
row = 0
column = 1

row -= 1
column -= 1

#Importing random library for computer's move
from random import randrange
#print(board[0][1])






def display_board(board):
    for x in range(3):
        print(board[x])




def enter_move(board):
    #User move
    user_move = str(input("Where would you spot an 'O'?   "))
    for row in range(3):
        for column in range(3):
            if user_move == board[row][column]:
                board[row][column] = "O"
    
    #Display board
    for x in range(3):
        print(board[x])






""""""

def make_list_of_free_fields(board):
    free_fields = []
    for row in range(3):
        for column in range(3):
            if board[row][column] != "O" and board[row][column] != "X":
                free_fields.append((row, column))
    print(free_fields)

    #Computer move
    computer_move_done = True
    while computer_move_done:
        computer_move_column = randrange(0, 3)
        computer_move_row = randrange(0, 3)
        computer_move_coordinates = (computer_move_column, computer_move_row)
        if computer_move_coordinates in free_fields and board[computer_move_row][computer_move_column] != "O":
            board[computer_move_row][computer_move_column] = "X"
            computer_move_done = False
    


    #Display board
    for x in range(3):
        print(board[x])






def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    sign = False
    for x in range(3):
        if board[x] == sign:
            sign = True
            print("True")
            return sign
            
            



display_board(board)
enter_move(board)
make_list_of_free_fields(board)
print()
display_board(board)
enter_move(board)
make_list_of_free_fields(board)
print(victory_for(board, "X"))
print()
display_board(board)
enter_move(board)
make_list_of_free_fields(board)
print(victory_for(board, "X"))
print()
display_board(board)
enter_move(board)
make_list_of_free_fields(board)
print(victory_for(board, "X"))
print()
display_board(board)
enter_move(board)
make_list_of_free_fields(board)
print(victory_for(board, "X"))
print()
display_board(board)
enter_move(board)
make_list_of_free_fields(board)
print(victory_for(board, "X"))
print()
"""
def draw_move(board):
    # The function draws the computer's move and updates the board.
"""
from random import randrange


def display_board(board):
	print("+-------" * 3,"+", sep="")
	for row in range(3):
		print("|       " * 3,"|", sep="")
		for col in range(3):
			print("|   " + str(board[row][col]) + "   ", end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")


def enter_move(board):
	ok = False	# fake assumption - we need it to enter the loop
	while not ok:
		move = input("Enter your move: ") 
		ok = len(move) == 1 and move >= '1' and move <= '9' # is user's input valid?
		if not ok:
			print("Bad move - repeat your input!") # no, it isn't - do the input again
			continue
		move = int(move) - 1 	# cell's number from 0 to 8
		row = move // 3 	# cell's row
		col = move % 3		# cell's column
		sign = board[row][col]	# check the selected square
		ok = sign not in ['O','X'] 
		if not ok:	# it's occupied - to the input again
			print("Field already occupied - repeat your input!")
			continue
	board[row][col] = 'O' 	# set '0' at the selected square


def make_list_of_free_fields(board):
	free = []	# the list is empty initially
	for row in range(3): # iterate through rows
		for col in range(3): # iterate through columns
			if board[row][col] not in ['O','X']: # is the cell free?
				free.append((row,col)) # yes, it is - append new tuple to the list
	return free


def victory_for(board,sgn):
	if sgn == "X":	# are we looking for X?
		who = 'me'	# yes - it's computer's side
	elif sgn == "O": # ... or for O?
		who = 'you'	# yes - it's our side
	else:
		who = None	# we should not fall here!
	cross1 = cross2 = True  # for diagonals
	for rc in range(3):
		if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:	# check row rc
			return who
		if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn: # check column rc
			return who
		if board[rc][rc] != sgn: # check 1st diagonal
			cross1 = False
		if board[2 - rc][2 - rc] != sgn: # check 2nd diagonal
			cross2 = False
	if cross1 or cross2:
		return who
	return None


def draw_move(board):
	free = make_list_of_free_fields(board) # make a list of free fields
	cnt = len(free)
	if cnt > 0:	# if the list is not empty, choose a place for 'X' and set it
		this = randrange(cnt)
		row, col = free[this]
		board[row][col] = 'X'


board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] # make an empty board
board[1][1] = 'X' # set first 'X' in the middle
free = make_list_of_free_fields(board)
human_turn = True # which turn is it now?
while len(free):
	display_board(board)
	if human_turn:
		enter_move(board)
		victor = victory_for(board,'O')
	else:	
		draw_move(board)
		victor = victory_for(board,'X')
	if victor != None:
		break
	human_turn = not human_turn		
	free = make_list_of_free_fields(board)

display_board(board)
if victor == 'you':
	print("You won!")
elif victor == 'me':
	print("I won")
else:
	print("Tie!")
