import sys
import logging
import asyncio

from pandawaste.pandawaste import pandawaste

if len(sys.argv) != 3:
    accountcode = input("accountcode: ")
    pin = input("pin: ")
else:
    accountcode = sys.argv[1]
    pin = sys.argv[2]

logger = logging.getLogger('')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('[%(asctime)s] %(levelname)s [%(filename)s.%(funcName)s:%(lineno)d] %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')
handler.setFormatter(formatter)
logger.addHandler(handler)

async def main():
    logger.debug("instantiating Panda Waste Scraping Client")

    client: pandawaste = pandawaste(accountcode,pin)

    logger.debug("Scraping...")
    try:
        logger.debug("Login")
        await client.scrapelogin()
        logger.debug("Lifts")
        lifts = await client.scrapelifts()
        logger.info(lifts)
        logger.debug("Collections")
        collections = await client.scrapecollections()
        logger.info(collections)
    except Exception as e:
        logger.error(e)


asyncio.run(main())
