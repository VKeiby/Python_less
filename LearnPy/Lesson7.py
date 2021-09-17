# This Python file uses the following encoding: utf-8
#
# with open('data_car', 'w') as f:
#   f.write('Volvo,V90,3.0l,15l/1k,3kk')
from datetime import datetime

start_time = datetime.now()

import csv

with open('data_car') as f:
  reader = csv.reader(f, delimiter=',')
  for row in reader:
    print(row)

from docxtpl import DocxTemplate

def get_context(row):  # возвращает словарь аргуменов
  Brand = row[0]
  Model = row[1]
  FuelCons = row[2]
  Capacity = row[3]
  Value = row[4]
  return {
    'Brand': Brand,
    'Model': Model,
    'FuelCons': FuelCons,
    'Capacity': Capacity,
    'Value': Value
  }

def from_template(row, template):
  template = DocxTemplate(template)
  context = get_context(row)  # gets the context used to render the document
  template.render(context)

  template.save(str(datetime.now().date()) + '_report.docx')


def generate_report(row):
  template = 'report.docx'
  document = from_template(row, template)

def toFixed(numObj, digits=0):
  return f"{numObj:.{digits}f}"


generate_report(row)
finish_time = datetime.now() - start_time
print(finish_time)


car_data = [['Brand','Model','FuelCons','Capacity','Value'],row]
with open('../report.csv', 'w') as f:
  writer = csv.writer(f)  #
  writer.writerows(car_data)
print('Writing csv file complete!')
finish_time = datetime.now() - start_time
print(finish_time)

# with open('report.csv') as f:
#   reader = csv.reader(f, delimiter=',')
#   for rw in reader:
#     print(rw)

import json
dictJS = get_context(row)
with open('../dict_to_json.json', 'w') as f:
  json.dump(dictJS, f)
  print('Writing json file complete!')
finish_time = datetime.now() - start_time
print(finish_time)

