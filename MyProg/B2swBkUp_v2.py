#!/usr/bin/env python3

import sys
import time
import paramiko
import os
import cmd
import datetime

###set date and time
now = datetime.datetime.now()

###authentication
USER = 'bsquared'
PASSWORD = 'bsquared2019!@#'
secret = 'bsquared2019!@#'

###start FOR ...in
report = "REP_%.2i%.2i%i." % (now.year, now.month, now.day)
ff = open(report, 'a')
f = open('ruckus_switch')
for ip in f.readlines():
    ip = ip.strip()
    ###prefix files for backup  on ELK
    # filename_prefix = '/var/netbackup/' + ip
    # filename_prefix = 'C:/Repo/Python_less/MyProg/' + ip # TMP for debug

    ###session start
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=USER, password=PASSWORD, banner_timeout=60)

    ###ssh shell
    chan = client.invoke_shell()
    time.sleep(2)
    ###enter enable secret
    chan.send('ena\n')
    chan.send(USER + '\n')
    chan.send(secret + '\n')
    time.sleep(1)
    ### command for backUp
    filename = "%s_%.2i%.2i%i" % (ip, now.year, now.month, now.day)
    backupComm = 'copy startup-config tftp 192.168.99.130 /',filename,'\n'
    backupComm = ''.join(backupComm)
    chan.send(backupComm)
    time.sleep(1)
    output = chan.recv(9999)
    ###show output and write file with prefix, date and time
    print(output)
    print(ip,'Done')
    ff.write(output.decode("utf-8"))
    ###close ssh session
    print(ip)
    chan.send('exit\n')
    chan.send('exit\n')
    chan.send('y')
    client.close()
    f.close()
ff.close()