---
slurm_use_vpn: True
slurmctlddebug: {level: 9, log: '/var/log/slurm/slurmctld.log'}
slurmddebug: {level: 9, log: '/var/log/slurm/slurmd.log'}
slurmschedlog: {level: 9, log: '/var/log/slurm/slurmsched.log'}
slurmdbdlog: {level: 9, log: '/var/log/slurm/slurmdbd.log'}
slurmfairshare: {def: false, val: 10000}
slurmdatadir: "/var/spool/slurm"
slurmselecttype: "select/linear"
slurmfastschedule: "1"
slurmschedulertype: "sched/backfill"

