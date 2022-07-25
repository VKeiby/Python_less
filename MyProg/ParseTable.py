import pandas as pd
import numpy as np
from pyparsing import *

# Pyparsing Learn https://habr.com/ru/post/239081/

# b = 'Interface GigabitEthernet5/1/15(): Ethernet speed <1Gbps'
#
# interface = Word(alphas) # Only int name
# portNum = Word(nums + '/')
# GREEDYDATA = 'Ethernet speed <1Gbps'
# parse_module = 'Interface' + interface + portNum + Suppress('():') + Suppress(GREEDYDATA)
# res = parse_module.parseString(b)
# res[1] = 'ethernet'
# print(' '.join(res))

# -------           END                  ---------

data = pd.read_csv('zbx_problems_export.csv',dtype=object) # load data
print(data.head(1)) # control view
LinkTable = data[['Host','Problem']]

# There is can be subprogram...
# interface = Word(alphas) # Only int name
# portNum = Word(nums + '/')
# GREEDYDATA = 'Ethernet speed <1Gbps'
# parse_module = 'Interface' + interface + portNum + Suppress('():') + Suppress(GREEDYDATA)
# res = parse_module.parseString(b)
# res[1] = 'ethernet'
# print(' '.join(res))
# for i in range (10):
#     fives = input("Input number: ")
#     data.iloc[0,1] = 'rename'
#     if int(fives)==5: sum+=1
# print (sum)




print(LinkTable.Problem)