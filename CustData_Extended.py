from random import randrange
from random import random
from random import shuffle
from faker import Faker
from barnum import gen_data
import csv
import python_account_ID
import NAICS 
import random 




Related_Type = ['Primary','Secondary','Joint']
Party_Type = ['Person','Non-Person']
Party_Relation = ['Customer','Non-Customer']
Yes_No = ['Yes','No','No','No','No','No','No','No','No','No','No'] 
Yes_No_Consent = ['Yes','No','No','No','No']
Yes_No_50 = ['Yes','No']
Official_Lang = ['English','English','English','French']
Preffered_Channel = ['Direct Mail','Telemarketing','Email','SMS']
Primary_Branch = ['00CHi','01CHi','02CHi','2343L','0122S','001To','002To','003To','004To']
Customer_Status = ['Prospect','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Active Customer','Inactive Customer','Past Customer']
Seg_Model_Type = ['LOB Specific','Profitability','Geographical','Behavioral','Risk Tolerance']
Model_ID = ['01','02','03','04','05']
Seg_Model_Name = ['IRRI', 'CRS Risk Score','Geo Risk','Financial Behavior Risk','CM Risk']
Seg_Model_Score = ['200','300','400','100','500']
Seg_Model_Group = ['Group 1','Group 1','Group 2','Group 3','Group 4']
Seg_Model_Description = ['High Risk Tier','Mid Risk Tier','Low Risk Tier','Vertical Risk','Geographical Risk']

