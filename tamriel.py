"""
TamrielCal v0.1
Calendrier de correspondance entre le calendrier grégorien et le celui de Tamriel.
"""

# Import de bibliothèques
import datetime
import calendar

# Jours, mois et signes astrologiques de Tamriel
moistam = (("Primétoile",3), ("Clairciel",0), ("Semailles",0), ("Ondepluie",0), ("Plantaisons",1), ("Mi-l'An",1), ("Hautzénith",1), ("Vifazur",2), ("Âtrefeu",2), ("Soufflegivre",2), ("Sombreciel",3), ("Soirétoile",3))
jourtam = ("Morndas", "Tirdas", "Middas", "Turdas", "Fredas", "Loredas", "Sundas")
astrotam = ("le Rituel", "l'Amant", "le Seigneur", "le Mage", "l'Ombre", "le Destrier", "l'Apprenti", "le Guerrier", "la Dame", "la Tour", "l'Astronach", "le Voleur")
saisontam = ("printemps", "été", "automne", "hiver")

# Récupération de la date du moment
date = datetime.datetime.now()
now = datetime.datetime.today()
moisactuel = moistam[date.month-1]
saison = moisactuel[1]
# Affichage de la date du jour
print("Nous sommes le", jourtam[now.weekday()], date.day, moisactuel[0], date.year, "et nous sommes en plein", saisontam[saison], ".")

########################################################################################################################

# L'utilisateur entre sa date de naissance
entree = input("Entrez votre date de naissance (au format jj/mm/aaaa) : ")

# Découpage de la date entrée en jour/mois/année
dateob = entree.split('/')
annee = int(dateob[2])
mois = int(dateob[1])-1
jour = int(dateob[0])

moistamactuel = moistam[mois]

# Définition du jour de semaine d'une date donnée
c = calendar.Calendar()

# Boucle permettant de trouver le jour de la semaine 
for i in c.itermonthdays2(annee,mois+1):
	if(i[0] == jour):
		res = i[1]

print("Vous êtes né le", jourtam[res], jour, moistamactuel[0], annee, "en plein",saisontam[mois-1],". Votre signe est", astrotam[mois] +".")