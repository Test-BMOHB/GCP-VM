from faker import Faker
import csv
fake = Faker()
with open('large.csv','w') as f1:
    writer=csv.writer(f1, delimiter=',',lineterminator='\n',)
    writer.writerow([''] + range(100))
    for i in range(100):
        row = [i] + [10] + [fake.name()] +[fake.address()]
        writer.writerow(row)
