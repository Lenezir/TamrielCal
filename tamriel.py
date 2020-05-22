"""
TamrielCal v0.2
Calendrier de correspondance entre le calendrier grégorien et le celui de Tamriel.
"""

# Import de bibliothèques
import datetime
import calendar

calendrier_tamriel = {
	1: {"mois": "Primétoile", "signe": "le Rituel", "saison": "hiver"},
	2: {"mois": "Clairciel", "signe": "l'Amant", "saison": "printemps"},
	3: {"mois": "Semailles", "signe": "le Seigneur", "saison": "printemps"},
	4: {"mois": "Ondepluie", "signe": "le Mage","saison": "printemps"},
	5: {"mois": "Plantaisons", "signe": "l'Ombre", "saison": "été"},
	6: {"mois": "Mi-l'an", "signe": "le Destrier", "saison": "été"},
	7: {"mois": "Hautzénith", "signe": "l'Apprenti", "saison": "été"},
	8: {"mois": "Vifazur", "signe": "le Guerrier", "saison": "automne"},
	9: {"mois": "Âtrefeu", "signe": "la Dame", "saison": "automne"},
	10: {"mois": "Soufflegivre", "signe": "la Tour", "saison": "automne"},
	11: {"mois": "Sombreciel", "signe": "l'Astronach", "saison": "hiver"},
	12: {"mois": "Soirétoile", "signe": "le Voleur", "saison": "hiver"}
}

jour_tamriel = ("Morndas", "Tirdas", "Middas", "Turdas", "Fredas", "Loredas", "Sundas")

# Récupération de la date du moment
date = datetime.datetime.now()
now = datetime.datetime.today()

# Boucle pour ajouter 'er' au premier jour du mois
if(date.day == 1):
	auj = "1er"
else:
	auj = date.day

# Boucle pour le choix de l'article
if(calendrier_tamriel[date.month]["saison"] == "printemps"):
	article = "au"
else:
	article = "en"

# Affichage de la date du jour
print("Nous sommes le ", jour_tamriel[now.weekday()], " ", auj, " ", calendrier_tamriel[date.month]["mois"], " ", date.year, ", nous sommes ", article, " ", calendrier_tamriel[date.month]["saison"], " et le signe astrologique du mois est ", calendrier_tamriel[date.month]["signe"], ".", sep='')

########################################################################################################################

# L'utilisateur entre sa date de naissance
entree = input("Entrez votre date de naissance (au format jj/mm/aaaa) : ")

# Découpage de la date entrée en jour/mois/année
dateob = entree.split('/')
annee = int(dateob[2])
mois = int(dateob[1])
jour = int(dateob[0])

# Boucle pour ajouter 'er' au premier jour du mois
if jour == 1:
	jour_nd = "1er"
else:
	jour_nd = jour

# Définition du jour de semaine d'une date donnée
c = calendar.Calendar()

# Boucle permettant de trouver le jour de la semaine 
for i in c.itermonthdays2(annee,mois):
	if(i[0] == jour):
		res = i[1]

# Article à mettre devant la saison (au à la place de en pour le printemps)
if calendrier_tamriel[mois]["saison"] == "printemps":
	article = "au"
else:
	article = "en"

print("Vous êtes né le ", jour_tamriel[res]," ", jour_nd," ", calendrier_tamriel[mois]["mois"]," ", annee," ", article," ", calendrier_tamriel[mois]["saison"], ". Votre signe est ", calendrier_tamriel[mois]["signe"], ".", sep='')