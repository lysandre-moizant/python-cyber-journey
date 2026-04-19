# Script interactif d'analyse réseau
nom_machine = input("Nom de la machine : ")
ip = input("Adresse IP : ")
port = int(input("Port SSH : "))

print(f"\n--- Rapport ---")
print(f"Machine : {nom_machine}")
print(f"IP : {ip}")
print(f"Longueur IP : {len(ip)} caractères")
print(f"Contient '192' : {'192' in ip}")
print(f"Port SSH : {port}")

port_backup = port + 1
print(f"Port backup : {port_backup}")