import time
from configparser import ConfigParser
from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from TestCase.Login_A import objectRepository
from Utility import BasicOperation, Logging

configDriver = ConfigParser()
configDriver.read("C:\\Users\\Administrator\\PycharmProjects\\nibsc\\ObjectRepository\\ElementBaseMaster.ini")


def unitAdd(driver, name, description):
    try:
        BasicOperation.clickXpath(driver, configDriver.get("UnitOfMeasurement", "masterIcon"))

        Logging.logInfo("Clicked Master Icon")

        print("Clicked Master Icon")

        time.sleep(3)
        try:

            time.sleep(3)

            BasicOperation.clickXpath(driver, configDriver.get("UnitOfMeasurement", "baseMasterIcon"))

            Logging.logInfo("Clicked Base Master Icon")

            print("Clicked Base Master Icon")

            try:
                time.sleep(3)
                BasicOperation.clickXpath(driver, configDriver.get("UnitOfMeasurement", "unitOfMeasurementIcon"))
                Logging.logInfo("Cliecked Unit Icon")

                print("Cliecked Unit Icon")

                try:
                    time.sleep(3)
                    BasicOperation.clickXpath(driver, configDriver.get("UnitOfMeasurement", "unitAdd"))
                    Logging.logInfo("Clicked Add Button")
                    print("Clicked Add Button")

                    try:

                        BasicOperation.sendKeysXpath(driver, configDriver.get("UnitOfMeasurement", "unitName"), name)

                        Logging.logInfo("Entered unit name")

                        print("Entered unit name")

                        try:
                            BasicOperation.sendKeysXpath(driver,
                                                         configDriver.get("UnitOfMeasurement", "unitDescription"),
                                                         description)

                            Logging.logInfo("entered unit description")

                            print("entered unit description")
                            try:

                                BasicOperation.clickXpath(driver,
                                                          configDriver.get("UnitOfMeasurement", "unitAddSubmit"))
                                Logging.logInfo("Clicked the Unit Add submit Button")

                                print("Clicked the Unit Add submit Button")

                                try:

                                    # Wait for initialize, in seconds
                                    wait = WebDriverWait(driver, 10)

                                    wait.until(EC.visibility_of_element_located(
                                        configDriver.get("UnitOfMeasurement", "unitAdd")))

                                    Logging.logInfo("Add popup is closed")
                                except:
                                    Logging.logError("Add popup is not closed")


                            except Exception as e:
                                Logging.logError(
                                    "Tried to click the Unit Add submit button, It causes exception" + str(e))

                                raise Exception

                                raise Exception



                        except Exception as e:
                            Logging.logError(
                                "Tried to enter the unit description detail, It causes exception" + str(e))

                    except Exception as e:
                        Logging.logError(
                            "Tried to enter the unit name detail, It causes exception" + str(e))

                except Exception as e:
                    Logging.logError("Tried to click the Unit add button, It causes exception" + str(e))


            except Exception as e:
                Logging.logError("Tried to click the Unit screen icon, It causes exception" + str(e))

        except Exception as e:
            Logging.logError("Tried to click the Base Master Icon, It causes exception" + str(e))


    except Exception as e:
        Logging.logError("Tried to enter the Master Icon, It causes exception" + str(e))


def unitEdit(driver):
    print()
    BasicOperation.clickXpath(driver, configDriver.get("UnitOfMeasurement", "masterIcon"))

    BasicOperation.clickXpath(driver, configDriver.get("UnitOfMeasurement", "baseMasterIcon"))

    BasicOperation.clickXpath(driver, configDriver.get("UnitOfMeasurement", "unitOfMeasurementIcon"))



    a= driver.find_elements(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[3]/div/div[1]/table/tbody/tr/td[1]")

    print(str(len(a)))

    b=0
    for i in a:
        print(b)
        print(i.text)
        b=b+1




def unitDelete():
    print()


def unitRefresh():
    print()


def unitExportPDF():
    print()


def unitExportExcel():
    print()