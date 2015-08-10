pache_cert_file: "{{ inventory_hostname }}.{{ domain }}.crt"
apache_key_file: "{{ inventory_hostname }}.{{ domain }}.key"
 
shibbolenth_file: {aaf: "{{ inventory_hostname }}.metadata.aaf.xml", cert: "{{ inventory_hostname }}.aaf-metadata-cert.pem" }

