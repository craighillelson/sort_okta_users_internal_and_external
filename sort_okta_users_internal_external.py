""" __doc__ """

# import
import csv

# prompt user
print "What is your fully qualified domain name?"
DOMAIN = raw_input()

# create lists to be populated later
INTERNAL_USERS = []
EXTERNAL_USERS = []

# define write_csv function
def write_csv(a, b):
    """ write results to csv """
    with open(a, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['email'])
        for email in b:
            writer.writerow([email])

# open csv and sort users into two lists (internal_users and external_users)
# based on their email addresses
with open('OktaPasswordHealth.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        email = row['Login']
        if email.endswith(DOMAIN):
            INTERNAL_USERS.append(email)
        else:
            EXTERNAL_USERS.append(email)

# call function
write_csv('internal_users.csv', INTERNAL_USERS)
write_csv('external_users.csv', EXTERNAL_USERS)

# update user
print "'internal_users.csv' and 'external_users.csv' exported successfully"
