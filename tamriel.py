"""
TamrielCal v0.1
Calendrier de correspondance entre le calendrier grégorien et le celui de Tamriel.
"""

# Import de bibliothèques
import datetime
import calendar

# Jours, mois et signes astrologiques de Tamriel
moistam = ("Primétoile", "Clairciel", "Semailles", "Ondepluie", "Plantaisons", "Mi-l'An", "Hautzénith", "Vifazur", "Âtrefeu", "Soufflegivre", "Sombreciel", "Soirétoile")
jourtam = ("Morndas", "Tirdas", "Middas", "Turdas", "Fredas", "Loredas", "Sundas")
astrotam = ("le Rituel", "l'Amant", "le Seigneur", "le Mage", "l'Ombre", "le Destrier", "l'Apprenti", "le Guerrier", "la Dame", "la Tour", "l'Astronach", "le Voleur")
saisontam = ("hiver","printemps","printemps","printemps","été","été","été","automne","automne","automne","hiver","hiver")

# Récupération de la date du moment
date = datetime.datetime.now()
now = datetime.datetime.today()

# Affichage de la date du jour
print("Nous sommes le", jourtam[now.weekday()], date.day, moistam[date.month-1], date.year, "et nous somme en plein", saisontam[date.month-1], ".")

########################################################################################################################

# L'utilisateur entre sa date de naissance
entree = input("Entrez votre date de naissance (au format jj/mm/aaaa) : ")

# Découpage de la date entrée en jour/mois/année
dateob = entree.split('/')
annee = int(dateob[2])
mois = int(dateob[1])-1
jour = int(dateob[0])

# Définition du jour de semaine d'une date donnée
c = calendar.Calendar()

# Boucle permettant de trouver le jour de la semaine 
for i in c.itermonthdays2(annee,mois+1):
	if(i[0] == jour):
		res = i[1]

print("Vous êtes né le", jourtam[res], jour, moistam[mois], annee, "en plein",saisontam[mois-1],". Votre signe est", astrotam[mois] +".")