---
# This is a list of mounts to make
nfsMounts:
 - { mntpt: '/home' src:"{{ hostvars[groups['ManagementNodes'][0]]['ansible_eth0']['ipv4']['address'] }}:/cinderVolume/home", opts: "defaults", fstype: "nfs4" }
# This is a list of exports, individual entry for each mount.
exportList:
 - { name : '/mnt/test-nfs', src : '/mnt',fstype : 'nfs', opts : 'vers=3,noatime,rsize=16384,wsize=16384,hard,intr,tcp,nolock' , interface : 'tun0', srvopts: 'rw,sync,root_squash' }
 - { name : '/mnt/test-volume', src : '/mnt/vdc',fstype : 'nfs', opts : 'vers=3,noatime,rsize=16384,wsize=16384,hard,intr,tcp,nolock' , interface : 'tun0', srvopts: 'rw,sync,root_squash' }
