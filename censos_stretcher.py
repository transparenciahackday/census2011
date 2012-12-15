import couchdb
import csv

#couch = couchdb.Server()
#db = couch['censos2011']

def loadfields(row):
    # APPLY A FEW TRANSFORMATIONS TO THE FIELDS
    return [str(cell).strip().decode('latin-1') for cell in row]

with open('Q1.01..csv', 'r') as file:
    for row in csv.reader(file):
        print loadfields(row)


