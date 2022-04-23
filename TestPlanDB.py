import Database as db


db.ws['A1'] = "TP ID"
db.ws['B1'] = "TCD ID"
db.ws['A2'] = "1"
db.ws['B2'] = "1 2 3"
db.wb.save("TestPlan.xlsx")