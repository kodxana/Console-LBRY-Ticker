import requests
import json
import time
import datetime
import os
import sys
import logging
import logging.handlers
import argparse
import configparser
import traceback
from pygame import mixer

get_price_url = "https://api.coingecko.com/api/v3/simple/price?ids=lbry-credits&vs_currencies=usd"
price_query= requests.get(get_price_url)
price_json = price_query.json()
price_usd = price_json["lbry-credits"]["usd"]
latest_price = price_usd
start_time = time.time()

try:
    while True:
        time_left = 2 - (time.time() - start_time) / 60
        if time_left < 0:
            time_left = 0
        print("Time left: " + str(time_left) + " minutes")
        price_query= requests.get(get_price_url)
        price_json = price_query.json()
        price_usd = price_json["lbry-credits"]["usd"]
        mixer.init()
        # Print current price in USD
        print("\nCurrent price: " + str(price_usd) + " USD")
        if price_usd != latest_price:
            if price_usd > latest_price:
                print("\nPrice increased to " + str(price_usd) + " USD")
                mixer.music.load("01-oh-yeah.m.mp3")
                mixer.music.play()
            else:
                print("\nPrice decreased to " + str(price_usd) + " USD")
                mixer.music.load("Sad Violin.mp3")
                mixer.music.play()
            latest_price = price_usd
        time.sleep(120)
except KeyboardInterrupt:
    print("Exiting")
    sys.exit(0)
except Exception as e:
    print("Error: " + str(e))
    traceback.print_exc()
    sys.exit(1)
except:
    print("Unknown error")
    traceback.print_exc()
    sys.exit(1)
finally:
    print("Exiting")
    sys.exit(0)
