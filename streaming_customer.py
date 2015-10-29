#!/usr/bin/env python

# Copyright 2015, Google, Inc.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Command-line application that streams data into BigQuery.
This sample is used on this page:
    https://cloud.google.com/bigquery/streaming-data-into-bigquery
For more information, see the README.md under /bigquery.
"""

import argparse
import ast
import json
import uuid

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
from six.moves import input

from random import randrange
from random import random
from random import shuffle
from faker import Faker
from barnum import gen_data
import csv

# [START stream_row_to_bigquery]
def stream_row_to_bigquery(bigquery, project_id, dataset_id, table_name, row,num_retries=5):
    # Generate a unique row id so retries
    # don't accidentally duplicate insert
	insert_all_data = {'insertId': str(uuid.uuid4()),'rows': [{'json': row}]}
	return bigquery.tabledata().insertAll(projectId=project_id,datasetId=dataset_id,tableId=table_name,body=insert_all_data).execute(num_retries=num_retries)
    # [END stream_row_to_bigquery]

def main(project_id, dataset_id, table_name, num_retries):
    # [START build_service]
    # Grab the application's default credentials from the environment.
    credentials = GoogleCredentials.get_application_default()

    # Construct the service object for interacting with the BigQuery API.
    bigquery = discovery.build('bigquery', 'v2', credentials=credentials)
    # [END build_service]

    for row in get_rows():
		print(row)
		response = stream_row_to_bigquery(
            bigquery, project_id, dataset_id, table_name, row, num_retries)
    print(json.dumps(response))
			
def get_rows():
    i=501
	#line = input("Enter a row (python dict) into the table: ")
    while i < 1000:
		fake = Faker()
		#Pick an account number and store it in acct 
		#if the account hasn't been already generated then generate a record with all fields
		i=i+1	
		line = "{'rownum':"+str(i)+",'dunno':"+str(10)+",'CC':"+str(gen_data.cc_number())+",'Employer':"+str(gen_data.create_company_name())+\
		",'Custemail':"+str(gen_data.create_email())+",'name':"+\
		str(gen_data.create_name())+",'occupation':"+str(gen_data.create_job_title())+",'address_street':"+\
		str(gen_data.create_city_state_zip())+",'DOB':"+str(gen_data.create_birthday(min_age=2, max_age=85))+\
		",'previous_address_city_state_zip':"+str(gen_data.create_city_state_zip())+",'altcustomer_name':"+str(fake.name())+\
		",'altcustomer_occupation':"+str(gen_data.create_job_title())+",'altcustomer_dob':"+str(gen_data.create_birthday(min_age=2, max_age=85))+\
		",'ssn':"+str((randrange(101,1000,1),randrange(10,100,1),randrange(1000,10000,1)))+",'phone':"+\
		str((randrange(101,1000,1),randrange(101,999,1),randrange(1000,10000,1)))+ \
		",'AccountID':"+str(randrange(100000,100000000,1))+",'PepFlag':"+str(max((randrange(0,101,1)-99,0)))+",'altcustomerssn':"+\
		str((randrange(101,1000,1),randrange(10,100,1),randrange(1000,10000,1)))+",'demarketed_customer_flag':"+\
		str(max((randrange(0,101,1)-99),0))+\
		",'SAR_flag':"+str(max((randrange(0,101,1)-99),0))+",'nolonger_a_customer':"+str(max((randrange(0,101,1)-99),0))+\
		",'closed_account'"+str(max((randrange(0,101,1)-90),0))+",'High_risk_flag':"+str(max((randrange(0,101,1)-99),0))+\
		",'Risk_rating':"+str(max((randrange(0,101,1)-99),0))+"}"
        yield ast.literal_eval(line)
        #line = input("Enter another row into the table \n" +
         #            "[hit enter to stop]: ")
					 
# [START main]
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('project_id', help='Your Google Cloud project ID.')
    parser.add_argument('dataset_id', help='A BigQuery dataset ID.')
    parser.add_argument(
        'table_name', help='Name of the table to load data into.')
    parser.add_argument(
        '-p', '--poll_interval',
        help='How often to poll the query for completion (seconds).',
        type=int,
        default=1)
    parser.add_argument(
        '-r', '--num_retries',
        help='Number of times to retry in case of 500 error.',
        type=int,
        default=5)

    args = parser.parse_args()

    main(
        args.project_id,
        args.dataset_id,
        args.table_name,
        args.num_retries)
# [END main]
