import os
import sys
from PIL import Image

def redimensionner_images(dossier_racine, dimension):
    for racine, dirs, fichiers in os.walk(dossier_racine):
        for fichier in fichiers:
            if fichier.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                chemin_fichier = os.path.join(racine, fichier)
                try:
                    with Image.open(chemin_fichier) as img:
                        largeur, hauteur = img.size
                        if max(largeur, hauteur) > dimension:
                            img = img.resize((dimension, dimension), Image.LANCZOS)
                            img.save(chemin_fichier)
                            print(f"Image redimensionnée: {chemin_fichier}")
                        else:
                            print(f"Image non redimensionnée (trop petite): {chemin_fichier}")
                except Exception as e:
                    print(f"Erreur lors du redimensionnement de {chemin_fichier}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python redimensionner_images.py <dossier_racine> <dimension>")
        sys.exit(1)

    dossier_racine = sys.argv[1]
    dimension = int(sys.argv[2])

    redimensionner_images(dossier_racine, dimension)
    
