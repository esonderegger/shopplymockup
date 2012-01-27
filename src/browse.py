#!/usr/bin/env python

import shopplyDeals

print 'Content-Type: text/html \n'
print '<div id="container">'

allDeals = shopplyDeals.getAllDeals("")
objectCount = 0

for deal in allDeals:
  print '<div class="coverflow" id="object' + str(objectCount) + '" title="' + str(deal.key()) + '" onclick="moveCenter(' + str(objectCount) + ');">'
  print '<div class="vendorLogo"><img src="' + deal.vendorGraphic.encode('utf-8') + '" alt="' + deal.vendor.encode('utf-8') + '" /></div>'
  print '<div class="itemGraphic"><img src="' + deal.itemGraphic.encode('utf-8') + '" alt="' + deal.itemName.encode('utf-8') + '" /></div>'
  print '<div class="itemName">' + deal.itemName.encode('utf-8') + '</div>'
  print '<div class="itemDescription">' + deal.itemDescription.encode('utf-8') + '</div>'
  print '<div class="averageSavings">Average saving: $' + str(deal.averageSavings) + '</div>'
  print '</div>'
  objectCount += 1

print '</div>'

print '<div id="browseLinks">'
print '<div class="arrowLink">'
print '<a href="javascript:void(0)" onclick="moveLeft();"><img src="/img/moveLeft.png" alt="Move Left" /></a>'
print '</div>'
print '<div id="addToDeals">'
print '<a href="javascript:void(0)" onclick="addToDeals();">Add to Deals</a>'
print '</div>'
print '<div class="arrowLink">'
print '<a href="javascript:void(0)" onclick="moveRight();"><img src="/img/moveRight.png" alt="Move Right" /></a>'
print '</div>'
print '</div>'