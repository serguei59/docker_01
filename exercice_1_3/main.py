import pandas as pd

nb_element = 0
element_liste = []
while nb_element != 4:
    element = input("que voulez vous ajouter a la liste de courses")
    element_liste.append(element)
    nb_element+=1

print("voici la liste de courses")
df = pd.DataFrame(element_liste, columns={"Numbers:"})
print(df)