import urllib3
urllib3.disable_warnings()
# import xlrd for redaing the excel file
import xlrd
import getjanid
# import xlrd for writing to the excel file
#import xlwt
# access test data excel
filename = "D:\Coke - Freestyle\GitHub_Python\Python\janRain.xlsx"
sheetnames = "testresult"
file_location = "D:\Coke - Freestyle\GitHub_Python\Python\janRain.xlsx"
workbook = xlrd.open_workbook(file_location)

# making a writable copy of open excel file
#workbook = copy(sworkbook)
sheet = workbook.sheet_by_index(0)
rwcount = sheet.nrows
print(rwcount)
clcount = sheet.ncols

data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)]
        for r in range(sheet.nrows)]

for svar in data:
    if svar[0] != 'Y':
        continue

    jemail = svar[1]
    print(jemail)
    juuid = svar[2]
    print(juuid)
    getjanid.getjanid(jemail, juuid)
