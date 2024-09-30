declare variables
baseFee = 5
taxRate = 0.14
sentinel value = 0

start



Display "Please enter 3-digit area code"

input areaCode

while true:

Display "Please input 7 digit phone number and amount of texts sent."

input phoneNumber and textAmount


 if phoneNumber = sentinelValue then
    quit program
            
 endif
       

# Calculations

     if textAmount > 400 then
        additionalFee = (textAmount - 400) * 0.02

     else if textAmount > 300 then
        additionalFee = (textAmount - 300) * 0.03

     else
        additionalFee = 0

     endif

totalBill = baseFee + additionalFee
taxedTotalBill = totalBill + (totalBill * taxRate)

    if taxedTotalBill > 10 then
        display "Phone Number: ", phoneNumber
        display "Total Bill (including tax): $ ", taxedTotalBill
    endif

endwhile

stop
