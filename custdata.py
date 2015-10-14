from random import randrange
from faker import Faker
from barnum import gen_data
import csv
fake = Faker()
#gen_data = gen_data()
with open('large.csv','w') as f1:
    writer=csv.writer(f1, delimiter=',',lineterminator='\n',)
    writer.writerow(['rownum'] +['dunno'] + ['CC'] + ['Employer'] + ['Custemail'] + ['name'] \
	+ ['occupation'] + ['address_street'] + ['DOB']+['previous address_city_state_zip']+ ['altcustomer_name'] \
	+ ['altcustomer_occupation']   + ['altcustomer_dob'] + ['ssn'] + ['phone']  + ['AccountID'] + ['PepFlag'] + ['ssn'])
	#writer.writerow([''] + range(10))
    for i in range(50000000):
        row = [i] + [10] + [gen_data.cc_number()]+[gen_data.create_company_name()]  \
		+[gen_data.create_email()]+[gen_data.create_name()] +[gen_data.create_job_title()] + \
		[gen_data.create_city_state_zip()] + [gen_data.create_birthday(min_age=2, max_age=85)] + \
		[gen_data.create_city_state_zip()] + [fake.name()] + [gen_data.create_job_title()] + \
		[gen_data.create_birthday(min_age=2, max_age=85)] + \
		[ gen_data.create_phone() * randrange(0,2,1)  ] +[ gen_data.create_phone()] \
		+ [randrange(100000,100000000,1)] + [max((randrange(0,101,1)-99),0)] + [randrange(100000,100000000,1)]
	writer.writerow(row)
		
		
		
 #row = [i] + [10] + [fake.name()] +[fake.address()]  [gen_data.create_phone() * randrange(0,2,1)   ]
