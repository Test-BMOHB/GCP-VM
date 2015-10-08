#from faker import Faker
import faker
import csv
with open('large.csv','w') as f1:
    writer=csv.writer(f1, delimiter=',',lineterminator='\n',)
    writer.writerow([''] + range(10))
    for i in range(10):
        row = [i] + [10] + fake.name()
        writer.writerow(row)
