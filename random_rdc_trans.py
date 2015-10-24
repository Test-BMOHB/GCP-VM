from random import randrange
import csv
with open('large_rdc.csv','w') as f1:
    writer=csv.writer(f1, delimiter=',',lineterminator='\n',)
    writer.writerow(['IP'] + range(10))
    for i in range(1000000):
        countrycode = randrange(0,277,1)
        customerid = randrange(0,999999,1)
        amount = randrange(0,10000,1)
        accountid = randrange(100000,100000000,1)
        row = [i] + [ str(countrycode) +':' + str(customerid) + str(amount) + ':' + str(accountid)] 
        writer.writerow(row)
		
		
		
