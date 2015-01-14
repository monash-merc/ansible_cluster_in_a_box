---
nfsExportFile: "/etc/exports"
nfsClientIp: "{{ ansible_tun0.ipv4.address }}"
nfsServerOption: "ro,fsid=0,sync"
