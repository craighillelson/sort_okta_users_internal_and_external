""" __doc__ """

# import
import csv

# prompt user
print("What is your fully qualified domain name?")
DOMAIN = input()

# create lists to be populated later
INTERNAL_USERS = []
EXTERNAL_USERS = []

# define write_csv function
def write_csv(csv_file, lst):
    """ write results to csv """
    with open(csv_file, 'w') as out_csvfile:
        writer = csv.writer(out_csvfile)
        writer.writerow(['email'])
        for email in lst:
            writer.writerow([email])


# open csv and sort users into two lists (internal_users and external_users)
# based on their email addresses
with open('OktaPasswordHealth.csv', 'r') as in_csvfile:
    READER = csv.DictReader(in_csvfile)
    for row in READER:
        user_email = row['Login']
        if user_email.endswith(DOMAIN):
            INTERNAL_USERS.append(user_email)
        else:
            EXTERNAL_USERS.append(user_email)

# call function
write_csv('internal_users.csv', INTERNAL_USERS)
write_csv('external_users.csv', EXTERNAL_USERS)

# update user
print("'internal_users.csv' and 'external_users.csv' exported successfully")
