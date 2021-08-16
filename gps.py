from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
import paths
from selenium.webdriver.common.keys import Keys


def log_in(email, password, email_area, pass_area):
    email_area.click()
    email_area.send_keys(email)
    pass_area.click()
    pass_area.send_keys(password)
    pass_area.send_keys(Keys.ENTER)


class Bot:
    # hints
    youtube_window: WebDriver
    facebook_window: WebDriver
    discord_window: WebDriver
    browser_window: WebDriver

    # websites
    def open_website(self, website):
        try:
            if website == "youtube":
                self.youtube_window = webdriver.Chrome(paths.chromedriver_path)
                self.youtube_window.get("https://www.youtube.com/")
                button = self.youtube_window.find_element_by_xpath(paths.youtube_button_path)
                button.click()
            elif website == "facebook":
                self.facebook_window = webdriver.Chrome(paths.chromedriver_path)
                self.facebook_window.get("https://www.facebook.com/")
                button = self.facebook_window.find_element_by_xpath(paths.facebook_button_path)
                button.click()
            elif website == "discord":
                self.discord_window = webdriver.Chrome(paths.chromedriver_path)
                self.discord_window.get("https://www.discord.com")
                button = self.discord_window.find_element_by_xpath(paths.discord_button_path)
                button.click()
            elif website == "browser":
                self.browser_window = webdriver.Chrome(paths.chromedriver_path)
                self.browser_window.get("https://duckduckgo.com/")
        except(ValueError, Exception):
            pass

    # login
    def login(self):
        try:
            email_area = self.facebook_window.find_element_by_xpath(paths.email_area_facebook_path)
            pass_area = self.facebook_window.find_element_by_xpath(paths.pass_area_facebook_path)
            log_in(paths.facebookEmail, paths.facebookPass, email_area, pass_area)
        except(ValueError, Exception):
            pass

        try:
            email_area = self.discord_window.find_element_by_css_selector(paths.email_area_discord_path)
            pass_area = self.discord_window.find_element_by_css_selector(paths.pass_area_discord_path)
            log_in(paths.discordEmail, paths.discordPass, email_area, pass_area)
        except(ValueError, Exception):
            pass


program = Bot()
