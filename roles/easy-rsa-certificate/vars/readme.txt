---
x509_key_file: "/etc/ssl/private/server.key"
x509_cert_file: "/etc/ssl/certs/server.crt"
x509_cacert_file: "/etc/ssl/certs/ca.crt"
x509_csr_args: ""
x509_sign_args: "{{ x509_csr_args }}"
x509_common_name: "{{ ansible_fqdn }}"
