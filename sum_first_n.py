####################################

def sum_with_loop(n):
    my_sum = 0
    for i in range(1, n+1):
        my_sum += i
    return my_sum

def sum_with_formula(n):
    my_sum = n*(n+1)/2
    return my_sum

def sum_with_recursion(n):
    if n == 0:
        return 0
    my_sum = sum_with_recursion(n-1) + n
    return my_sum
    
# Main program #
while True:
    n = int(input("Enter a natural number please: "))
    res = sum_with_recursion(n)
    res_loop = sum_with_loop(n)
    res_formula = sum_with_formula(n)
    assert res_loop == res_formula, \
        f'ERROR!!: res_loop = {res_loop} but res_formula == {res_formula}'
    assert res  == res_formula
    print(f'S({n}) = {res_loop}')
    
## Next time ##
## 1. Take care of negative number (lines 14,15) ##
## 2. Take care of max recursion depth ##
##
