#!/usr/bin/env python

def mainHeader():
  print '<header>'
  print '<div id="logo">'
  print '<img src="/img/ShopplyLogo.png" alt="Shopply Logo" />'
  print '</div>'
  print '<div id="headerLinks">'
  print 'Home | My Deals | Search'
  print '</div>'
  print '<div id="welcomeUser">'
  print 'Welcome Dave'
  print '</div>'
  print '</header>'

print 'Content-Type: text/html \n'
print '<!DOCTYPE html>'
print '<html lang="en">'
print '<head>'
print '<meta charset="utf-8" />'
print '<title>Shopply</title>'
print '<link href="/css/shopply.css" rel="stylesheet" />'
print '</head>'
print '<body>'
mainHeader()
print '</body>'
print '</html>'