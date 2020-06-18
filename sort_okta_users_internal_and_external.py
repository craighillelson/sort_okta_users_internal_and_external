"""
Import 'OktaPasswordHealth.csv' and sort users into internal and external
groups.
"""

import csv

print("\nWhat is your fully qualified domain name?")
DOMAIN = input('> ')

INTERNAL_USERS = []
EXTERNAL_USERS = []


def write_csv(csv_file, lst):
    """Write results to a csv."""
    with open(csv_file, 'w') as out_csvfile:
        writer = csv.writer(out_csvfile)
        writer.writerow(['email'])
        for email in lst:
            writer.writerow([email])


with open('OktaPasswordHealth.csv', 'r') as in_csvfile:
    READER = csv.DictReader(in_csvfile)
    for row in READER:
        user_email = row['Login']
        if user_email.endswith(DOMAIN):
            INTERNAL_USERS.append(user_email)
        else:
            EXTERNAL_USERS.append(user_email)

write_csv('internal_users.csv', INTERNAL_USERS)
write_csv('external_users.csv', EXTERNAL_USERS)
print("'internal_users.csv' and 'external_users.csv' exported successfully\n")
