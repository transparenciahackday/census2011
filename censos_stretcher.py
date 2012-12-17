import couchdb
import csv
import os
from json import dumps
#couch = couchdb.Server()
#db = couch['censos2011']


class Quadro(object):
    def __init__(self, reader):
        iter_read = self._iter_rows(reader)
        first = iter_read.next()
        
        self.qname = first
        
        
        headers = list()
        while True:
            row = iter_read.next()
            headers.append(row)
            if all([cell.isdigit() for cell in row[:-2]]):
                break
            else:
                #print row
                pass
        
        self.headers = headers
        
        
        
    
    def _iter_rows(self, reader):
        for row in reader:
            yield self._load_fields(row)
    
    def _load_fields(self, row):
        # APPLY A FEW TRANSFORMATIONS TO THE FIELDS
        return [str(cell).strip().decode('latin-1') for cell in row]


#for p in os.listdir(os.curdir)[:6]:
for p in os.listdir(os.curdir + '/data'):
    if p.endswith('csv'):
        print 
        with open('data/' + p, 'r') as f:
            q = Quadro(csv.reader(f))
            print q.qname
            print len(q.headers)



