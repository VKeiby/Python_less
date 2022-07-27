import pandas as pd
import numpy as np
from pyparsing import *

# Pyparsing Learn https://habr.com/ru/post/239081/
# b = 'Interface GigabitEthernet5/1/15(): Ethernet speed <1Gbps'
# interface = Word(alphas) # Only int name
# portNum = Word(nums + '/')
# GREEDYDATA = 'Ethernet speed <1Gbps'
# parse_module = 'Interface' + interface + portNum + Suppress('():') + Suppress(GREEDYDATA)
# res = parse_module.parseString(b)
# res[1] = 'ethernet'
# print(' '.join(res))
# -------           END                  ---------

data = pd.read_csv('zbx_problems_export.csv',dtype=object) # load data
# print(data.head(1)) # control view
LinkTable = data[['Host','Problem']]

# There is can be subprogram...
interface = Word(alphas) # Only int name
portNum = Word(nums + '/')
GREEDYDATA = restOfLine()
parse_module = 'Interface' + interface + portNum + Suppress(GREEDYDATA)
for i in range (15):
    res = parse_module.parseString(LinkTable['Problem'].iloc[i])
    res[1] = 'ethernet'
    res = ' '.join(res)
    LinkTable.iat[i,1] = res
print(LinkTable.head())
print(data.head())
# https://pandas.pydata.org/docs/user_guide/10min.html