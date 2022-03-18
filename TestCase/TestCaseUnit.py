from configparser import ConfigParser

from TestCase import Login_A
from TestCoverage import TestCoverageUnit
from Utility import BrowserOperation


testData=ConfigParser()
testData.read("C:\\Users\\Administrator\\PycharmProjects\\nibsc\\TestData\\TestDataTestCoverageBaseMaster.ini")


driver=Login_A.launchLIMS()
#TestCoverageUnit.unitAdd(driver,testData.get("Unit","unitAddName"),testData.get("Unit","unitAddDescription"))

# TestCoverageUnit.unitEdit(driver,"driver","driver1")

TestCoverageUnit.unitDelete(driver,"driver1")