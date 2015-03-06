---
slurm_use_vpn: True
clustername: "CIAB"
slurmqueues:
  - {name: batch, group: default_partition, default: yes}
  - {name: 64cpu, group: 64cpu_partition, default: no}
  - {name: vis, group: VisNodes, default: no}
slurmlogin: "{{ groups['LoginNodes'][0] }}"
slurmctlddebug: {level: 9, log: '/var/log/slurm/slurmctld.log'}
slurmddebug: {level: 9, log: '/var/log/slurm/slurmd.log'}
slurmschedlog: {level: 9, log: '/var/log/slurm/slurmsched.log'}
slurmdbdlog: {level: 9, log: '/var/log/slurm/slurmdbd.log'}
slurmfairshare: {def: false, val: 10000}
slurmdatadir: "/var/spool/slurm"
slurm_version: 14.11.1
munge_version: 0.5.11
slurmctrl: "{{ groups['ManagementNodes'][0] }}"
slurmselecttype: "select/linear"
slurmfastschedule: "1"
slurmschedulertype: "sched/backfill"

