# Calculs sur les nombres
port_base = 8000
port_dev = port_base + 80
port_admin = port_base + 443

print(f"Port de base : {port_base}")
print(f"Port dev : {port_dev}")
print(f"Port admin : {port_admin}")

# Manipulation de texte (str)
ip = "192.168.1.1"
print(f"Longueur de l'IP : {len(ip)} caractères")
print(f"IP en majuscules : {ip.upper()}")
print(f"L'IP contient un point : {'.' in ip}")

# Concaténation
hostname = "srv"
domaine = ".local"
fqdn = hostname + domaine
print(f"FQDN complet : {fqdn}")