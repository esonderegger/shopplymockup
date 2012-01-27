#!/usr/bin/env python

import shopplyDeals
import cgi

print 'Content-Type: text/html \n'

form = cgi.FieldStorage()
showMyDeals = form.getfirst("myDeals", "no")
searchString = form.getfirst("search", "")

if showMyDeals == 'yes':
  myDeals = shopplyDeals.getAllMyDeals(searchString)
  if myDeals:
    for deal in myDeals:
      print '<h1>' + deal.itemName.encode('utf-8') + '</h1>'
  else:
    print "<h1>You don't have any saved deals</h1>"
else:
  myDeals = shopplyDeals.getAllDeals(searchString)
  if len(myDeals) > 0:
    for deal in myDeals:
      print '<h1>' + deal.itemName.encode('utf-8') + '</h1>'
  else:
    print "<h1>Your search generated no results.</h1>"

