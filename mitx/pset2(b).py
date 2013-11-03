annualInterestRate = 0.15
balance = 378498
monthlyInterestRate = (annualInterestRate) / 12.0

minMonthPayment = 10
while 1:
	balanceCopy = balance
	for i in range(1,13):
		unPaid = balanceCopy - minMonthPayment
		balanceCopy = unPaid + monthlyInterestRate * unPaid
	if balanceCopy > 0 :#(annualInterestRate * minMonthPayment) :
		minMonthPayment = minMonthPayment + 0.01
	else :
		break


print "Lowest Payment : ",minMonthPayment, balanceCopy

