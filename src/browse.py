#!/usr/bin/env python

print '<div id="container">'

sampleFile = open('sampleDeals.txt', 'r')
objectCount = 0

for line in sampleFile:
  lineList = line.split(';')
  print '<div class="coverflow" id="object' + str(objectCount) + '">'
  print '<h2>' + lineList[0] + ' - ' + lineList[1] + ' - ' + lineList[2] + '</h2>'
  print '</div>'
  objectCount += 1

print '</div>'