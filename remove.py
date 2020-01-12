import sys
from selenium import webdriver
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("username")
password = os.getenv("password")
reponame = sys.argv[1]

browser = webdriver.Chrome(
    executable_path='/Users/harisbeslic/Documents/chrome/chromedriver')
browser.get('http://github.com/login')


def remove():
    browser.find_elements_by_xpath(
        "//input[@name='login']")[0].send_keys(username)
    browser.find_elements_by_xpath(
        "//input[@name='password']")[0].send_keys(password)
    browser.find_elements_by_xpath("//input[@name='commit']")[0].click()
    browser.get('https://github.com/' + username +
                '/' + reponame + '/settings')
    browser.find_elements_by_xpath(
        '/html/body/div[4]/div/main/div[2]/div/div/div[2]/div/div[8]/ul/li[4]/details/summary')[0].click()
    browser.find_elements_by_xpath(
        '/html/body/div[4]/div/main/div[2]/div/div/div[2]/div/div[8]/ul/li[4]/details/details-dialog/div[3]/form/p/input')[0].send_keys(username + '/' + reponame)
    browser.find_elements_by_xpath(
        '/html/body/div[4]/div/main/div[2]/div/div/div[2]/div/div[8]/ul/li[4]/details/details-dialog/div[3]/form/button')[0].click()
    browser.get("https://github.com/" + username)
    browser.quit()


if __name__ == "__main__":
    remove()
