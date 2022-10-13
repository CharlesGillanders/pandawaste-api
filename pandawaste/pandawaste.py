import requests
#import time
#import csv
#import re
import logging

from bs4 import BeautifulSoup
from datetime import datetime


logger = logging.getLogger(__name__)

from voluptuous import Optional

BASEURL = "https://www.mypanda.ie/"

class pandawaste:
    """Class for Panda Waste"""
    def __init__(self, accountcode, pin):
        """Initialize"""
        self._accountcode = accountcode
        self._pin = pin
        self._session = requests.Session()
        


    async def scrapelogin(self):
        """Scrape Login Page"""

        try:
            formatted_url = BASEURL + "Account/Login"
            html_text = self._session.get(formatted_url).text
            soup = BeautifulSoup(html_text,"html.parser")
            RequestVerificationToken = soup.find("input", attrs={"name": "__RequestVerificationToken"})['value']
            payload= 'ReturnUrl=%2F&Username='+self._accountcode+'&Password='+self._pin+'&RememberMe=true&__RequestVerificationToken='+RequestVerificationToken+'&RememberMe=false'
            headers = {'Referer':'https://www.mypanda.ie/Account/Login',
            'Origin':'https://www.mypanda.ie',
            'Connection':'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Content-Type': 'application/x-www-form-urlencoded'
            }
            Response = self._session.post(formatted_url,data=payload,headers=headers)
            Response.raise_for_status()
            return True
        except Exception as e:
            logger.debug(e)
            return e
    
    async def scrapelifts(self):
        """Scrape bin lifts"""

        try:
            formatted_url = BASEURL + "Lifts"
            html_text = self._session.get(formatted_url).text
            soup = BeautifulSoup(html_text,"html.parser")
            liftstable = soup.find("table",attrs={'recent-lifts-data-table'}).find("tbody").find_all("tr")
            lifts = []
            for lift in liftstable:
                liftdate = datetime.strptime(lift.find_all("td")[0].text, '%d/%m/%Y')
                lifttype = lift.find_all("td")[2].text
                liftweight = float(lift.find_all("td")[3].text)
                liftentry = {'date':liftdate,'type':lifttype,'weight':liftweight}
                lifts.append(liftentry)
            return lifts
        except Exception as e:
            logger.debug(e)
            return e

    #Home/NextCollections

    async def scrapecollections(self):
        """Scrape bin collections"""

        try:
            formatted_url = BASEURL + "Home/NextCollections"
            html_text = self._session.get(formatted_url).text
            soup = BeautifulSoup(html_text,"html.parser")
            collectionstable = soup.find("table").find("tbody").find_all("tr")
            collections = []
            for collection in collectionstable:
                collectiondate = datetime.strptime(collection.find_all("td")[0].text, '%d/%m/%Y')
                collectiontype = collection.find_all("td")[2].find("span",attrs={'style':None}).text
                collectionentry = {'date':collectiondate,'type':collectiontype}
                collections.append(collectionentry)
            return collections
        except Exception as e:
            logger.debug(e)
            return e
