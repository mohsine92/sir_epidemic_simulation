# main.py
# Modèle SIR – Simulation de propagation d'une épidémie
# Auteur : Mohsine ESSAT
# Description : Modèle épidémiologique simple SIR codé en Python

import matplotlib.pyplot as plt 


# 1. Initialisation des paramètres du modèle


# Nombre total de personnes dans la population (Ville, Pays, ect)
N = 1000

# Cas initiaux :
I = [3]
S = [997]
R = [0]

# Paramètre du virus 
beta = 0.3 # Taux de transmition (à quel point c'est contagieux)
gamma = 0.1 # Taux de guérison ( à quel point on guérit vite)

# Nombre total de jours à simuler
jours = 100

# 2. Simulation jour par jour
for jour in range(jours):

    # On récupère les données du jour précédent (le dernier de chaque liste)
    s = S[-1]  # personnes en bonne santé hier
    i = I[-1]  # personnes infectées hier
    r = R[-1]  # personnes retirées (guéries) hier
    
# Calcul des nouvelles infections
    # Plus il y a de malades ET de gens sains → plus ça contamine
    nouvelles_infections = beta * s * i / N

# Calcul des nouvelles guérisons
    # Une partie des malades guérissent chaque jour
    nouvelles_guerisons = gamma * i

# Mise à jour des valeurs pour aujourd’hui (jour courant)
    s_next = s - nouvelles_infections
    i_next = i + nouvelles_infections - nouvelles_guerisons
    r_next = r + nouvelles_guerisons

    S.append(s_next)
    I.append(i_next)
    R.append(r_next)

# 3. Affichage des résultats sous forme de graphique
plt.plot(S, label='🟢 Sains')
plt.plot(I, label='🔴 Infectés')
plt.plot(R, label='🔵 Guéris')

# Titres et légendes
plt.xlabel('Jours')
plt.ylabel('Nombre de personnes')
plt.title("Modèle SIR - Simulation de propaganation d'un virus")
plt.legend()
plt.show()
