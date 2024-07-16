from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
PROMISED_DOWN = 100
PROMISED_UP = 10
X_EMAIL = os.environ.get("X_EMAIL")
X_PASS = os.environ.get("X_PASS")
X_USERNAME = os.environ.get("X_USERNAME")


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_options)
        self.down = ""
        self.up = ""

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        time.sleep(1)

        go_button = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                             '3]/div[1]/a')
        go_button.click()
        time.sleep(60)

        self.down = float(self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div['
                                                                   '2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div['
                                                                   '1]/div[1]/div/div[2]/span').text)
        self.up = float(self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div['
                                                                 '2]/div[3]/div[3]/div/div[3]/div/div/div[2]/di'
                                                                 'v[1]/div[2]/div/div[2]/span').text)

        print(f"up: {self.up}")
        print(f"down: {self.down}")

    def tweet_at_provider(self):
        self.driver.get("https://x.com/i/flow/login")

        time.sleep(5)
        x_user_texbox = self.driver.find_element(by=By.XPATH,
                                                 value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                       '2]/div/div/div[2]/div[2]/div/div/div/div['
                                                       '4]/label/div/div[2]/div/input')
        x_next_button = self.driver.find_element(by=By.XPATH,
                                                 value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                       '2]/div/div/div[2]/div[2]/div/div/div/button[2]')
        x_user_texbox.send_keys(X_EMAIL)
        x_next_button.click()

        time.sleep(2)
        second_username_textbox = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div['
                                                                              '2]/div/div/div/div/div/div[2]/div['
                                                                              '2]/div/div/div[2]/div[2]/div['
                                                                              '1]/div/div[2]/label/div/div['
                                                                              '2]/div/input')
        second_username_textbox.send_keys(X_USERNAME)
        second_username_textbox.send_keys(Keys.ENTER)

        time.sleep(2)
        x_pass_textbox = self.driver.find_element(by=By.XPATH,
                                                  value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                        '2]/div/div/div[2]/div[2]/div[1]/div/div/div['
                                                        '3]/div/label/div/div[2]/div[1]/input')
        x_pass_textbox.send_keys(X_PASS)
        x_pass_textbox.send_keys(Keys.ENTER)

        time.sleep(5)
        tweet_textbox = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div['
                                                                    '2]/main/div/div/div/div/div/div[2]/div/div['
                                                                    '2]/div[1]/div/div/div/div[2]/div['
                                                                    '1]/div/div/div/div/div/div/div/div/div/div['
                                                                    '1]/div/div/div/div[2]/div/div/div/div')
        tweet_textbox.send_keys(
            f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for "
            f"100down/10up?")
        time.sleep(3)
        send_tweet_button = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div['
                                                                        '2]/main/div/div/div/div/div/div[2]/div/div['
                                                                        '2]/div[1]/div/div/div/div[2]/div['
                                                                        '4]/div/div/div[2]/div[3]')
        send_tweet_button.click()
        time.sleep(2)
        self.driver.quit()
