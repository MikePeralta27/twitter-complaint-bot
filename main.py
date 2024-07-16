from internet_speed_twitter_bot import InternetSpeedTwitterBot
PROMISED_DOWN = 100
PROMISED_UP = 10
CHROME_DRIVER_PATH = "/Users/mkprt/Development/chromedriver"


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

input("Press any key to close the browser...")

bot.driver.close()

