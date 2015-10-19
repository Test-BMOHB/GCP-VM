
from random import randrange
from random import random
from random import shuffle
from faker import Faker
from barnum import gen_data
import csv
fake = Faker()
#items = [gen_data.create_email(),gen_data.create_name(),gen_data.create_job_title()]
#gen_data = gen_data()
with open('large.csv','w') as f1:
    writer=csv.writer(f1, delimiter=',',lineterminator='\n',)
    writer.writerow(['rownum'] +['dunno'] + ['CC'] + ['Employer'] + ['Custemail'] + ['name'] \
	+ ['occupation'] + ['address_street'] + ['DOB']+['previous address_city_state_zip']+ ['altcustomer_name'] \
	+ ['altcustomer_occupation']   + ['altcustomer_dob'] + ['ssn'] + ['phone']  + \
	['AccountID'] + ['PepFlag'] + ['altcustomerssn'] + ['demarketed_customer_flag'] + \
	['SAR_flag'] + ['nolonger_a_customer'] + ['closed_account'] \
	+ ['occupation_and_rating'] + ['occupation_and_rating2'] + ['randomshuffle'])
	#writer.writerow([''] + range(10))
    for i in range(50000000):
	items = [(randrange(101,1000,1),randrange(10,100,1),randrange(1000,10000,1)),gen_data.create_city_state_zip(),gen_data.create_email(),gen_data.create_name() , gen_data.create_job_title(),gen_data.create_birthday(min_age=2, max_age=85),',','!','@','$',max((randrange(0,101,1)-99),0),',']
	occupationratings = [randrange(0,100,1),',',',,','\/', randrange(0,100,1)-99,gen_data.create_job_title()]
        row = [i] + [10] + [gen_data.cc_number()]+[gen_data.create_company_name()]  \
		+[gen_data.create_email()]+[gen_data.create_name()] +[gen_data.create_job_title()] + \
		[gen_data.create_city_state_zip()] + [gen_data.create_birthday(min_age=2, max_age=85)] + \
		[gen_data.create_city_state_zip()] + [fake.name()] + [gen_data.create_job_title()] + \
		[gen_data.create_birthday(min_age=2, max_age=85)] + \
		[ max( gen_data.create_phone() * randrange(0,2,1) ,(randrange(101,1000,1),randrange(10,100,1),randrange(1000,10000,1))* randrange(0,2,1) ) ] \
		+[ gen_data.create_phone()] \
		+ [randrange(100000,100000000,1)] + \
		[max((randrange(0,101,1)-99),0)] + \
		[(randrange(101,1000,1),randrange(10,100,1),randrange(1000,10000,1))]\
		+[max((randrange(0,101,1)-99),0)]+[max((randrange(0,101,1)-99),0)] +[max((randrange(0,101,1)-99),0)] \
		+[items] + [shuffle(items)] +[occupationratings] \
		+[shuffle(occupationratings)] 
	writer.writerow(row)
		
		
		
 #row = [i] + [10] + [fake.name()] +[fake.address()]  [gen_data.create_phone() * randrange(0,2,1)   ]
