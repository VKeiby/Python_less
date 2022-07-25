#!/usr/bin/env python3

import sys
import time
import paramiko
import os
import cmd
import datetime
import pandas as pd
import numpy as np


###set date and time
now = datetime.datetime.now()

###authentication
USER = 'bsquared'
PASSWORD = 'bsquared2019!@#'
secret = 'bsquared2019!@#'

###start FOR ...in
f = open('ruckus_switch')
for ip in f.readlines():
    ip = ip.strip()
    ###prefix files for backup  - filename_prefix = '/var/netbackup/' + ip
    filename_prefix = 'C:/Repo/Python_less/MyProg/' + ip # TMP for debug

    ###session start
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=USER, password=PASSWORD)

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
    chan.send('sh run\n')
    time.sleep(10)
    output = chan.recv(999999)
    ###show output config and write file with prefix, date and time
    print(output)
    # filename = "%s_%.2i-%.2i-%i_%.2i-%.2i-%.2i" % (filename_prefix,now.day,now.month,now.year,now.hour,now.minute,now.second)
    filename = "%s_%.2i%.2i%i_%.2i%.2i%.2i" % (
    filename_prefix, now.year, now.month, now.day, now.hour, now.minute, now.second)
    ff = open(filename, 'a')
    # ff.write(output)
    ff.write(output.decode("utf-8"))
    ff.close()
    ###close ssh session
    client.close()

    print(ip)
    f.close()