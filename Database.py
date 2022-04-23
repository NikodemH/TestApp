from openpyxl import Workbook


def read_multiple(cell):
    text = ws[cell]
    text_split = text.value.split()
    print(text_split)


wb = Workbook()
ws = wb.active

