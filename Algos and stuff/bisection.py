# 1. Bisection method
# 2. method of false position


def disp():
        i = 0
        for i in range(len(deg)):
                print(str(coef[i]) + " * x^" + str(deg[i]) + " + ", end='' )

def enter():
        a = input("Enter degree of 1st term : ")
        deg.append(eval(a))
        a = input("Enter coefficient of 1st term : ")
        coef.append(eval(a))
        while 1:
                a = input("Enter degree of next term : ")
                if a == '':
                        break
                deg.append(eval(a))
                a = input("Enter coefficient of the present term : ")
                coef.append(eval(a))
        print("Your func is : ")
        disp()
        return None

def f(num):
        sum = 0
        i = 0
        for i in range(len(deg)):
                sum += coef[i] * (num ** deg[i])
                i+=1
        return sum

def initialSol():
        x = -100;
        while x<100:
                if (f(x) * f(x+0.5)) < 0 :
                        if f(x) < 0 :
                                return x, x+0.5
                        else :
                                return x+0.5, x
                x=x+0.5


def chk(num1, num2):
        if ( (int(num1*10000000) - int(num2*10000000)) == 0 ):
                return 1
        return 0

def bisection():
        x, y = initialSol()
        # print(x, y)
        while 1 :
                temp = (x+y)/2;
                if(f(temp) == 0):
                        return temp
                elif (f(temp) <  0):
                        if chk(x, temp):
                                return temp
                        x = temp
                else:
                        if chk(y, temp):
                                return temp
                        y = temp

def falPosition():
        x, y = initialSol()
        # print(x, y)
        while 1 :
                temp = (f(y) * x - y * f(x)) / ( f(y) - f(x) );
                if(f(temp) == 0):
                        return temp
                else:
                        if chk(y, temp):
                                return temp
                        y = temp


deg = []
coef = []
enter()
a = bisection()
b = falPosition()
print ("\n%d", a)
print (b)
print(f(a))
print(f(b))