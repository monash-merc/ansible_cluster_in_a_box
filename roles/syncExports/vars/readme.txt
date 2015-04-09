---
# This is a list of directorys to export and where to export them too
# interface referst to an interface name which must be present on all members
# of the group mounting the export (as opposed to the interface on the server
# which is irrelevant).
# group is a group of nodes (ansible group) authorised to mount the export
exportList:
  - { src: '/cinderVolume/home', srvopts: 'fsid=1,rw,no_root_squash,sync', 'opts': 'defaults,nofail', group: ['DesktopNodes', 'LoginNodes'], interface: 'eth0' }
