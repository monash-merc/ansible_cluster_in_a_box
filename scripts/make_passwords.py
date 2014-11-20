# This program writes a yaml varaible file where each varible is suitable as a password
# If a variable is not defined it will pick a new random varaible for you
# If a variable is already defined it will not change
import random
import sys
import string
import yaml

def new_pass(length):
    return ''.join(random.choice(string.ascii_uppercase + string.digits+string.ascii_lowercase) for _ in range(length))

# required_passwords is a dictionay consisting of variable names and the length of random password you would like to associate with that variable
required_passwords={}
# Passwords for munge and slurm
required_passwords['mungekey']=32
# Passwords for karaage and ldap
required_passwords['ldapManagerPassword']=8
required_passwords['ldapBindDNPassword']=8
required_passwords['karaageSqlPassword']=8
required_passwords['sqlrootPasswd']=8

changed=False
pwpath='./passwords.yml'
try:
    f=open(pwpath,'r')
    data=yaml.load(f.read())
    f.close()
except Exception as e:
    pass
if data==None:
    data={}

print data

for pw in required_passwords.keys():
    if data.has_key(pw):
        pass
    else:
        data[pw]=new_pass(required_passwords[pw])
        changed=True
if changed:
    f=open(pwpath,'w+')
    f.write(yaml.dump(data,default_flow_style=False,explicit_start=True))
    f.close()

