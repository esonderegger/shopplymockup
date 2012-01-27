#!/usr/bin/env python

import shopplyDeals
import cgi

form = cgi.FieldStorage()
dealKey = form.getfirst("addkey", "none")
if dealKey != 'none':
  theDeal = shopplyDeals.shopplyDeal.get(dealKey)
  theDeal.isMyDeal = True
  theDeal.put()

dealsCount = shopplyDeals.countMyDeals()

print 'Content-Type: text/html \n'
if dealsCount > 0:
  print '<a href="javascript:void(0)" onclick="showMyDeals();">My Deals (' + str(dealsCount) + ')</a>'
else:
  print '<a href="javascript:void(0)" onclick="showMyDeals();">My Deals</a>'