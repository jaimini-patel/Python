# import xlrd for redaing the excel file
import xlrd
# import xlrd for writing to the excel file
#import xlwt
# access test data excel
filename = "C:\Myproject\Automation\examples1.xlsx"
sheetnames = "testresult"
arrays = [1, 2, 3, 4, 5]
file_location = "C:\Myproject\Automation\examples.xlsx"
workbook = xlrd.open_workbook(file_location)

# making a writable copy of open excel file
#workbook = copy(sworkbook)
sheet = workbook.sheet_by_index(0)
rwcount = sheet.nrows
clcount = sheet.ncols

data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)]
        for r in range(sheet.nrows)]
for svar in data:
    if svar[0] != 'Y':
        continue
    print(svar[0])
    print(svar[1])
    print(svar[2])
    print("=======================")
