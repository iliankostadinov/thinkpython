#!/usr/bin/env python3

'''
 Write a function called eval_loop that iteratively prompts the user,
 takes the resultin input and evaluates it using eval, and prints  the result
'''


def eval_loop():
    while True:
        user_input = input("Please enter string for evaluation or done if \
you want to finish\n")
        if user_input != "done":
            result = eval(user_input)
            print(result)
        if user_input == "done":
            print(result)
            break


eval_loop()
