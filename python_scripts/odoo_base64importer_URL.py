# -*- coding: cp1252 -*-
##Configuration
url = raw_input("Database URL (e.g. https://mydatabase.odoo.com): ")
db = raw_input("Database Name (e.g. mydatabase): ")
username = raw_input("Login (e.g. admin@mydatabase.com): ")
password = raw_input("Password (e.g. admin): ")

##Importing Libraries
import xmlrpclib
import csv 
import sys
import base64
import urllib
import time

##Authentication
common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
common.version()

##uid Routing
uid = common.authenticate(db, username, password, {})

##calling
models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))

#first open of CSV
from Tkinter import Tk
from tkFileDialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
var = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print "You Selected ", var
f = open(var)
reader = csv.reader(f)

next(reader, None)  # skip the headers
#unique_emails = []
for row in reader:
    try:
        g = urllib.urlopen(row[1])  
        encoded = base64.b64encode(g.read())
        print(row[0])
        #print(encoded)
        models.execute_kw(db, uid, password, 'product.product', 'write', [int(row[0]), {
        'image': encoded
        }])
        time.sleep(1)
        continue
    except:
        print('error')
        continue
        



print '****IMPORT COMPLETED****'
close = raw_input("Press enter to close prompt")
