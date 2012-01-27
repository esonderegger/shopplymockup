#!/usr/bin/env python

import shopplyDeals
import cgi

def dealsToTable(deals):
  print '<table>'
  for i in range(len(deals)):
    if i % 2 == 1:
      print '<tr class="oddTableRow">'
    else :
      print '<tr class="evenTableRow">'
    print '<td>' + deals[i].vendor.encode('utf-8') + '</td>'
    print '<td>' + deals[i].itemName.encode('utf-8') + '</td>'
    print '<td>' + deals[i].itemDescription.encode('utf-8') + '</td>'
    if deals[i].isMyDeal:
      print '<td><a href="javascript:void(0)" onclick="removeDealFromList(\'' + str(deals[i].key()) + '\');"><img src="/img/remove.png" alt="Remove Deal" /></a></td>'
    else :
      print '<td><a href="javascript:void(0)" onclick="addDealFromList(\'' + str(deals[i].key()) + '\');"><img src="/img/add.png" alt="Add Deal" /></a></td>'
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
    dealsToTable(myDeals)
  else:
    print "<h1>Your search generated no results.</h1>"

