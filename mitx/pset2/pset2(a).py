annualInterestRate = 0.2
monthlyPaymentRate = 0.04
balance = 4842
monthlyInterestRate = (annualInterestRate) / 12.0

total = 0
for i in range(1,13):
	print "Month : ",i
	minMonthPayment = monthlyPaymentRate * balance
	print "Minimum monthly payment : ",round(minMonthPayment, 2)
	unPaid = balance - minMonthPayment
	balance = unPaid + unPaid * monthlyInterestRate
	print "Remaining balance : ",round(balance,2)
	total = total + minMonthPayment

print "Total paid : ",round(total,2)
print "Remaining balance : ",round(balance,2)
