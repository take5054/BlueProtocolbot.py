import openpyxl as excel
def named(msg):
    data = openpyxl.load_workbook('nameddata.xlsx')
    for row in data.iter_rows(min_row=1,min_col=1,max_row=50,max_col=50):
        for cell in col:
            if 'A5' in msg:
                return '114514'
    return 'test'