---
x509_csr_args: ""
x509_cacert_file: "/etc/ssl/certs/cacert.crt"
x509_key_file: "/etc/ssl/private/client.key"
x509_cert_file: "/etc/ssl/certs/client.crt"
x509_common_name: "{{ ansible_fqdn }}_OpenVPN_Client"
