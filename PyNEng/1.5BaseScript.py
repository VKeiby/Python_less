from sys import argv

interface = argv[1]
vlan = argv[2]

#interface = 'f0/21'
#vlan = 2

access_template = ['interface eth {}',
                    'protected-port',
                    'inline power power-by-class 3'
                    'stp-bpdu-guard'
                    'packet-inerror-detect 100'
                    'spanning-tree portfast',
print('\n'.join(access_template).format(interface,vlan))
input("Press any key...")