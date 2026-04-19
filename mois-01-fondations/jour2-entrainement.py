#Partie 1 : ENTRAINEMENT ET MANIPULATION 

nom_machine = "SHADOW-1"
ip = "192.168.55.10"
port_ssh = 22
port_ssh_backup = port_ssh + 1 # port 2222 souvent utilisé pour éviter les conflits ou les scans automatiques

print(f"PORT SSH : {port_ssh}")
print(f"PORT SSH BACKUP : {port_ssh_backup}")

#Vérification et analyse 

print(f"Longueur de l'IP : {len(ip)} caractères")
print(f"Contient 192 : {'192' in ip}")

#Concaténation 
hostname = "reseau"
source = ".local"
fqdn = hostname + source 
print(f"FQDN complet : {fqdn}")



