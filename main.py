# Note : les équations sont prises dans tous les fichiers .tex du répertoire dès que "\begin{equation}\label{...}" est détecté (les sous-fichiers ne sont a priori pas parcourus)(attention s'il y a des fichiers tex à ne pas prendre en compte)
# Les citations sont prises dans le premier .bib trouvé
# Si on veut donner explicitement les fichiers à explorer pour récupérer les équations et les citation, on peut décommenter les lignes 

import re
import os
import glob
from pybtex.database.input import bibtex # pip install pybtex (si nécessaire...)

# Cherche les fichiers .tex et .bib dans le répertoire courant
tex_files = glob.glob('*.tex')
bib_files = glob.glob('*.bib')

# Vérifie s'il y a au moins un fichier .tex et .bib
if not tex_files or not bib_files:
    print("Aucun fichier .tex ou .bib trouvé.")
    exit()

bib_file = bib_files[0]

# print(tex_file)
# print(bib_file)

# Exploration non-automatique des fichiers :
# tex_files = ["main.tex"]
# bib_file = "biblio.bib"

################################################################################
# ÉQUATIONS
################################################################################
# Supprime le fichier 'equations.txt' s'il existe déjà
if os.path.exists('equations.txt'):
    os.remove('equations.txt')

label_names = []  # Liste pour stocker les noms des labels

# Sauvegarde chaque équation dans 'equations.txt'
with open('equations.txt', 'w') as f:
    # Ouvre ton/tes fichier(s) LaTeX
    for tex_file in tex_files:
        with open(tex_file, 'r') as ff:
            contenu = ff.read()

        # Recherche toutes les équations avec leurs labels
        equations = re.findall(r'\\begin{equation}\\label{(.*?)}(.*?)\\end{equation}', contenu, re.DOTALL)

        for label, eq in equations:
            label_names.append(label)  # Ajoute le nom du label à la liste
            f.write(f'%<*{label}>\n')
            f.write(eq.strip() + '\n')
            f.write(f'%</{label}>\n\n')

# Imprime tous les noms des labels
print("Noms des labels compilés :\n")
for name in label_names:
    print(name)

# Imprime le nombre de labels
print(f"\nNombre de labels : {len(label_names)}\n")

print(">>> Le fichier 'equations.txt' a été créé.\n")

################################################################################
# CITATIONS BIB
################################################################################
def format_author(person):
    first_name = person.first_names[0][0] if person.first_names else ''
    last_name = person.last_names[0] if person.last_names else ''
    return f"{first_name}. {last_name}"

# Supprime le fichier 'citations.txt' s'il existe déjà
if os.path.exists('citations.txt'):
    os.remove('citations.txt')

# Pour stocker les noms des citations
citation_names = []

# Sauvegarde chaque clé bibtex dans 'citations.txt'
with open('citations.txt', 'w', encoding='utf-8') as f:
    # Charge le fichier BibTeX
    parser = bibtex.Parser()
    bib_data = parser.parse_file(bib_file)
    # Parcours chaque entrée BibTeX
    for key in bib_data.entries:
        citation_names.append(key)  # Ajoute le nom de la citation à la liste
        entry = bib_data.entries[key]
        # Récupère les auteurs et l'année
        authors = ' and '.join([format_author(person) for person in entry.persons['author']])
        year = entry.fields.get('year', 'N/A')

        # Écrit les données dans 'citations.txt'
        f.write(f'%<*{key}>\n')
        f.write(f'{authors} ({year})\n')
        f.write(f'%</{key}>\n\n')

# Imprime tous les noms des citations
print("Noms des citations compilées :\n")
for name in citation_names:
    print(name)

# Imprime le nombre de citations
print(f"\nNombre de citations : {len(citation_names)}\n")

print(">>> Le fichier 'citations.txt' a été créé.")

