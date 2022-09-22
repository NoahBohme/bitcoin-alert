# Call Coingecko API

import json
import requests
import os
import time


while (True):
    alertprice = 145640

    # Select current
    currency = "dkk"

    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=" + currency

    payload = ""
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    json_data = json.loads(response.text)

    price = json_data["bitcoin"][currency]

    # Check if price drops below alertprice

    def notify(title, text):
        os.system("""
                osascript -e 'display notification "{}" with title "{}"'
                """.format(text, title))

    if price > alertprice:
        os.system('afplay alert.mp3')
        notify("Bitcoin alert", "Bitcoin price is now " +
               str(price) + " " + currency.upper())

    time.sleep(60)