Arms_Manufacturer=['Yes','No','No','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
Auction=['Yes','No','No','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
CashIntensive_Business=['Yes','No','No','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
Casino_Gambling=['Yes','No','No','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
Channel_Onboarding=['E-mail','In Person','In person - In Branch/Bank Office','In person - Offsite/Client Location','Mail', \
					'Not Applicable','Not Applicable','Not Applicable','Not Applicable','Not Applicable','Not Applicable','Not Applicable',\
					'Not Applicable','Not Applicable','Not Applicable','Online','Phone',\
					'Request for Proposal (RFP)']
Channel_Ongoing_Transactions=['ATM','E-mail','Fax','In Person','In Person','In Person','In Person',\
							'In Person','In Person','In Person','In Person','In Person','In Person','In Person',\
							'In Person','In Person','In Person','In Person','In Person','In Person','In Person','In Person',\
							'In Person','In Person','In Person','In Person','In Person','In Person','In Person','In Person','In Person','In Person',\
							'In Person','In Person','Mail','Not Applicable','Online','Online','Online','Online','OTC Communication System','Phone',]

Complex_HI_Vehicle=['Yes','No','No','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
Dealer_Precious_Metal=['Yes','No','No','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
Digital_PM_Operator=['Yes','No','No','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
Embassy_Consulate=['Yes','No','No','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
Exchange_Currency=Embassy_Consulate
Foreign_Financial_Institution=Embassy_Consulate
Foreign_Government=Embassy_Consulate
Foreign_NonBank_Financial_Institution=Embassy_Consulate
Internet_Gambling=Embassy_Consulate
Medical_Marijuana_Dispensary=Embassy_Consulate
Money_Service_Business=Embassy_Consulate

NonRegulated_Financial_Institution=Embassy_Consulate
Not_Profit=Embassy_Consulate
Occupation=['11-1011 Chief Executives',\
'11-3011 Administrative Services Managers',\
'11-3031 Financial Managers',\
'11-3061 Purchasing Managers',\
'13-1011 Agents and Business Managers of Artists, Performers, and Athletes',\
'13-1031 Claims Adjusters, Examiners, and Investigators',\
'13-1199 Business Operations Specialists, All Other',\
'13-2099 Financial Specialists, All Other',\
'17-1011 Architects, Except Landscape and Naval',\
'23-1011 Lawyers',\
'23-1023 Judges, Magistrate Judges, and Magistrates',\
'25-2012 Kindergarten Teachers, Except Special Education',\
'25-2021 Elementary School Teachers, Except Special Education',\
'29-1041 Optometrists',\
'29-2054 Respiratory Therapy Technicians',\
'33-2011 Firefighters',\
'37-1012 First-Line Supervisors of Landscaping, Lawn Service, and Groundskeeping Workers',\
'39-1011 Gaming Supervisors',\
'39-2011 Animal Trainers',\
'41-1011 First-Line Supervisors of Retail Sales Workers',\
'41-1012 First-Line Supervisors of Non-Retail Sales Workers',\
'41-2011 Cashiers',\
'41-2031 Retail Salespersons',\
'43-3021 Billing and Posting Clerks',\
'45-1011 First-Line Supervisors of Farming, Fishing, and Forestry Workers',\
'49-2011 Computer, Automated Teller, and Office Machine Repairers',\
'53-3021 Bus Drivers, Transit and Intercity',\
'53-4031 Railroad Conductors and Yardmasters',\
'55-1011 Air Crew Officers',\
'55-1012 Aircraft Launch and Recovery Officers',\
'55-1013 Armored Assault Vehicle Officers',\
]
Privately_ATM_Operator=Embassy_Consulate
Products=['Certificate of Deposit',\
'Checking Account',\
'Credit Card',\
'Custodial and Investment Agency - Institutional',\
'Custodial and Investment Agency - Personal',\
'Custodial/Trust Outsourcing Services (BTOS)',\
'Custody Accounts (PTIM)',\
'Custody Accounts (RSTC)',\
'DTF (BHFA)',\
'Investment Agency - Institutional','Investment Agency - Institutional','Investment Agency - Institutional','Investment Agency - Institutional','Investment Agency - Institutional',\
'Investment Agency - Personal',\
'Investment Management Account (PTIM)',\
'Lease',\
'Loan / Letter of Credit',\
'Money Market',\
'Mortgage / Bond / Debentures',\
'Nondeposit Investment Products','Nondeposit Investment Products','Nondeposit Investment Products','Nondeposit Investment Products','Nondeposit Investment Products','Nondeposit Investment Products','Nondeposit Investment Products','Nondeposit Investment Products','Nondeposit Investment Products','Nondeposit Investment Products','Nondeposit Investment Products','Nondeposit Investment Products','Nondeposit Investment Products','Nondeposit Investment Products',\
'None',\
'Savings Account',\
'Trust Administration - Irrevocable and Revocable (PTIM)',\
'Trust Administration - Irrevocable and Revocable Trusts (BDTC)',\
]
Sales_Used_Vehicles=Embassy_Consulate
Services=['Benefit Payment Services',\
'Domestic Wires and Direct Deposit / ACH',\
'Family Office Services (FOS)',\
'Fiduciary Services',\
'Financial Planning','Financial Planning','Financial Planning','Financial Planning','Financial Planning','Financial Planning',\
'International Wires and IAT',\
'Investment Advisory Services (IAS)',\
'Investment Services',\
'None',\
'Online / Mobile Banking',\
'Payroll',\
'Retirement Plans','Retirement Plans','Retirement Plans','Retirement Plans','Retirement Plans','Retirement Plans','Retirement Plans','Retirement Plans','Retirement Plans','Retirement Plans','Retirement Plans','Retirement Plans','Retirement Plans','Retirement Plans','Retirement Plans','Retirement Plans','Retirement Plans','Retirement Plans','Retirement Plans',\
'Short?Term Cash Management',\
'Trust Services',\
'Trustee Services',\
'Vault Cash Services',\
]
SIC_Code=['6021 National Commercial Banks',\
'6211 Security Brokers, Dealers, and Flotation Companies',\
'6282 Investment Advice',\
'6311 Life Insurance',\
'6722 Management Investment Offices, Open-End','6722 Management Investment Offices, Open-End','6722 Management Investment Offices, Open-End','6722 Management Investment Offices, Open-End','6722 Management Investment Offices, Open-End','6722 Management Investment Offices, Open-End','6722 Management Investment Offices, Open-End','6722 Management Investment Offices, Open-End','6722 Management Investment Offices, Open-End','6722 Management Investment Offices, Open-End','6722 Management Investment Offices, Open-End','6722 Management Investment Offices, Open-End',\
'6733 Trusts, Except Educational, Religious, and Charitable',\
'8999 Services, NEC',\
]
Stock_Market_Listing=['Australian Stock Exchange',\
'Brussels Stock Exchange',\
'Montreal Stock Exchange',\
'Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found','Not Found',\
'Tiers 1 and 2 of the TSX Venture Exchange (also known as Tiers 1 and 2 of the Canadian Venture Exchange)',\
'Toronto Stock Exchange',\
]
Third_Party_Payment_Processor=Embassy_Consulate
Transacting_Provider=Embassy_Consulate


fake = Faker()
gen_data.create_date(past=True)

with open('large.csv','r') as csvinput:
	with open('large_extended.csv','w') as csvoutput:
	
		writer=csv.writer(csvoutput, delimiter=',',lineterminator='\n',)
		reader = csv.reader(csvinput)

		row = next(reader)
		
		
		row.append('RELATED_ACCT')
		row.append('RELATED_TYPE')
		row.append('PARTY_TYPE')
		row.append('PARTY_RELATION')
		row.append('PARTY_STARTDATE')
		row.append('PARTY_ENDDATE')
		row.append('LARGE_CASH_EXEMPT')
		row.append('DEMARKET_FLAG')
		row.append('DEMARKET_DATE')
		row.append('PROB_DEFAULT_RISKR')
		row.append('OFFICIAL_LANG_PREF')
		row.append('CONSENT_SHARING')
		row.append('PREFERRED_CHANNEL')
		row.append('PRIMARY_BRANCH_NO')
		
		row.append('CUSTOMER_STATUS')
		row.append('DEPENDANTS_COUNT')
		row.append('SEG_MODEL_ID')
		row.append('SEG_MODEL_TYPE')
		row.append('SEG_MODEL_NAME')
		row.append('SEG_MODEL_GROUP')
		row.append('SEG_M_GRP_DESC')
		row.append('SEG_MODEL_SCORE')
		row.extend(['ARMS_MANUFACTURER','AUCTION','CASHINTENSIVE_BUSINESS','CASINO_GAMBLING','CHANNEL_ONBOARDING','CHANNEL_ONGOING_TRANSACTIONS',\
				'CLIENT_NET_WORTH','COMPLEX_HI_VEHICLE','DEALER_PRECIOUS_METAL','DIGITAL_PM_OPERATOR','EMBASSY_CONSULATE','EXCHANGE_CURRENCY','FOREIGN_FINANCIAL_INSTITUTION',\
				'FOREIGN_GOVERNMENT','FOREIGN_NONBANK_FINANCIAL_INSTITUTION','INTERNET_GAMBLING','MEDICAL_MARIJUANA_DISPENSARY','MONEY_SERVICE_BUSINESS','NAICS_CODE',\
				'NONREGULATED_FINANCIAL_INSTITUTION','NOT_PROFIT','OCCUPATION','PRIVATELY_ATM_OPERATOR','PRODUCTS','SALES_USED_VEHICLES','SERVICES','SIC_CODE',\
				'STOCK_MARKET_LISTING','THIRD_PARTY_PAYMENT_PROCESSOR','TRANSACTING_PROVIDER'])
		
		writer.writerow(row)
		
		for i in range(16800000):   
			row = next(reader)
			rel = random.choice(python_account_ID.accountid)*max((randrange(0,10000,1)-9999),0)
			
			if rel <> 0: 
				row.append(rel[0])
				row.append(random.choice(Related_Type))
			else:
				row.append('')
				row.append('')
				
			party_start=gen_data.create_date()
			Consent_Share = random.choice(Yes_No_Consent)
			
			row.extend([random.choice(Party_Type) , random.choice(Party_Relation) , party_start , gen_data.create_date() , \
			random.choice(Yes_No), random.choice(Yes_No) , gen_data.create_date() , randrange(0,100,1) , random.choice(Official_Lang)])
			
			if Consent_Share == 'Yes':
				row.extend(['Yes',random.choice(Preffered_Channel)])
			else: 
				row.extend(['Yes',''])
			
			row.extend([random.choice(Primary_Branch),random.choice(Customer_Status),randrange(0,5,1)])
			
			Segment_ID = randrange(0,5,1)%5
			
			if Segment_ID == 0:
				row.extend([Model_ID[0],Seg_Model_Type[0],Seg_Model_Name[0],Seg_Model_Group[0],Seg_Model_Description[0],Seg_Model_Score[0]])
			
			if Segment_ID == 1:
				row.extend([Model_ID[1],Seg_Model_Type[1],Seg_Model_Name[1],Seg_Model_Group[1],Seg_Model_Description[1],Seg_Model_Score[1]])
				
			if Segment_ID == 2:
				row.extend([Model_ID[2],Seg_Model_Type[2],Seg_Model_Name[2],Seg_Model_Group[2],Seg_Model_Description[2],Seg_Model_Score[2]])
				
			if Segment_ID == 3:
				row.extend([Model_ID[3],Seg_Model_Type[3],Seg_Model_Name[3],Seg_Model_Group[3],Seg_Model_Description[3],Seg_Model_Score[3]])
				
			if Segment_ID == 4:
				row.extend([Model_ID[4],Seg_Model_Type[4],Seg_Model_Name[4],Seg_Model_Group[4],Seg_Model_Description[4],Seg_Model_Score[4]])
					
			row.extend([random.choice(Arms_Manufacturer),
			random.choice(Auction),
			random.choice(CashIntensive_Business),
			random.choice(Casino_Gambling),
			random.choice(Channel_Onboarding),
			random.choice(Channel_Ongoing_Transactions)])
			
			row.append(max(max((randrange(0,101,1)-99),0)* randrange(20000,500000,1),randrange(5,35000,1)))
			
			row.extend([random.choice(Complex_HI_Vehicle),
			random.choice(Dealer_Precious_Metal),
			random.choice(Digital_PM_Operator),
			random.choice(Embassy_Consulate),
			random.choice(Exchange_Currency),
			random.choice(Foreign_Financial_Institution),
			random.choice(Foreign_Government),
			random.choice(Foreign_NonBank_Financial_Institution),
			random.choice(Internet_Gambling),
			random.choice(Medical_Marijuana_Dispensary),
			random.choice(Money_Service_Business),
			random.choice(NAICS.NAICS_Code),
			random.choice(NonRegulated_Financial_Institution),
			random.choice(Not_Profit),
			random.choice(Occupation),
			random.choice(Privately_ATM_Operator),
			random.choice(Products),
			random.choice(Sales_Used_Vehicles),
			random.choice(Services),
			random.choice(SIC_Code),
			random.choice(Stock_Market_Listing),
			random.choice(Third_Party_Payment_Processor),
			random.choice(Transacting_Provider)])
					
			writer.writerow(row)
