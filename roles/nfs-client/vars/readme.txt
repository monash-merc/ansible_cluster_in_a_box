---
# This is a list of mounts to make
nfsMounts:
 - { mntpt: '/home' src:"{{ hostvars[groups['ManagementNodes'][0]]['ansible_eth0']['ipv4']['address'] }}:/cinderVolume/home", opts: "defaults", fstype: "nfs4" }

