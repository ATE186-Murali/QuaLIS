from configparser import ConfigParser

from selenium import webdriver

from Utility import Logging

objectRepository=ConfigParser()
objectRepository.read("C:\\Users\\Administrator\\PycharmProjects\\nibsc\\login.ini")

testData=ConfigParser()
testData.read("C:\\Users\\Administrator\\PycharmProjects\\nibsc\\login.ini")

configDriver=ConfigParser()
configDriver.read("C:\\Users\\Administrator\\PycharmProjects\\nibsc\\config.ini")

try:
    driver = webdriver.Chrome(executable_path=configDriver.get("Driver","chrome"))
    Logging.logInfo("Browser Launched")
    driver.maximize_window()
    driver.implicitly_wait(30)



except Exception as e:
    Logging.logError("Browser is not Launched, It caused exception "+str(e))

