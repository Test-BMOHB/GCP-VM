import python_account_ID
import Python_aba_transit_numbers
from random import randrange
from random import random
import random 
from random import shuffle
from faker import Faker
from barnum import gen_data
import csv
fake = Faker()

ON_US_INDICATOR = ['ON','OFF']
DebitCredit = ['CR','DR']
bank= ['0','8','9']
select = '1' 
#ATM_FLAG = ['1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
ATM_FLAG = ['1','0']
with open('largetrns.csv','w') as f1:
    writer=csv.writer(f1, delimiter=',',lineterminator='\n',)
    writer.writerow(['rownum'] +['TXN_ROUTING_TRANSIT'] + ['DEBIT_CREDIT_INDICATOR'] +['Bank']+ \
	['AccountID'] + ['Amount'] + ['ON_US_INDICATOR'] + \
	['COMPANY_NAME'] + ['DATE_POSTED']+ ['City_State_Zip'] + ['ATM_FLAG'] +['RDCFLAG'])
    for i in range(500):   
		row = [i] +  [random.choice(Python_aba_transit_numbers.aba)] + \
		[DebitCredit[random.randint(0,len(DebitCredit)-1)]] +  \
		[random.choice(bank)] + \
		[random.choice(python_account_ID.accountid)] +  \
		[max ( max((randrange(0,101,1)-99),0)* randrange(20000,500000,1),randrange(5,35000,1))] + \
		[ON_US_INDICATOR[random.randint(0,len(ON_US_INDICATOR)-1)]] + \
		[gen_data.create_company_name()] + \
		[gen_data.create_birthday(min_age=1, max_age=8)] + \
		[gen_data.create_city_state_zip()] + \
		[random.choice(ATM_FLAG)* max((randrange(0,101,1)-99),0)]  +  [random.choice(ATM_FLAG)* max((randrange(0,101,1)-99),0)]
		writer.writerow(row)
