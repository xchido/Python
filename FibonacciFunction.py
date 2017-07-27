#-------------------------------------------------------------------------------
# Name:        Fibonacci Function
# Purpose:
#
# Author:      Jorge
#
# Created:     17/03/2014
# Copyright:   (c) Jorge 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def fibonacci(n):
    terms = [0, 1]
    i = 2
    while i <= n:
        terms.append(terms[i-1]+terms[i-2])
        i = i+1

    return terms[n]

user_input = eval(input("Enter the nth number in the Fibbonacci sequence: "))

answer = fibonacci(user_input)

print (answer)