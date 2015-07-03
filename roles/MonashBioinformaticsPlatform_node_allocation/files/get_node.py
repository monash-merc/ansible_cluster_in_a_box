#!/usr/bin/python
import subprocess
import sys

def getTime():
    print "How long do you think you need this computer for?"
    print "If you need the computer for 2 days and 12 hours please enter as 2-12 or 2-12:00:00"
    time=sys.stdin.readline().strip()
    try:
        (days,hours)=time.split('-')
    except:
        days=0
        hours=time
    try:
        (hours,minues) = time.split(':')
    except:
        pass
    return (days,hours)

def getNCPUs():
    print "How many CPUs would you like?"
    cpus=None
    while cpus==None:
        cpustr=sys.stdin.readline().strip()
        try:
            cpus=int(cpustr)
        except:
            print "Sorry I can't interpret %s as a number"%cpustr
            print "How many CPUs would you like?"

    return cpus

def getRAM():
    print "How much RAM would you like (press enter for the default)?"
    ramstr= sys.stdin.readline().strip()
    while ramstr!=None and ramstr!="":
            try:
                ram=int(ramstr)
                return ram
            except:
                print "Sorry I can't interpret %s as a number"%ramstr
                print "How much RAM would you like?"
                ramstr= sys.stdin.readline()
    return None

def subjob(time,cpus,ram):
    if ram==None:
        ram=cpus*2000
    import subprocess
    scriptpath='/home/chines'
    p=subprocess.Popen(['sbatch','--time=%s-%s'%(time[0],time[1]),'--nodes=1','--mincpu=%s'%cpus,'--mem=%s'%ram,'%s/mbpjob.sh'%scriptpath],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (stdout,stderr)=p.communicate()
    import re
    m=re.match('Submitted batch job (?P<jobid>[0-9]+)',stdout)
    if m:
        return m.groupdict()['jobid']

def isState(jobid,state='RUNNING'):
    import re
    p=subprocess.Popen(['scontrol','show','job','-d',jobid],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (stdout,stderr)=p.communicate()
    jobidre=re.compile('JobId=(?P<jobid>[0-9]+)\s')
    statere=re.compile('^\s+JobState=(?P<state>\S+)\s')
    currentjobid=None
    for l in stdout.splitlines():
        m=jobidre.match(l)
        if m:
            currentjobid=m.groupdict()['jobid']
        m=statere.match(l)
        if m:
            if m.groupdict()['state']==state:
                if jobid==currentjobid:
                    return True
            else:
                if jobid==currentjobid:
                    return False
    return False

def waitjob(jobid):
    import time
    while True:
        if isState(jobid,'RUNNING'):
            return
        else:
            print "job %s not running"%jobid
            time.sleep(1)

def listJobs():
    import re
    r=[]
    user = subprocess.check_output(['whoami'])
    jobs = subprocess.check_output(['squeue','-u',user,'-h','-o','"%i %L %j %c"'])
    jobre=re.compile("(?P<jobid>(?P<jobidNumber>[0-9]+)) (?P<time>\S+ (?P<jobname>\S+) (?P<cpus>[0-9]+))$"
    for l in jobs.splitlines():
        m=jobidre.search(l)
        if m:
            r.append(m.groupdict())
    return r

def getNode(jobid):
    import re
    stdout=subprocess.check_output(['scontrol','show','job','-d',jobid])
    for l in stdout.splitlines():
        m=re.search('^\s+Nodes=(?P<nodelist>\S+)\s',l)
        if m:
            nodes=m.groupdict()['nodelist'].split(',')
            return nodes[0]

def createJob(*args,**kwargs):
    time=getTime()
    #cpus=getNCPUs()
    cpus=1
    #ram=getRAM()
    ram=None
    subjob(time,cpus,ram)

def selectJob(jobidlist):
    if len(jobidlist)==1:
        return jobidlist[0]['jobid']
    else:
        print "Please select a job (or press enter to cancel)"
        i=1
        print "\tJob name\tNum CPUs\tRemaining Time"
        for j in jobidlist:
            print "%s\t%s\t%s\t%s"%(i,j['jobname'],j['numcpus'],j['time'])
        try:
            jobnum=int(sys.stdin.readline().strip())
            if (jobnum>0 and jobnum<=jobidlist):
                return jobidlist[jobnum-1]['jobid']
        except:
            pass
    return None


def connect(*args,**kwargs):
    jobidlist=listJobs()
    jobid=selectJob(jobidlist)
    if jobid!=None:
        waitjob(jobid)
        node=getNode(jobid)
        print node

def stop(*args,**kwargs):
    jobidlist=listJobs()
    jobid=selectJob(jobidlist)
    if jobid!=None:
        stopjob(jobid)



def main():
    import argparse
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers()

    start = subparser.add_parser('start', help='alloate a node to the user')
    start.set_defaults(func=createJob)

    connect = subparser.add_parser('connect')
    start.set_defaults(func=connect)

    stop = subparser.add_parser('stop')
    start.set_defaults(func=stop)
        
    args = parser.parse_args()
    args.func(args)

try:
    jobidlist=listJobs()
    if len(jobidlist)>1:
        print "cancel all jobs here"
    jobidlist=listJobs()
    if len(jobidlist)==0:
        time=getTime()
        #cpus=getNCPUs()
        cpus=1
        #ram=getRAM()
        ram=None
        subjob(time,cpus,ram)
    jobidlist=listJobs()
    if len(jobidlist)==1:
        jobid=jobidlist[0]
        waitjob(jobid)
        node=getNode(jobid)
        print node
        sys.exit(0)
except Exception as e:
    print e
    import traceback
    print traceback.format_exc()
    sys.exit(1)

main()
