"""
TamrielCal v0.1
Calendrier de correspondance entre le calendrier grégorien et le calendrier de Tamriel.
"""

import datetime

mois = ("Primétoile", "Clairciel", "Semailles", "Ondepluie", "Plantaisons", "Mi-l'An", "Hautzénith", "Vifazur", "Âtrefeu", "Soufflegivre", "Sombreciel", "Soirétoile")
jours = ("Morndas", "Tirdas", "Middas", "Turdas", "Fredas", "Loredas", "Sundas")
astro = ("Le Rituel", "L'Amant", "Le Seigneur", "Le Mage", "L'Ombre", "Le Destrier", "L'Apprenti", "Le Guerrier", "La Dame", "La Tour", "L'Astronach", "Le Voleur")

date = datetime.datetime.now()
now = datetime.datetime.today()


print("Nous sommes le",jours[now.weekday()], date.day, mois[date.month-1], date.year)
print("Vous êtes né le", "xxx", mois[], "xxx. Votre signe est", astro[],".")
