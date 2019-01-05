# import
import csv

# prompt user
print "What is your fully qualified domain name?"
domain = raw_input()

# create lists to be populated later
internal_users = []
external_users = []

# define write_csv function
def write_csv(a, b):
    with open(a, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['email'])
        for email in b:
            writer.writerow([email])

# open csv and sort users into two lists (internal_users and external_users) based on their email addresses
with open('OktaPasswordHealth.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        email = row['Login']
        if email.endswith(domain):
            internal_users.append(email)
        else:
            external_users.append(email)

# call function
write_csv('internal_users.csv', internal_users)
write_csv('external_users.csv', external_users)

# update user
print "'internal_users.csv' and 'external_users.csv' exported successfully"
