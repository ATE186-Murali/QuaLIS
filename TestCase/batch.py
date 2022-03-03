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

BasicOperation.clickXpath(driver,"//*[@id='app-wrapper']/div[1]/div[2]/div[1]/ul/div/li[5]/a")

BasicOperation.clickXpath(driver,"//a[@href='#/batchCreation']")

BasicOperation.clickXpath(driver,"//*[@data-tip='Add']")


driver.find_element(By.XPATH, "//*[text()='Select Record...']").send_keys("Albumins")