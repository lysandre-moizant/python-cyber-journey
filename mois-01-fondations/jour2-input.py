# Script interactif d'analyse réseau
nom_machine = input("Nom de la machine : ")
ip = input("Adresse IP : ")
port = int(input("Port SSH : "))

#Ce que je dois retenir --> input() renvoie toujours du texte
#Donc port vaut "22" (texte) et je veux faire ( texte+ nombre) cela ne fonctionne pas comme cela python ne peut pas le faire 
# la solution : int() --> port = int(input("Port SSH : "))
#En effet int() transforme "22" en 22 --> du texte en nombre entier ! 
#Résultat attendu 22+1 = 23 car port est maintenant un vrai nombre 

print(f"\n--- Rapport ---")
print(f"Machine : {nom_machine}")
print(f"IP : {ip}")
print(f"Longueur IP : {len(ip)} caractères")
print(f"Contient '192' : {'192' in ip}")
print(f"Port SSH : {port}")

port_backup = port + 1
print(f"Port backup : {port_backup}")