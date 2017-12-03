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

# Boucle pour ajouter 'er' au premier jour du mois
if(date.day == 1):
	auj = "1er"
else:
	auj = date.day

# Boucle pour le choix de l'article
if(saisontam[moistam[date.month-1][1]] == "printemps"):
	article = "au"
else:
	article = "en"

# Affichage de la date du jour
print("Nous sommes le ", jourtam[now.weekday()]," ", auj," ", moistam[date.month-1][0]," ", date.year, ", nous sommes ", article," ", saisontam[moistam[date.month-1][1]], " et le signe astrologique du mois est ", astrotam[date.month-1], ".", sep='')

########################################################################################################################

# L'utilisateur entre sa date de naissance
entree = input("Entrez votre date de naissance (au format jj/mm/aaaa) : ")

# Découpage de la date entrée en jour/mois/année
dateob = entree.split('/')
annee = int(dateob[2])
mois = int(dateob[1])-1
jour = int(dateob[0])

# Boucle pour ajouter 'er' au premier jour du mois
if(jour == 1):
	jour_nd = "1er"
else:
	jour_nd = jour

# Définition du jour de semaine d'une date donnée
c = calendar.Calendar()

# Boucle permettant de trouver le jour de la semaine 
for i in c.itermonthdays2(annee,mois+1):
	if(i[0] == jour):
		res = i[1]

# Article à mettre devant la saison (au à la place de en pour le printemps)
if(saisontam[moistam[mois][1]] == "printemps"):
	article = "au"
else:
	article = "en"

print("Vous êtes né le ", jourtam[res]," ", jour_nd," ", moistam[mois][0]," ", annee," ", article," ", saisontam[moistam[mois][1]], ". Votre signe est ", astrotam[mois], ".", sep='')