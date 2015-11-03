#!/bin/sh
# A CRUDE Script to install Mellanox OFED drivers
# Philip.Chan@monash.edu
#
# TODO: check if MLNX_OFED is already installed!
# TODO: check kernel...

KERN=`uname -r`

if [ "$KERN" != "3.10.0-229.14.1.el7.x86_64" ]
then
  echo "Oops! Did you forget to reboot?"
  echo "Kernel version has to be 3.10.0-229.14.1.el7.x86_64"
  exit 1
fi

sudo yum install -y pciutils gcc-gfortran libxml2-python tcsh libnl lsof tcl tk perl
sudo yum install -y gtk2 atk cairo
tar xzvf MLNX_OFED_LINUX-3.1-1.0.3-rhel7.1-x86_64-ext.tgz
cd MLNX_OFED_LINUX-3.1-1.0.3-rhel7.1-x86_64-ext
sudo ./mlnxofedinstall -q
cd ..

tmpfile="/tmp/ifcfg.pc"
rm -f $tmpfile
./set_ifcfg.pl $tmpfile

if [ -f $tmpfile ]
then
  echo "Attempting to install ifcfg-ens6"
  if [ -f /etc/sysconfig/network-scripts/ifcfg-ens6 ]
  then
    echo "/etc/sysconfig/network-scripts/ifcfg-ens6 already exists!"
    grep IP /etc/sysconfig/network-scripts/ifcfg-ens6
    echo "bailing!"
  else
    sudo cp -ip $tmpfile /etc/sysconfig/network-scripts/ifcfg-ens6 
    sudo chown root:root /etc/sysconfig/network-scripts/ifcfg-ens6 
    cd /etc/sysconfig/network-scripts
    sudo ./ifup ens6
    ping -c 1 172.16.228.1
  fi
fi
exit 0
