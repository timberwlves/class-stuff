// FILE DECLARATIONS

fileGeraldine as FILE
fileGerard as FILE
fileMerged as FILE


// DECLARATIONS

num customerNumber
string lastName
string customerAddress
num propertySize
num set mergedCustomerNumbers

start

    openRead fileGeraldine 
    openRead fileGerard
    openWrite fileMerged

    
    while not EOF
         read customerNumber, lastName, address, propertySize from fileGeraldine
             if customerNumber not in mergedCustomerNumbers then
                 write customerNumber, lastName, address, propertySize to fileMerged
                 add customerNumber to mergedCustomerNumbers
		else: 
		  close fileGeraldine

             endif
    endwhile
         
        
    while not EOF
        read customerNumber, lastName, address, propertySize from fileGerard
            if customerNumber not in mergedCustomerNumbers then
                write customerNumber, lastName, address, propertySize to fileMerged
                add customerNumber to mergedCustomerNumbers
		
		else: 
		 close fileGerard

            endif
    endwhile



    close fileGeraldine
    close fileGerard
    close fileMerged

stop
    
