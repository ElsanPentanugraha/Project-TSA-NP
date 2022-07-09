from netmiko import ConnectHandler

router = {
    'device_type':'cisco_ios',
    'ip':'10.10.20.48',
    'username':'developer',
    'password':'C1sco12345',
    'secret':'enablepass',
    'port':22
}

conn = ConnectHandler(**router)

#privilege exec mode
print(conn.enable())

#global config mode
cmd = [
        'interface GigabitEthernet2',
        'description Configure IP Address using python',
        'ip address 192.168.2.1 255.255.255.0',
        'no shutdown',
	'exit'
]
print(conn.send_config_set(cmd))

#user exec mode
print(conn.send_command('sh ip int b'))
