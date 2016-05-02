import csv
import operator
from ast import literal_eval
from datetime import datetime

baldata = []

with open('data/bal.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['Weapon'] != 'FIREARM' or not row['Location 1']:
            continue
        crime_time = row['CrimeTime']
        if len(crime_time) == 4:
            crime_time = ('000' + str(int(crime_time) % 2400))[-4:]
        else:
            crime_time = crime_time.replace(':', '')[:4]

        crime_dt = row['CrimeDate'] + crime_time
        crime_ts = datetime.strptime(crime_dt, '%m/%d/%Y%H%M')

        latitude, longitude = literal_eval(row['Location 1'])

        baldata.append((crime_ts,
                        row['CrimeCode'],
                        row['Description'].title(),
                        row['Weapon'].title(),
                        latitude,
                        longitude,
                        int(row['Total Incidents'])))

baldata.sort(key=operator.itemgetter(0))

with open('data/bal_cleaned.csv', 'w') as f:
    fieldnames = ['ts',
                  'code',
                  'description',
                  'weapon',
                  'lat',
                  'long',
                  'count']
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(fieldnames)
    for row in baldata:
        writer.writerow(row)
