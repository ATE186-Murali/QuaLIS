from Utility import BrowserOperation
from Utility.BrowserOperation import *

from Utility.ExcelOperation import *

# Open link
#
#
# result=case[0]
# actualResult=case[1]

ResultFlagColumn=8
ActualFlagColumn=7

writeExcel("D:\\python\\nibsc.xlsx","usermanagement",2,ResultFlagColumn,result[0])
writeExcel("D:\\python\\nibsc.xlsx","usermanagement",2,ActualFlagColumn,actualResult[0])

writeExcel("D:\\python\\nibsc.xlsx","usermanagement",3,ResultFlagColumn,result[1])
writeExcel("D:\\python\\nibsc.xlsx","usermanagement",3,ActualFlagColumn,actualResult[1])

writeExcel("D:\\python\\nibsc.xlsx","usermanagement",4,ResultFlagColumn,result[2])
writeExcel("D:\\python\\nibsc.xlsx","usermanagement",4,ActualFlagColumn,actualResult[2])