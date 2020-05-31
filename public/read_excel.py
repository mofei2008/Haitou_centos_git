import xlrd
from public import read_excel1
#from xlutils.copy import copy

class ExcelUtil:
    def __init__(self,excel_path=None,index=None):
        if excel_path  == None:
            excel_path = r'E:\Test\Haitou\test_data\test_data.xlsx'
        if index ==None:
            index = 0
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheets()[index]
        self.rows = self.table.nrows
        # print(self.rows)
    # def get_sheet_by_name(self,name):
    #     self.sheet = self.data.sheet_by_name(name)
    #     return self.get_data()

    def get_data(self):
        result = []
        for i in range(1,self.rows):
            col = self.table.row_values(i)
            # print(col)
            result.append(col)
        return result

    def write_data(self,row,value):
        data = self.data
        print(data)
        write_data = copy(data)
        print(write_data)
        write_data.get_sheet(0).write(row,7,value)
        write_data.save(r'E:\Test\Haitou\test_data\keywords.xlsx' )
    def get_col_value(self,row,col):
        if self.get_lines() >= row:
            data = self.table.cell(row,col).value
            return data
        return None
    def get_lines(self):
        rows = self.table.nrows
        print(rows)
        if rows>=1:
            return rows
        return None



if __name__ =="__main__":
    # datainfo = XLDatainfo(r'E:\Test\Haitou\test_data\test_data.xlsx')
    # alldata = datainfo.get_sheetinfo_by_name('H5')
    # print(alldata)
    # x1 = XLDatainfo
    # testfile = 'test_data.xlsx'
    # H5 = x1.get_sheet_data('test_data.xlsx', 'H5')
    # print(H5)c
    a = ExcelUtil(r'E:\Test\Haitou\test_data\keywords.xlsx')
    # a.write_data(5,'fasfas')
    print(a.get_col_value(1,6))