#!/usr/bin/env python3

import sys
import time

import numpy
import paramiko
import os
import cmd
import datetime
import pandas as pd
import numpy as np
from pyparsing import Word, alphas, restOfLine, Suppress, nums

# Pyparsing Learn https://habr.com/ru/post/239081/
# b = 'Interface GigabitEthernet5/1/15(): Ethernet speed <1Gbps'
# interface = Word(alphas) # Only int name
# portNum = Word(nums + '/')
# GREEDYDATA = 'Ethernet speed <1Gbps'
# parse_module = 'Interface' + interface + portNum + Suppress('():') + Suppress(GREEDYDATA)
# res = parse_module.parseString(b)
# res[1] = 'ethernet'
# print(' '.join(res))
# -------                 END                  ---------

data = pd.read_csv('zbx_problems_export.csv', dtype=object) # load data
# print(data) # control view
# print (data.columns)

LinkTable = data[['Host','Problem']]

# LinkTable.drop(labels=[0],axis=0) #How Delete Head? ..or ignore


# There is can be subprogram...
interface = Word(alphas) # Only int name
portNum = Word(nums + '/')
GREEDYDATA = restOfLine()
parse_module = Suppress(interface) + interface + portNum + Suppress(GREEDYDATA)
for i in range (15):
    # https://pandas.pydata.org/docs/user_guide/10min.html    #How to change & read cell in dataframe
    res = parse_module.parseString(LinkTable['Problem'].iloc[i])
    res[0] = 'ethernet'
    res = ' '.join(res)
    LinkTable.iat[i,1] = res

print(LinkTable)
# LinkTable.to_csv('LinkTable.csv') # out file

# ---------------------------------------------------------------------
###set date and time
now = datetime.datetime.now()

###authentication
USER = 'bsquared'
PASSWORD = 'bsquared2019!@#'
secret = 'bsquared2019!@#'

##start FOR ...in
f = open('LinkTable.csv')
for ip in f.readlines():
    ip = ip.strip()
    ipSTR = ip.split(',')
    # print(ipSTR[2])
    ###prefix files for backup  - filename_prefix = '/var/netbackup/' + ip
    filename_prefix = 'C:/Repo/Python_less/MyProg/' + ip # TMP for debug

    ###session start
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ipSTR[1], username=USER, password=PASSWORD)

    ###ssh shell
    chan = client.invoke_shell()
    time.sleep(2)
    ###enter enable secret
    chan.send('ena\n')
    chan.send(USER + '\n')
    chan.send(secret + '\n')
    time.sleep(1)
    ###terminal lenght for no paging
    chan.send('skip\n')
    time.sleep(1)
    ###show config and write output
    chan.send('sh lldp neigh det po '+ipSTR[2]+'\n')
    time.sleep(10)
    output = chan.recv(999999)
    ###show output config and write file with prefix, date and time
    print(output)
    # filename = "%s_%.2i-%.2i-%i_%.2i-%.2i-%.2i" % (filename_prefix,now.day,now.month,now.year,now.hour,now.minute,now.second)
    filename = "212112" # % (filename_prefix, now.year, now.month, now.day, now.hour, now.minute, now.second)
    ff = open(filename, 'a')
    # ff.write(output)
    ff.write(output.decode("utf-8"))
    ff.close()
    ###close ssh session
    client.close()

    print(ip)
    f.close()

