# program to identify fibonacci numbers from a list of numbers

def fib1(A):
    output = []
    max_num = 50
    fib_list = [0,1]
    i = 0
    while len(fib_list)<max_num:
        fib_list.append(fib_list[i]+fib_list[i+1])
        i += 1
    for num in A:
        if num in fib_list:
            output.append(num)
    return output