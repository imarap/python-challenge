#pyBoss.py
#Imara Paiz
import os
import csv
from datetime import datetime
csvpath = 'employee_data1.csv'

#create dictionary of states and abbreviations
states = {
    'Alabama' : 'AL',
    'Alaska' : 'AK',
    'Arizona' : 'AZ',
    'Arkansas' : 'AR',
    'California' : 'CA',
    'Colorado' : 'CO',
    'Connecticut' : 'CT',
    'Delaware' : 'DE',
    'Florida' : 'FL',
    'Georgia' : 'GA',
    'Hawaii' : 'HI',
    'Idaho' : 'ID',
    'Illinois' : 'IL',
    'Indiana' : 'IN',
    'Iowa' : 'IA',
    'Kansas' : 'KS',
    'Kentucky' : 'KY',
    'Louisiana' : 'LA',
    'Maine' : 'ME',
    'Maryland' : 'MD',
    'Massachusetts' : 'MA',
    'Michigan' : 'MI',
    'Minnesota' : 'MN',
    'Mississippi' : 'MS',
    'Missouri' : 'MO',
    'Montana' : 'MT', 
    'Nebraska' : 'NE',
    'Nevada' : 'NV',
    'New Hampshire' : 'NH',
    'New Jersey' : 'NJ',
    'New Mexico' : 'NM',
    'New York' : 'NY',
    'North Carolina' : 'NC',
    'North Dakota' : 'ND',
    'Ohio' : 'OH',
    'Oklahoma' : 'OK',
    'Oregon' : 'OR',
    'Pennsylvania' : 'PA',
    'Rhode Island' : 'RI',
    'South Carolina' : 'SC',
    'South Dakota' : 'SD',
    'Tennessee' : 'TN',
    'Texas' : 'TX',
    'Utah' : 'UT',
    'Vermont' : 'VT',
    'Virginia' : 'VA',
    'Washington' : 'WA',
    'West Virginia' : 'WV',
    'Wisconsin' : 'WI',
    'Wyoming' : 'WY'
}

counter = 0
employee_line = []

with open(csvpath, newline='') as csvfile1:
    csvreader = csv.reader(csvfile1, delimiter=',')
    print("Emp ID,First Name,Last Name,DOB,SSN,State")
    for row in csvreader:
        counter = counter + 1
        empid = row[0]
        names = row[1].split(" ")
        firstname = names[0]
        lastname = names[1]
        dob_to_date = datetime.strptime(row[2], '%Y-%m-%d').date()
        dob_format = datetime.strftime(dob_to_date, '%m/%d/%Y')
        ssn = '***-**-' + row[3][7:]
        state = states[row[4]]
        employee_line.append(empid + "," + firstname + "," + lastname + "," + str(dob_format) + "," + ssn + "," + state)
        print(employee_line[counter-1])
print('Total Employees: ' + str(counter))    

#print results to a file
output_file = os.path.join("employees_formatted.csv")
with open(output_file, "w", newline="") as datafile:   
    datafile.write("Emp ID,First Name,Last Name,DOB,SSN,State\n")
    for emp in employee_line:
        datafile.write(str(emp) + '\n')

    datafile.write("Total Employees: " + str(counter))