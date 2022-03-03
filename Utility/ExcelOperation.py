import openpyxl
from Utility.BasicOperation  import *
def writeExcel(loc, sheet,row,column,value):
    loc = "D:\\python\\nibsc.xlsx"
    workbook = openpyxl.load_workbook(loc)
    sheet = workbook[sheet]
    sheet.cell(row, column).value=value
    time1=time()
    print(time1)
    workbook.save(loc)

