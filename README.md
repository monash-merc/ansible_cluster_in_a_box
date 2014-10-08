ansible_cluster_in_a_box
========================

The aim of this repo is to provide a set or ansible roles that can be used to deploy a cluster
We are working from 
https://docs.google.com/a/monash.edu/spreadsheets/d/1IZNE7vMid_SHYxImGVtQcNUiUIrs_Nu1xqolyblr0AE/edit#gid=0
as our architecture document.

We aim to make these roles as generic as possible. You should be able to start from an inventory file, an ssh key and a git clone of this and end up with a working cluster. In the longer term we might branch to include utilities to make an inventory file using NeCTAR credentials.

If you need a password use get_or_make_password.py (delegated to the passwword server/localhost) to generate a random one that can be shared between nodes

We aim to make these roles run on all common linux platforms (both RedHat and Debian derived) but at the very least they should work on a CentOS 6 install.
