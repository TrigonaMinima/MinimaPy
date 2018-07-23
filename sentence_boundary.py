import re


# data = input()
with open("input.txt", "r") as f:
    data = f.readlines()
    data = [i.strip("\n") for i in data][0]


def que_ex(data):
    """
    Handles full sentences in between quotes
    Handles question and exclamation marks as sentence boundaries.
    Does not handle the abbreviations or salutations (Dr./Ms. etc)
    """
    ndata = []
    st = []
    for i in data:
        if i == '"':
            if not st:
                st.append(i)
            else:
                st.pop(-1)
            ndata.append('"')
        else:
            bound = ""
            if st:
                bound = st.pop(-1)

            if not bound:
                if i == ".":
                    ndata.append(".|")
                elif i == "?":
                    ndata.append("?|")
                elif i == "!":
                    ndata.append("!|")
                else:
                    ndata.append(i)
            else:
                ndata.append(i)
                st.append(bound)

    return "".join(ndata)


# def standardise(data):
#     data = re.sub()
# print(data)
# print()
data = que_ex(data)
# print(data)

for i in data.split("|"):
    print(i.strip())
