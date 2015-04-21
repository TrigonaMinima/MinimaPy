# Write a program to generate a wordmaze for a given set of words. Here is an example of a wordmaze:
# http://www.sugardoodle.net/index.php?option=com_content&view=article&id=6106

# Assume a 12x12 grid and about 6-10 words. These words must be placed in
# the maze, and the remaining spaces in the maze should be filled up.


import re
import random

sentence = "Write a program to generate a wordmaze."
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def display(matrix, endi, endj):
    """
    Displays the matrix in the puzzle format- in a grid, with start and end point.
    """

    if endi == 0:
        print("    " * endj + " End")
        print(" ---" * endj + " | |" + " ---" * (11 - endj))
    else:
        print(" ---" * 12)

    if endj == 11 and endi != 0:
        for i in range(11):
            for j in range(12):
                print("|", matrix[i][j], "", end="")
            if i == endi:
                print("= End\n" + "|---" * 12 + "|")
            else:
                print("|\n" + "|---" * 12 + "|")
    else:
        for i in range(11):
            for j in range(12):
                print("|", matrix[i][j], "", end="")
            print("|\n" + "|---" * 12 + "|")

    for i in range(12):
        print("|", matrix[i][j], "", end="")
    print("|\n" + " | |" + " ---" * 11)

    print("Start")


def words(sentence):
    """
    Takes in the initial sentence and cleans is up.
    Returns the cleaned sentence.
    """
    pattern = r"[^A-Z]"
    p = re.compile(pattern)
    sentence = p.sub("", sentence)

    return sentence


def fill(matrix):
    """
    Fills the remaining spaces in the matrix with random characters.
    Takes matrix as an input.
    """
    for i in range(12):
        for j in range(12):
            if matrix[i][j] == "0":
                matrix[i][j] = random.sample(alphabets, 1)[0]


def mazed(matrix, sentence):
    """
    Takes in matrix and the cleaned sentence and returns the row number and
    column number where the last element of the sentence lands.
    """

    k = 0
    j = 0
    toggle = 0

    while sentence:
        temp = sentence[0:12]
        tempL = len(temp)

        if tempL < (12 - toggle):
            if toggle:
                for k, char in enumerate(temp):
                    matrix[11 - toggle - k][11] = char
                return (11 - toggle - k, 11)
            else:
                for k, char in enumerate(temp):
                    matrix[11 - toggle - k][0] = char
                return (11 - toggle - k, 0)

        elif tempL == 12:
            if not (toggle % 2):
                matrix[11 - toggle] = temp[:]
            else:
                matrix[11 - toggle] = temp[::-1]

        else:
            if toggle:
                for k in range(12 - toggle):
                    matrix[11 - toggle - k][11] = temp[k]
                for j in range(1, tempL - 12 + toggle):
                    matrix[0][11 - j] = temp[j + k]
                return (11 - toggle - k, 11 - j)
            else:
                for k in range(12 - toggle):
                    matrix[11 - toggle - k][0] = temp[k]
                for j in range(1, tempL - 12 + toggle):
                    matrix[0][j] = temp[j + k]
                return (11 - toggle - k, j)

        toggle += 1
        sentence = sentence[12:]

    if toggle % 2:
        return (11 - toggle - k, 0)
    else:
        return (11 - toggle - k, 11)


def generate(sentence):
    """
    Takes the sentence to be encoded in the matrix.
    Returns None.

    Displays the final puzzle matrix with the start and end points displayed.
    """
    if len(sentence) > 12 * 12:
        print("Wordmaze cannot be generated: number of alphabets \
            exceeded 12x12!!")
        return 0

    matrix = [["0"] * 12 for j in range(12)]
    (i, j) = mazed(matrix, sentence)
    # display(matrix, i, j)
    fill(matrix)
    print()
    display(matrix, i, j)


if __name__ == "__main__":
    print("\n")
    generate(words(sentence.upper()))
    print("\n")
