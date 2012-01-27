#!/usr/bin/env python

import shopplyDeals
import cgi
import time

form = cgi.FieldStorage()
addKey = form.getfirst("addkey", "none")
removeKey = form.getfirst("removekey", "none")

if addKey != 'none':
  theDeal = shopplyDeals.shopplyDeal.get(addKey)
  theDeal.isMyDeal = True
  theDeal.put()

if removeKey != 'none':
  theDeal = shopplyDeals.shopplyDeal.get(removeKey)
  theDeal.isMyDeal = False
  theDeal.put()

time.sleep(0.3)
dealsCount = shopplyDeals.countMyDeals()

print 'Content-Type: text/html \n'
if dealsCount > 0:
  print '<a href="javascript:void(0)" onclick="showMyDeals();">My Deals (' + str(dealsCount) + ')</a>'
else:
  print '<a href="javascript:void(0)" onclick="showMyDeals();">My Deals</a>'