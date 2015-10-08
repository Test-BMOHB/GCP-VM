from barnum import gen_data
import csv
#gen_data = gen_data()
with open('large.csv','w') as f1:
    writer=csv.writer(f1, delimiter=',',lineterminator='\n',)
    writer.writerow([''] + range(10))
    for i in range(100000):
        row = [i] + [10] + [gen_data.cc_number()]+[gen_data.create_company_name()] +[gen_data.create_email()]+[gen_data.create_name()] +[gen_data.create_job_title()] + [gen_data.create_city_state_zip()] + [gen_data.create_birthday(min_age=2, max_age=85)]
        writer.writerow(row)
		
		
		
 #row = [i] + [10] + [fake.name()] +[fake.address()]
