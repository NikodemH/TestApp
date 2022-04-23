import Database as db

db.ws['A1'] = "TCD ID"
db.ws['B1'] = "TP ID"
db.ws['C1'] = "TC ID"

db.ws['A2'] = "1"
db.ws['A3'] = "2"



db.wb.save("TestCaseDefinition.xlsx")