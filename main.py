import requests
import defs
import logging

logger = logging.getLogger(__name__)


def maincycle(API_URL, HEADERS, PAYLOAD):
    logging.basicConfig(level=logging.INFO)
    req = requests.request("POST", API_URL, headers=HEADERS, data=PAYLOAD)
    data = req.json()
    # logging
    logger.info("Status: %s", req.status_code)
    logger.info("User ID: %s", data["clickerUser"]["id"])
    logger.info("Total Conis: %s", data["clickerUser"]["totalCoins"])
    logger.info("Balance Coins: %s", data["clickerUser"]["balanceCoins"])
    logger.info("Level: %s", data["clickerUser"]["level"])
    logger.info("Avaliable Taps: %s", data["clickerUser"]["availableTaps"])
    logger.info("Maximum Taps: %s", data["clickerUser"]["maxTaps"])


if __name__ == '__main__':
    maincycle(API_URL=defs.API_URL, HEADERS=defs.HEADERS, PAYLOAD=defs.PAYLOAD)

#https://hamsterkombatgame.io/clicker#tgWebAppData=query_id%3DAAHj3BckAwAAAOPcFyQ8TB2K%26user%3D%257B%2522id%2522%253A7047994595%252C%2522first_name%2522%253A%2522watafuck%2522%252C%2522last_name%2522%253A%2522%2522%252C%2522username%2522%253A%2522xdxdxdxdxdxdxdow%2522%252C%2522language_code%2522%253A%2522ru%2522%252C%2522allows_write_to_pm%2522%253Atrue%257D%26auth_date%3D1721348890%26hash%3De22a3d38392d91119a38155900e9c0f8630e4a49026439359802e5da70eb28e2&tgWebAppVersion=7.6&tgWebAppPlatform=android&tgWebAppThemeParams=%7B%22bg_color%22%3A%22%23212121%22%2C%22button_color%22%3A%22%238774e1%22%2C%22button_text_color%22%3A%22%23ffffff%22%2C%22hint_color%22%3A%22%23aaaaaa%22%2C%22link_color%22%3A%22%238774e1%22%2C%22secondary_bg_color%22%3A%22%23181818%22%2C%22text_color%22%3A%22%23ffffff%22%2C%22header_bg_color%22%3A%22%23212121%22%2C%22accent_text_color%22%3A%22%238774e1%22%2C%22section_bg_color%22%3A%22%23212121%22%2C%22section_header_text_color%22%3A%22%238774e1%22%2C%22subtitle_text_color%22%3A%22%23aaaaaa%22%2C%22destructive_text_color%22%3A%22%23ff595a%22%7D
