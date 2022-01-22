####################################

def sum_with_loop(n):
    my_sum = 0
    for i in range(1, n+1):
        my_sum += i
    return my_sum

# Main program #
while True:
    n = int(input("Enter a natural number please: "))
    res = sum_with_loop(n)
    print(f'S({n}) = {res}')
