#!/usr/bin/python
import sys
import json
filename = sys.argv[1]
domain = sys.argv[2]
f=open(filename,'r')
s=f.read()
d=json.loads(s)
f.close()
hosts={}

for group in d['groups'].keys():
    i=0
    for h in d['groups'][group]:
        hosts[h] = ['%s %s.%s'%(h, h, domain)]

for h in hosts.keys():
    if d['hostvars'].has_key(h):
        string="%s"%(d['hostvars'][h]['ansible_eth0']['ipv4']['address'])
        for name in hosts[h]:
            string=string+" %s"%(name)
        print string

for h in hosts.keys():
    if d['hostvars'].has_key(h):
        if d['hostvars'][h].has_key('ansible_tun0'):
            string="%s"%(d['hostvars'][h]['ansible_tun0']['ipv4']['address'])
            string=string+" %s-vpn"%h
            print string
