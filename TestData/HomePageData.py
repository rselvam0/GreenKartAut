# import openpyxl


class HomePageData:

    @staticmethod
    def getTestDataGK():
        test_Homepage_data = {"searchKeyWord": "roo", "promoCode": "rahulshettyacademy", "productID": "Beetroot - 1 Kg"}
        return [test_Homepage_data]

    @staticmethod
    def getTestData(test_case_name):
        book = openpyxl.load_workbook("E:\\Tech bite\\4_Selenium_Udemy\\PythonDemo.xlsx")
        sheet = book.active
        Dict = {}
        for i in range(1, sheet.max_row + 1):
            if sheet.cell(row=i, column=1).value == test_case_name:
                for j in range(2, sheet.max_column + 1):
                    Dict[sheet.cell(row=1, column=j).value] = sheet.cell(row=i, column=j).value

        return [Dict]

