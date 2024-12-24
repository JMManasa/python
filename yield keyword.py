def print_even(test_list):
    for i in test_list:
        if i%2==0:
            yield i       #return i and come back

test_list=[1,4,5,6,7]

print(test_list)

print("The even numbers in list are: ")
for j in print_even(test_list):     #how many times the func returns values that many times the loop runs
    print(j)
    
