# with an accuracy of 10 decimal places (number < 100000)

def reciprocal(num) :
        if num == 0:
                print ("Indeterminant")
                return none
        x=0.000001;
        while 1 :
                y = x * ( 2 - num * x )
                if ( (int(y*10000000000) - int(x*10000000000)) == 0):
                        return y
                        break
                x = y

a  =  eval(input("Enter the number : "))
print (a)
print (1/a)
print (reciprocal(a))