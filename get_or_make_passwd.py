#!/usr/bin/python
import random
import sys
import string
def get_passwd(f,passname):
    f.seek(0)
    for line in f.readlines():
        (key,passwd)=line.split(':')
        if key==passname:
            f.close()
            return passwd.rstrip()
    return None

def mk_passwd(f,passname):
    passwd=''.join(random.choice(string.ascii_uppercase + string.digits+string.ascii_lowercase) for _ in range(16))
    f.write("%s:%s\n"%(passname,passwd))
    return passwd
   
try:
    f=open('../passwd.txt','at+')
except:
    f=open('./passwd.txt','at+')
passname = sys.argv[1]
passwd = get_passwd(f,passname)
if passwd == None:
    passwd = mk_passwd(f,passname)
print passwd
f.close()
