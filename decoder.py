from cryptography.fernet import Fernet

def decrypt_file_with_splited3_key(file_name, key1, key2, key3):
    """
    Déchiffre 'file_name' en utilisant la clé constituée de key1 + key2 + key3.
    Crée un fichier '_decrypted.txt' dans le même dossier.
    """
    # Assemble la clé finale
    key = key1 + key2 + key3

    # Crée l'objet Fernet pour le déchiffrement
    fernet = Fernet(key)

    # Lit les données chiffrées
    with open(file_name, "rb") as file:
        encrypted_data = file.read()

    # Déchiffre les données
    decrypted_data = fernet.decrypt(encrypted_data)

    # Écrit le fichier déchiffré
    decrypted_file_name = file_name[:-4] + "_decrypted.txt"
    with open(decrypted_file_name, "wb") as file:
        file.write(decrypted_data)

    print(f"Fichier déchiffré : {decrypted_file_name}")

def main():
   
    # 1) Demande à l'utilisateur le nom du fichier et les 3 parties de la clé
    file_name = input("Entrez le nom du fichier à déchiffrer (laisser vide si le nom est winners_encrypted.txt): ")or "winners_encrypted.txt"
    key1 = input("Entrez la première partie de la clé (key1) : ")
    key2 = input("Entrez la deuxième partie de la clé (key2) : ")
    key3 = input("Entrez la troisième partie de la clé (key3) : ")

    # 2) Déchiffre le fichier avec la clé assemblée
    try:
        decrypt_file_with_splited3_key(file_name, key1, key2, key3)
        # 3) Affiche le contenu du fichier déchiffré
        decrypted_file_name = file_name[:-4] + "_decrypted.txt"
        with open(decrypted_file_name, "r") as file:
            print(file.read())
    except Exception as e:
        print(f"Une erreur est survenue lors du déchiffrement : {e}")

if __name__ == "__main__":
    main()