#!/usr/bin/env python
# this provides the database funtionality for the mockup
# the long if statements are because appengine doesn't provide full-text search and I had invested too much in
# this appengine project to try a different approach.

from google.appengine.ext import db

class shopplyDeal(db.Model):
	vendor = db.StringProperty()
	vendorGraphic = db.StringProperty()
	itemName = db.StringProperty()
	itemDescription = db.StringProperty()
	itemGraphic = db.StringProperty()
	averageSavings = db.FloatProperty()
	isMyDeal = db.BooleanProperty()

def getAllDeals(srch):
  outputDeals = []
  dealsQuery = shopplyDeal.all()
  deals = dealsQuery.fetch(50)
  if len(deals) > 0:
    for deal in deals:
      if (str(deal.vendor).lower().find(srch.lower()) >= 0) or (str(deal.itemName).lower().find(srch.lower()) >= 0) or (str(deal.itemDescription).lower().find(srch.lower()) >= 0):
        outputDeals.append(deal)
    return outputDeals
  else:
    getDealsFromFile()
    getAllDeals("")

def getAllMyDeals(srch):
# filters the query to only return the deals that are saved by the user
# note that for this mockup I only allow for one user
  dealsQuery = db.GqlQuery("SELECT * FROM shopplyDeal WHERE isMyDeal = True")
  deals = dealsQuery.fetch(50)
  outputDeals = []
  for deal in deals:
    if (str(deal.vendor).lower().find(srch.lower()) >= 0) or (str(deal.itemName).lower().find(srch.lower()) >= 0) or (str(deal.itemDescription).lower().find(srch.lower()) >= 0):
      outputDeals.append(deal)
  return outputDeals

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
