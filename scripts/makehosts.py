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
        if hosts.has_key(h):
            hosts[h].append('%s-%s.%s'%(group,i,domain))
            hosts[h].append('%s-%s'%(group,i))
            pass
        else:
            hosts[h] = ['%s.%s'%(h,domain),'%s-%s.%s'%(group,i,domain),'%s'%h,'%s-%s'%(group,i)]
        i=i+1


for h in hosts.keys():
    string="%s"%(d['hostvars'][h]['ansible_eth0']['ipv4']['address'])
    for name in hosts[h]:
        string=string+" %s"%name
    print string
