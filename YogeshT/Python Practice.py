import csv
'''
# opening the CSV file
with open('students.csv', mode='r') as file:
    # reading the CSV file
    csvFile = csv.reader(file)

    # displaying the contents of the CSV file
    for lines in csvFile:
        print(lines)
'''

'''
# Appending in CSV Files

with open('students.csv', mode = 'a') as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(['Demo 1','Person 1','7666648075','hirefreelancersnow@gmail.com','16-Aug-21','03:00pm','L1','Ipsita'])
    file.close()
'''


