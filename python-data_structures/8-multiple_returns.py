#!/usr/bin/python3
def multiple_returns(sentence):
    uz = len(sentence)
    if uz == 0:
        return uz, None
    else:
        return uz, sentence[0]
