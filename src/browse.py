#!/usr/bin/env python

print '<div id="container">'

sampleFile = open('sampleDeals.txt', 'r')
objectCount = 0

for line in sampleFile:
  lineList = line.split(';')
  print '<div class="coverflow" id="object' + str(objectCount) + '">'
  print '<div>' + lineList[0] + '</div>'
  print '<div>' + lineList[1] + '</div>'
  print '<div>' + lineList[2] + '</div>'
  print '</div>'
  objectCount += 1

print '</div>'