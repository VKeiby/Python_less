#!/usr/bin/python3
# snmpwalk -c PROinit -v 2c 172.18.1.202 1.0.8802.
import argparse
import json
import subprocess, shlex

# передаем сюда результат subprocess.check_output(call_args)
def data_constructor(snmpwalk_output):
    global cmd
    data = {'data': []}
    ip = cmd.split()[-2]
    snmpwalk_output_rows = [row for row in snmpwalk_output.decode('utf-8').split('\n') if row]
    for row in snmpwalk_output_rows:
        localifindex = row.split()[0].split('.')[-2]
        ifadvindex = '{0}.{1}'.format(localifindex, row.split()[0].split('.')[-1])
        command = 'snmpget -c PROinit -v2c {0} 1.0.8802.1.1.2.1.3.7.1.3.{1}'.format(ip, localifindex)
        localifname = subprocess.check_output(shlex.split(command)).decode('utf-8').split()[-1].replace('"','')
        data['data'].append({'{#LOCALIFINDEX}': localifindex,
                             '{#LOCALIFNAME}': localifname,
                             '{#IFADVINDEX}': ifadvindex})
        #print('ToJson:', localifindex, localifname, ifadvindex)
    return data

parser = argparse.ArgumentParser()
parser.add_argument('ip')
parser.add_argument('snmpparam')
args = parser.parse_args()


cmd = 'snmpwalk {0} {1} 1.0.8802.1.1.2.1.4.1.1.7.0'.format(args.snmpparam, args.ip)
call_args = shlex.split(cmd)

output = subprocess.check_output(call_args)

print(json.dumps(data_constructor(output)))
