# prob4
'''
def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    c = b
    count = 1
    while c <= x:
        c *= b
        count += 1
    return count-1
'''

# prob5
'''
def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    s = ''
    c = min(len(s1), len(s2))
    for i in range(c):
        s += s1[i]
        s += s2[i]
    if len(s1) > len(s2):
        for i in range(c, len(s1)):
            s += s1[i]
    else:
        for i in range(c, len(s2)):
            s += s2[i]
    return s
'''

# prob6
'''
def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return s2
        if s2 == '':
            return s1
        else:
            return out + s1[0] + s2[0] + helpLaceStrings(s1[1:], s2[1:], '')
    return helpLaceStrings(s1, s2, '')
'''

# prob7
'''
def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    val = 0
    for c in range(n/2):
        for b in range(n/2):
            for a in range(n/2):
                val = 20*c + 9*b + 6*a
                if(val == n):
                    return True
    return False
'''

# prob8(a)
'''
def fixedPoint(f, epsilon):
    """
    f: a function of one argument that returns a float
    epsilon: a small float
  
    returns the best guess when that guess is less than epsilon 
    away from f(guess) or after 100 trials, whichever comes first.
    """
    guess = 1.0
    for i in range(100):
        if abs(f(guess) - guess) < epsilon :
            return guess
        else:
            guess = f(guess)
    return guess
'''
