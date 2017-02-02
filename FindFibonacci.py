# Program to calculate a Fibonacci number with the use of Memoization in the form of a list that includes all of the
# calculated Fibonacci numbers up to the one being presently calculated

from time import time

def fib(n) :
    if n <= 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        return fib(n - 1) + fib(n - 2)

def allFib(fibnum) :
    print("These are the first", fibnum, "Fibonacci numbers:")
    for i in range(fibnum) :
        print(fib(i), end = " ")
    print()


def fibwithMem(n, memoizedarray) :
    if n <= 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        return fibwithMem(n - 1, memoizedarray) + memoizedarray[n - 2] # calculate the latest fib num and recall the last one from the list

def allFibwithMem(fibnum, memoizedarray) :
    for i in range(fibnum) :
        memoizedarray.append(fibwithMem(i, memoizedarray)) # add the latest calculated fib num to list
    print("These are the first", fibnum, "Fibonacci numbers:")
    print(*memoizedarray, sep = " ") # print the list without brackets or commas, numbers separated by whitespace

def main() :
    memoizedarray = []
    print()
    fibnum = int(input("Enter the maximum number for the Fibonacci calculation: "))
    ans = (input("Would you like to run the calculation with Memoization?: "))
    print()

    if ans == 'Y' or ans == 'y' :
        startTime1 = time()
        allFibwithMem(fibnum, memoizedarray)
        finishTime1 = time()
        print()
        print("The elapsed calculation time utilizing Memoization is %.8f" % (finishTime1 - startTime1),  " seconds.")

    else :
        startTime2 = time()
        allFib(fibnum)
        finishTime2 = time()
        print()
        print("The elapsed calculation time without Memoization is %.8f" % (finishTime2 - startTime2), " seconds.")

main()