#!/usr/bin/python
import sys
import json
filename = sys.argv[1]
ansible_hostname = sys.argv[2]
domain = sys.argv[3]
f=open(filename,'r')
s=f.read()
d=json.loads(s)
f.close()
hosts={}
for group in d['groups'].keys():
    for h in d['groups'][group]:
        if hosts.has_key(h):
            pass
        else:
            hosts[h] = {}


url=""
try:
    for host in d['groups']['ldap']:
        fqdn="%s.%s"%(host,domain)
        url=url+"ldaps://%s"%fqdn
except:
    url="ldaps:///"
print url
	
