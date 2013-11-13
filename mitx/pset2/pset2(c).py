annualInterestRate = 0.2
balance = 320000
monthlyInterestRate = (annualInterestRate) / 12.0

lowerBound = balance / 12
upperBound = lowerBound * ((1 + monthlyInterestRate)**12)
while 1:
	minMonthPayment = ( lowerBound + upperBound ) / 2
	balanceCopy = balance
	for i in range(1,13) :
		unPaid = balanceCopy - minMonthPayment
		balanceCopy = unPaid + monthlyInterestRate * unPaid
	if round(abs(balanceCopy), 3) == 0.001 : #(annualInterestRate * minMonthPayment) :
		break	
	if balanceCopy > 0 :
		lowerBound = minMonthPayment
	else :
		upperBound = minMonthPayment

print "Lowest Payment : ",round(minMonthPayment,2)#, balanceCopy

