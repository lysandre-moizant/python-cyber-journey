# Informations d'une machine cible
nom_machine = "routeur-principal"
ip = "192.168.1.254"
port_http = 8080
port_https = 8443
actif = False
version_os = 3.1

print(f"Machine : {nom_machine}")
print(f"IP : {ip}")
print(f"Ports ouverts : {port_http} et {port_https}")
print(f"En ligne : {actif}")
print(f"Version : {version_os}")