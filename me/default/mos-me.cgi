#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Execute as cgi-skript and send a correct HTTP header.

"""

#Enable debugging of cgi-.scripts
import cgitb
cgitb.enable()    


# Send the HTTP header
print("Content-Type: text/plain;charset=utf-8")
#print("Content-Type: text/html;charset=utf-8")
print("")


# Here comes the content of the webpage 
print("""
Min Me-sida
==============================================================================

Hej, 

Jag heter Mikael Roos och är lärare på denna kurs i Python. 
          ,     ,
         (\____/)
          (_oo_)
            (O)
          __||__    \)
       []/______\[] /
       / \______/ \/
      /    /__\ 
     (\   /____\ 

Detta är min me-sida i kursen. Denna sidan innehåller en presentation av mig
själv. Underhåll denna sidan under hela kursen och uppdatera den efter hand
och behov.

Så, en presentation en bra början. Skriv några ord om dig själv. Jag börjar.

Mitt namn är Mikael Roos. Född och uppvuxen i Bankeryd, Småland, strax utanför
Jönköping, i ett villaområde som byggdes upp samtidigt som vi flyttade in där.
En längre historia om mig finns att läsa i min me-sida för kursen oophp. Du 
når den via länken:
http://dbwebb.se/oophp/me/kmom01/me.php


Om jag skall nämna någon hobby, förutom webbprogrammering, så får det bli att
bära sten på sommarstugetomten, och det finns sten så det räcker ett par 
livstider. Till och från får jag för mig att börja på lite hobbies, ett år 
satsade jag på pokerspel, ett annat år var det geocaching. 

Årets hobby är Turfing:
http://dbwebb.se/blogg/forsmak-infor-hosten-2014#hobby

Vi syns och hörs i forum och chatt!

""")
