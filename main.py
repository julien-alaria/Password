import hashlib
# print(hashlib.algorithms_available)
import json


def job6_version2(pass_user):

    caracteres_speciaux = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"
   
    if len(pass_user) < 8:
        return "mot de passe incorrect, doit contenir au moins 8 caracteres"

    if not any(caractere.isupper() for caractere in pass_user):
        return "Mot de passe incorrect : doit contenir au moins une majuscule."

    if not any(caractere.islower() for caractere in pass_user):
        return "Mot de passe incorrect : doit contenir au moins une minuscule."
    
    if not any(caractere.isdigit() for caractere in pass_user):
        return "Mot de passe incorrect : doit contenir au moins un chiffre."
    
    if not any (caractere in caracteres_speciaux for caractere in pass_user):
        return "mot de passe incorrect, doit contenir un caractere special"
    
    else:
        return "Mot de passe valide"
    
while True:
    pass_user = input("Veuillez entrer votre mot de passe:  ")
    resultat = job6_version2(pass_user)

    if resultat == "Mot de passe valide":
        print("Mot de passe valide")
        break
    else:
        print(resultat)


# Hashage
hashdata = pass_user
hashed = hashlib.sha256(hashdata.encode()).hexdigest()
print(f"CODAGE SHA-256: {hashed}")

# ecriture dans le fichier json
def write_json(pass_user, hashed, filename='password.json'):

    new_data = {
        "mot de passe": pass_user,
        "hash SHA 256": hashed
    }
    with open(filename, 'r') as file:
        file_data = json.load(file)
        # verification que les nouvelles données ne soient pas présentes dans le fichier (collisions)
        for user_id, data in file_data.items():
            if data == new_data:  # Si les données sont identiques
                return "Les données sont déjà présentes, aucune écriture effectuée."
     # Trouver un nouvel identifiant unique (par exemple user_1, user_2, etc.)
    user_id = f"user_{len(file_data) + 1}"
    # Ajouter la nouvelle entrée avec une clé unique
    file_data[user_id] = new_data
      
    with open(filename, 'w') as file:
        json.dump(file_data, file, indent=4)
        print("Écriture réussie dans le fichier JSON.")
    
    # # lire le fichier json
    with open(filename, 'r') as file:
        file_data = json.load(file)
        print("Contenu du fichier JSON:")
        print(file_data)
    
print(write_json(pass_user, hashed))

