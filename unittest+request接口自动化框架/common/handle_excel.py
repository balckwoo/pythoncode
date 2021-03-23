"""
========================================
# Author: Alem
# Email: chengrichong@foxmail.com  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Two roads diverged in a wood,and I 
# I took the one less traveled by, 
# And that has made all the difference. 
=========================================

"""
import openpyxl


class Test_case:

    def __init__(self, file_name, sheet_name):
        self.filename = file_name
        self.sheet_name = sheet_name

    def open_excel(self):
        self.wb = openpyxl.load_workbook(self.filename)
        self.sh = self.wb[self.sheet_name]

    def test_cases(self):
        self.open_excel()
        res = list(self.sh.rows)
        title = []
        test_case = []
        for i in res[0]:
            title.append(i.value)
        for j in res[1:]:
            data = []
            for k in j:
                data.append(k.value)
            case = dict(zip(title, data))
            test_case.append(case)
        return test_case

    def write_case(self, row, coulmn, value):
        self.open_excel()
        self.sh.cell(row=row, column=coulmn, value=value)
        self.wb.save(self.filename)
