# 12x12
# 6-10 words
# These words must be placed in the maze, and the remaining spaces in the
# maze should be filled up.

# overload print to print the matrix

sentence = "These words must be placed in the maze, and the remaining spaces in the maze should be filled up"
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def words(sentence):
    for i in "1234567890!@#$%^&*()_+-=;':[]{}\\|/.,<>?`~ "
        sentence = sentence.replace(i, "")

    sentence = sentence.upper()
    return sentence


def generate(sentence):
    matrix = []


if __name__ == "__main__":
    print(generate(words(sentence)))
