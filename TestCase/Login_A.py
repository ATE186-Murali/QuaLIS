import time
from configparser import ConfigParser

from selenium import webdriver
from selenium.webdriver.common.by import By

from Utility import Logging, BasicOperation

objectRepository=ConfigParser()
objectRepository.read("C:\\Users\\Administrator\\PycharmProjects\\nibsc\\ObjectRepository\\Element.ini")


testData=ConfigParser()
testData.read("C:\\Users\\Administrator\\PycharmProjects\\nibsc\\login.ini")

configDriver=ConfigParser()
configDriver.read("C:\\Users\\Administrator\\PycharmProjects\\nibsc\\config.ini")


def launchLIMS():



    try:
        driver = webdriver.Chrome(executable_path=configDriver.get("Driver", "chrome"))
        Logging.logInfo("Browser Launched")
        print("Browser Launched")
        driver.maximize_window()
        driver.implicitly_wait(20)

        try:
            driver.get(configDriver.get("Credential", "link"))
            Logging.logInfo("Link was hit")
            print("Link was hit")

            try:
                BasicOperation.sendKeysXpath(driver, objectRepository.get("login", "loginid"),
                                             configDriver.get("Credential", "loginid"))
                Logging.logInfo("Entered Login id")
                print("Entered Login id")

                try:

                    time.sleep(4)
                    BasicOperation.clickXpath(driver, objectRepository.get("login", "password"))

                    BasicOperation.sendKeysXpath(driver, objectRepository.get("login", "password"),
                                                 configDriver.get("Credential", "password"))
                    Logging.logInfo("Entered password id")

                    print("Entered password id")

                    try:
                        time.sleep(3)
                        BasicOperation.clickXpath(driver, objectRepository.get("login", "login"))
                        Logging.logInfo("Clicked the login button")

                        print("Clicked the login button")


                    except Exception as e:
                        Logging.logError("Tried to click the login button, It causes exception" + str(e))

                except Exception as e:
                    Logging.logError("Tried to enter the login id, It causes exception" + str(e))

            except Exception as e:
                Logging.logError("Tried to enter the login id, It causes exception" + str(e))

        except Exception as e:
            Logging.logError("Unable to hit the application, It causes exception" + str(e))



    except Exception as e:
        Logging.logError("Browser is not Launched, It caused exception " + str(e))

    return driver
