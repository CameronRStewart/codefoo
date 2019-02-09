#!/usr/local/bin/python
import csv
import datetime

def presidentParty(path):
    latestPossibleDate = datetime.datetime.now().year
    datesCount = {}
    with open(path) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:

            row = [c.strip() for c in row]

            if len(row) < 2:
                # birth not set
                # This is an error condition bruh
                continue
            elif len(row) < 4:
                # make assumption home boy hasnt died yet
                death = int(latestPossibleDate)
            else:
                try:
                    birth = int(row[1].split()[2])
                    death = int(row[3].split()[2])
                except:
                    # assume row is screwey, skip.
                    continue

            for i in range(birth, death+1):
                if i in datesCount:
                    datesCount[i] += 1
                else:
                    datesCount[i] = 1
    #Get max value
    maxCount = max(datesCount.values())
    print [key for key in datesCount.keys() if datesCount[key] == maxCount]


importCSV("/Users/bacchus/Documents/Code/coding-challenges/:r:codefoo/presidents/presidents.csv")
