#!/usr/bin/env python

print '<div id="container">'

sampleFile = open('sampleDeals.txt', 'r')
objectCount = 0

for line in sampleFile:
  lineList = line.split(';')
  print '<div class="coverflow" id="object' + str(objectCount) + '" onclick="moveCenter(' + str(objectCount) + ');">'
  print '<div>' + lineList[0] + '</div>'
  print '<div>' + lineList[1] + '</div>'
  print '<div>' + lineList[2] + '</div>'
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