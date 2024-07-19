import json
import calendar
import time


def getTimestamp():
    return calendar.timegm(time.gmtime())


AUTH_TOKEN = 'API_TOKEN_HERE'
CLICKER_COUNT = 1500

API_URL = "https://api.hamsterkombatgame.io/clicker/tap"
PAYLOAD = json.dumps({"count": CLICKER_COUNT, "availableTaps": 0, "timestamp": getTimestamp()})
HEADERS = {'Authorization': f'Bearer {AUTH_TOKEN}', 'Content-Type': 'application/json'}
