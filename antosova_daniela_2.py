import json

# nejprve připrav seznamy, zatím jsou prázdné

vsechny_filmy = []
list_slovniku = []

# otevři soubor

with open("netflix_titles.tsv", encoding="utf-8") as file:
    for line in file:
        # odstraň prázdné znaky na začátku a na konci řádku a rozděl řádek podle tabulátorů
        line_split = line.strip().split("\t")
        # přidej zpracovaný řádek do seznamu
        vsechny_filmy.append(line_split)


# připrav funkci, která mi udělá dekádu, oseká mi poslední znak z roku a přidá nulu
# výsledek musí být číslo!
def udelat_dekadu(rok):
    return int(rok[:3] + "0")


# projeď všechny filmy v seznamu, ale nechci záhlaví - nechci první řádek
for film in vsechny_filmy[1:]:
    # pokud ve sloupci DIRECTOR nic není, tak prázdný seznam v seznamu reziseru,
    # pokud obsahuje jmena, tak je rozděl podle čárky a dá do seznamu reziseru
    if film[15] == "":
        seznam_reziseru = []
    else:
        seznam_reziseru = film[15].split(", ")

    # cast = herci
    # pokud ve sloupci CAST nic není, tak prázdný seznam v seznamu castu,
    # pokud obsahuje jmena, tak je rozděl podle čárky a dej do seznamu castu
    if film[16] == "":
        seznam_castu = []
    else:
        seznam_castu = film[16].split(", ")

    # vezmi text, kde jsou žánry oddělený čárkama, rozděl je na jednotlivý žánry,
    # odstran z nich mezery na začátku a na konci, a pak je všechny hod do seznam_zanru
    # seznam_zanru = film[8].split(", ")
    seznam_zanru = []
    for zanr in film[8].split(","):
        seznam_zanru.append(zanr.strip())

    # použij funkci dekáda na STARTYEAR

    if film[5] != "":
        dekada = udelat_dekadu(film[5])

    # Soustruh
    # print("=====")
    # print(film[2])
    # print(seznam_reziseru)

    # vytvoř slovník pro každý film - detaily dle proměnných
    finalni_slovnik = {
        "title": film[2],
        "directors": seznam_reziseru,  # Režisér
        "cast": seznam_castu,  # Herci
        "genres": seznam_zanru,  # Žánry
        "decade": dekada,  # Rok vydání
    }
    # přidej slovníky do seznamu list slovníků
    list_slovniku.append(finalni_slovnik)

    print(list_slovniku)

# zde ulož
with open("movies.json", "w", encoding="utf-8") as json_file:
    json.dump(list_slovniku, json_file, ensure_ascii=False, indent=4)
