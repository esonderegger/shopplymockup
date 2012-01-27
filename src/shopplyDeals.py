#!/usr/bin/env python

from google.appengine.ext import db

class shopplyDeal(db.Model):
	vendor = db.StringProperty()
	vendorGraphic = db.StringProperty()
	itemName = db.StringProperty()
	itemDescription = db.StringProperty()
	itemGraphic = db.StringProperty()
	averageSavings = db.FloatProperty()
	isMyDeal = db.BooleanProperty()

def getAllDeals():
	dealsQuery = db.GqlQuery("SELECT * FROM shopplyDeal")
	deals = dealsQuery.fetch(50)
	if len(deals) > 0:
	  return deals
	else:
	  getDealsFromFile()
	  getAllDeals()

def getDealsFromFile():
  sampleFile = open('sampleDeals.txt', 'r')
  for line in sampleFile:
    lineList = line.split(';')
    newDeal = shopplyDeal()
    newDeal.vendor = lineList[0]
    newDeal.vendorGraphic = lineList[1]
    newDeal.itemName = lineList[2]
    newDeal.itemDescription = lineList[3]
    newDeal.itemGraphic = lineList[4]
    newDeal.averageSavings = float(lineList[5])
    newDeal.isMyDeal = False
    newDeal.put()

def countMyDeals():
  myDealsQuery = db.GqlQuery("SELECT * FROM shopplyDeal WHERE isMyDeal = True")
  myDealsCount = myDealsQuery.count()
  return myDealsCount
