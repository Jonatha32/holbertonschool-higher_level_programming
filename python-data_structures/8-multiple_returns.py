#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    if sentence == "":
        return (a, None)
    else:
        return (a, sentence[0])
