"""
TamrielCal v0.1
Calendrier de correspondance entre le calendrier grégorien et le calendrier de Tamriel.
"""

import datetime

mois = ("Primétoile", "Clairciel", "Semailles", "Ondepluie", "Plantaisons", "Mi-l'An", "Hautzénith", "Vifazur", "Âtrefeu", "Soufflegivre", "Sombreciel", "Soirétoile")
jours = ("Morndas", "Tirdas", "Middas", "Turdas", "Fredas", "Loredas", "Sundas")
astro = ("le Rituel", "l'Amant", "le Seigneur", "le Mage", "l'Ombre", "le Destrier", "l'Apprenti", "le Guerrier", "la Dame", "la Tour", "l'Astronach", "le Voleur")

date = datetime.datetime.now()
now = datetime.datetime.today()

print("Nous sommes le",jours[now.weekday()], date.day, mois[date.month-1], date.year)

dob = int(input("Entrez votre jour de naissance : "))
mob = int(input("Entrez le chiffre correspondant au mois de naissance (ex. 6 pour juin) : "))
yob = int(input("Entrez votre année de naissance : "))

print("Vous êtes né le", dob, mois[mob-1], yob,". Votre signe est", astro[mob-1],".")
