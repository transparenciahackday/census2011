import couchdb
import csv
import os

#couch = couchdb.Server()
#db = couch['censos2011']

def loadfields(row):
    # APPLY A FEW TRANSFORMATIONS TO THE FIELDS
    return [str(cell).strip().decode('latin-1') for cell in row]

def getdescription(file):
    with open(file, 'r') as f:
        r = csv.reader(f)
        row = loadfields(r.next())
        return row[0]


#with open('Q1.01..csv', 'r') as file:
#    for row in csv.reader(file):
#        print loadfields(row)




for p in os.listdir(os.curdir):
    if p.endswith('csv'):
        print getdescription(p)



