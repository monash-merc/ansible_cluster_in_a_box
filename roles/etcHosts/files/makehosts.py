#!/usr/bin/python
import sys
import json
import socket
filename = sys.argv[1]
try:
 domain = sys.argv[2]
except IndexError:
 domain = None
f=open(filename,'r')
s=f.read()
d=json.loads(s)
f.close()
hosts={}

for group in d['groups'].keys():
    i=0
    for h in d['groups'][group]:
      if not domain:
        hosts[h] = [h]
      else:
        hosts[h] = ['%s.%s %s'%(h,domain,h)]

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
