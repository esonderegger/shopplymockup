#!/usr/bin/env python

import shopplyDeals
import cgi

def dealsToTable(deals):
  print '<table>'
  for deal in deals:
    print '<tr>'
    print '<td>' + deal.vendor.encode('utf-8') + '</td>'
    print '<td>' + deal.itemName.encode('utf-8') + '</td>'
    print '<td>' + deal.itemDescription.encode('utf-8') + '</td>'
    if deal.isMyDeal:
      print '<td><a href="javascript:void(0)" onclick="removeDealFromList(\'' + str(deal.key()) + '\');"><img src="/img/remove.png" alt="Remove Deal" /></a></td>'
    else :
      print '<td><a href="javascript:void(0)" onclick="addDealFromList(\'' + str(deal.key()) + '\');"><img src="/img/add.png" alt="Add Deal" /></a></td>'
    print '</tr>'
  print '</table>'

print 'Content-Type: text/html \n'

form = cgi.FieldStorage()
showMyDeals = form.getfirst("myDeals", "no")
searchString = form.getfirst("search", "")

if showMyDeals == 'yes':
  myDeals = shopplyDeals.getAllMyDeals(searchString)
  if myDeals:
    dealsToTable(myDeals)
  else:
    print "<h1>You don't have any saved deals</h1>"
else:
  myDeals = shopplyDeals.getAllDeals(searchString)
  if myDeals:
    for deal in myDeals:
      dealsToTable(myDeals)
  else:
    print "<h1>Your search generated no results.</h1>"

