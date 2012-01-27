#!/usr/bin/env python
# this is the main page for the mockup. I put the header block in its own function in case I was going to make
# multiple pages, which I ended up not doing.

def mainHeader():
  print '<header>'
  print '<div id="logo">'
  print '<a href="/"><img src="/img/ShopplyLogo.png" alt="Shopply Logo" /></a>'
  print '</div>'
  print '<div id="headerLinks">'
  print '<span id="homeLink" title="allDeals"><a href="/">Home</a> | </span>'
  print '<span id="myDealsLink">My Deals</span>'
  print '<span name="searchContainer"> | <form id="searchForm">'
  print '<input type="text" id="searchBox" name="searchstring" value="Search..." onfocus="if (this.value == \'Search...\') {this.value = \'\';}" onKeyPress="return disableEnterKey(event)" onkeyup="shopplySearch()">'
  print '</form></span>'
  print '</div>'
  print '<div id="welcomeUser">'
  print '<div id="userPic">'
  print '<img src="/img/welcomeDave.png" alt="Welcome Dave" />'
  print '</div>'
  print '<div id="welcomeName">'
  print 'Welcome Dave'
  print '</div>'
  print '</div>'
  print '</header>'

print 'Content-Type: text/html \n'
print '<!DOCTYPE html>'
print '<html lang="en">'
print '<head>'
print '<meta charset="utf-8" />'
print '<title>Shopply</title>'
print '<link href="/css/shopply.css" rel="stylesheet" />'
print '<script src="/js/shopply.js"></script>'
print "<link href='http://fonts.googleapis.com/css?family=Nunito' rel='stylesheet' type='text/css'>"
print '</head>'
print '<body onload=initMainPage()>'
mainHeader()
print '<div id="dealsContent">'
print '</div>'
print '</body>'
print '</html>'