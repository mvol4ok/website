#!/usr/bin/python3


def ask_question():
    return input("what is the meaning of life?")

answer = ask_question()
while answer != "nothing":
    if answer == "nothing":
        print("you said %s" % answer)
    else:
        print("try again")
    answer = ask_question()

print("loop done!")