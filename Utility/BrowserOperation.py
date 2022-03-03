import time

from selenium.webdriver.common.by import By

from ObjectRepository.Element_Login import *
from ObjectRepository.Element_ResultEntryBySample import *

from selenium import webdriver

linkLoad="false"



def launchBrowser():
    global driver
    driver = webdriver.Chrome(executable_path="E:\driver1\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(30)


def launchLIMS():
    actualResult=[]
    result=[]

    testCaseResult_ID001="UN-EXECUTED"
    actualResult_ID001="UN-EXECUTED"

    testCaseResult_ID002="UN-EXECUTED"
    actualResult_ID002="UN-EXECUTED"

    testCaseResult_ID003="UN-EXECUTED"
    actualResult_ID003="UN-EXECUTED"



    try:
       launchBrowser()
       driver.get("http://192.168.0.199:9091/QuaLISWeb/#/login")

       welcome=driver.find_element(By.XPATH,welcomeText).text



       actualResult_ID001="Welcome message displayed"
       testCaseResult_ID001="PASS"

       try:
           driver.find_element(By.XPATH, loginid).send_keys("cdolman")
           time.sleep(4)
           driver.find_element(By.XPATH, password).click()

           try:
            userrole= driver.find_element(By.XPATH, "//*[text()='Admin']")
            actualResult_ID002="Correct userrole is loaded"
            testCaseResult_ID002="PASS"
           except:
               actualResult_ID002 = "Correct userrole is not loaded"
               testCaseResult_ID002 = "FAIL"

           try:
               userrole = driver.find_element(By.XPATH, "//*[text()='Internal']")
               actualResult_ID003 = "Correct login type is loaded"
               testCaseResult_ID003 = "PASS"
           except:
               actualResult_ID003 = "Correct  login type is not loaded"
               testCaseResult_ID003 = "FAIL"

           try:
               driver.find_element(By.XPATH, password).send_keys("123")

           except:
               print("Unable to enter the password")


           try:
               driver.find_element(By.XPATH, login).click()
           except:
                print("Unable to click the login button")

       except:
           print()

    except:
       case1="FAIL"

       actualResult_ID001 = "Welcome message displayed is not displayed"



    result.append(testCaseResult_ID001)

    result.append(testCaseResult_ID002)

    result.append(testCaseResult_ID003)

    actualResult.append(actualResult_ID001)

    actualResult.append(actualResult_ID002)

    actualResult.append(actualResult_ID003)

    output=[result,actualResult]

    return output

def resultEntry():
    driver.find_element(By.XPATH,resultEntry()).text