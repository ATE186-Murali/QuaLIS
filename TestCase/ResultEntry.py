import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from ObjectRepository import Element_Login, Element_ResultEntryBySample
from Utility import BasicOperation

enterResult=215.67

driver = webdriver.Chrome(executable_path="E:\driver1\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://192.168.0.199:9091/QuaLISWeb/#/login")
driver.find_element(By.XPATH, Element_Login.loginid).send_keys("cdolman")
driver.find_element(By.XPATH, Element_Login.password).send_keys("123")

BasicOperation.clickXpath(driver,Element_Login.userRole)

BasicOperation.clickXpath(driver,Element_Login.userRoleSelect)


BasicOperation.clickXpath(driver,Element_Login.login)

BasicOperation.clickXpath(driver, Element_ResultEntryBySample.resultEntry)

BasicOperation.clickXpath(driver, Element_ResultEntryBySample.resultEntryBySample)

BasicOperation.clickXpath(driver, Element_ResultEntryBySample.enterResult)

BasicOperation.sendKeysXpath(driver, Element_ResultEntryBySample.result,enterResult)

BasicOperation.screenshot(driver,"C:\\Users\\Administrator\\PycharmProjects\\nibsc\\Report\\Screenshot\\1.Enter Result.png")

BasicOperation.clickXpath(driver, Element_ResultEntryBySample.saveResult)

time.sleep(5)

BasicOperation.screenshot(driver,"C:\\Users\\Administrator\\PycharmProjects\\nibsc\\Report\\Screenshot\\2.Final Result.png")


actualFinalResult=driver.find_element(By.XPATH, Element_ResultEntryBySample.finalResult).get_attribute("data-tip")

expectedFinalResult=str(round(215.67,1))

print("actualresult", actualFinalResult)

print("expected",expectedFinalResult)

if actualFinalResult.__contains__(expectedFinalResult):
    print("Rounding digit is working")
else:
    print("Rounding digit is not working")

