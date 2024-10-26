s ='eNter the String:'
print(F"Length of the String = {len(s)}")
print(F"String in Uppercase = {s.upper()}")
print(F"String in Lowercase = {s.lower()}")
print(F"Capitalized String = {s.capitalize()}")
print("String is :",s)
print(F"Number of time 'n' occurs = {s.count('n')}")        #str.count(character, start, end)
print(F"Number of time 'e' occurs = {s.count('e')}")
print(F"Number of time 'the' occurs = {s.count('the')}")
print(F"Number of time 't' occurs = {s.count('t', 1, 10)}")
print(F"Starts with 'S' = {s.startswith('S')}")                 # str.startswith(starting_char, start, end)
print(F"Ends with 'ing' = {s.endswith('ing',0,16)}")                     # str.endswith(ending_char, start, end)
print(F"Finding 'S' = {s.find('S')}")                           #if chr is not present, it returns -1
print(F"Index of 'S' = {s.index('S')}")           #If the substring is not present --> it will generate an ERROR
print(F"finding last 't' = {s.rfind('t')}")  #If the substring is present multiple times: it will return the index of the LAST Occurrence
print(F"index last 't' = {s.rindex('t')}")      #If the substring is present multiple times: it will return the index of the LAST Occurrence
print("Modified String: " , s.title())
L = ['P', 'Y', 'T', 'H', 'O', 'N']
t1 = '*'.join(L)
print("String:" , t1)
print(s.center(21, '*'))            #21 is length of string which we want and extra length is filled with *
print(s.center(50))                 #2nd argument is optional, default value is space
string = 'Python'
width = 30
char='*'
print(string.rjust(width,char))
print(string.ljust(width,char))
print("Flipped Case = ", s.swapcase())
s1 = "Python                                      "
s1 = s1.rstrip()
print("String =", s1)
s1 = "                            Python"
s1 = s1.lstrip()
print("String =", s1)
s1 = "                            Python                           "
s1 = s1.strip()
print("String =", s1)
temp = s.replace('e', 'E')
print("Modified String: " , temp)
L = s.split('-')
print("List of String: " , L)
a = "abc123"
print("String: " , a)
print("Minimum = ", min(a))             #according to ASCII value
print("Maximum = ", max(a))             #according to ASCII value
'''
26. isalpha()         It checks whether the string is an alphabet or not
27. isdigit()           It checks whether the string is a digit or not
28. isidentifier()   It checks whether the string is an valid identifier or not. (Remember the rules of an identifier)
29. isprintable()   It checks whether the string is a printable character or not
30. isspace()        It checks whether the string consist of whitespaces
31. istitle()            It checks whether the string is in title case or not
32. isupper()         It checks whether the string is in uppercase or not
33. islower()          It checks whether the string is in lowercase or not
34. isnumeric()
35. isdecimal()
'''
