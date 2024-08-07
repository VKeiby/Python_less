import socket
import time
import datetime
from pprint import pprint
import paramiko

def sendShComm(ip, command, command2, shSleep=0.2, maxRead=10000, longSleep=2):
    USER = 'bsquared'
    PASS = 'bsquared2019!@#'
    report = "REP_%.2i%.2i%i" % (now.year, now.month, now.day)
    ff = open(report, 'a')
    try:
        cl = paramiko.SSHClient()
        cl.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        cl.connect(ip, username='bsquared', password=PASS, timeout=5)
    except socket.timeout:
        print(f'failed to connect to IP {ip}')
        return
    except paramiko.SSHException as error:
        print(f"error occurred {error} on ip {ip}")
        return
    except paramiko.ssh_exception.NoValidConnectionsError as error:
        print(f"error occurred {error} on ip {ip}")
        return

    with cl.invoke_shell() as ssh:
        ssh.send('ena\n')
        ssh.send(USER +'\n')
        ssh.send(PASS +'\n')
        time.sleep(shSleep)
    ###terminal lenght for no paging
        ssh.send('skip\n')
        time.sleep(shSleep)
    ###show config and write output
        #ssh.send('sh run\n')
        ssh.send(f'{command}\n')
        time.sleep(longSleep)
    ###Command2 and write output
        ssh.send(f'{command2}\n')
        time.sleep(longSleep)
        output = ssh.recv(maxRead).decode('utf-8').replace('\r\n', '\n')
        #prompt = re.search()
        ff.write(ip)
        ff.write(output)
    ###show output config and write file with prefix, date and time
        #print (output)
    ff.close()
    with open(report, 'r') as f_read:
        with open('result.txt', 'w') as f_write:
            f_write.write('---Next switch---\n')
            for str in f_read:
                if str.startswith('      Serial'):
                    f_write.write(str)
                elif str.startswith('1'):
                    f_write.write(str)
    return output

if __name__ == '__main__':

    ###set date and time
    now = datetime.datetime.now()
    sitePrefix = '''Al Khail		5		ECC-EO		9
Al_Dar			107		JAFZA-WEST	36
Al-Hamad DIC	65		JAFZA-WEST	49
Al-Hamad DIC	66		JAFZA-WEST	50
Al-Hamad DIC	67		JAFZA-WEST	51
Citadel1		1		JAFZA-WEST	63
Citadel2		2		JAFZA-WEST	64
DCE/CT			12		JAFZA-WEST	80
Dry_Docks		75		JAFZA-WEST	81
Dry_Docks		76		MGPI		21
Dry_Docks		77		RAK   		18
Dry_Docks		78		Sawaeed		29
ECC_SHJ2		37		Sharjah		19
ECC-AlQuoz		8		TECOM		26
ECC-CAMP22		47		 

Input site prefix: '''

    net = '172.18.'
    ipPref = input(sitePrefix)
    ipAdd = net + ipPref
    octet = 254
    ###start FOR ...in
    while octet > 200:
        octet -= 1
        ip = ipAdd + '.' + str(octet)
        #print(ip)
        out = sendShComm(ip, 'sh stack | i ICX', 'sh ver | i Serial')
        pprint(out, width=120)
        #print(out)

