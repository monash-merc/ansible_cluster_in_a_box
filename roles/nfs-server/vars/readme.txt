---
mkFileSystems:
  - {fstype : 'ext4', dev: '/dev/vdc', opts: '', name: '/mnt'}

mountFileSystems:
  - {name: '/mnt', fstype : 'ext4', dev: '/dev/vdc', opts: 'defaults,nofail'}
