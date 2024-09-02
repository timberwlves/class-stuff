# Pseudocode for a program that determines monthly checking account fee

start


   	accountBalance = 0

        input accountBalance
        input timesOverDrawn

	overDrawnFee = accountBalance * 0.01 - (timesOverDrawn * 5)
	newBalance = overDrawnFee - accountBalance
       
        print (overDrawnFee)
        print (newBalance)
        print ("Thanks for using this program")

stop
