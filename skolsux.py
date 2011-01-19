#!/usr/bin/python2.7
# ------------------------------------------------------
# file: $BINARIES/skool.py
# author: Richard Shaw - <richs@archlinux.us>
# modified: January 2011
# vim:fenc=utf-8:nu:ai:si:et:ts=4:sw=4:ft=python:
# ------------------------------------------------------
#
# Yes, yes, regex... I know.
from BeautifulSoup import BeautifulSoup
import urllib2

arg = '60' 

tree = urllib2.urlopen('http://schoolsout.com/view/school/%s' % arg)

compiled = BeautifulSoup(tree.read())

div = compiled.find("div", attrs={"class" : "body"})
p = div.find("p")

for p in p:
  p = p.replace('<p>',' ').replace('</p>',' ')

print (p)
