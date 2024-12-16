import json

vystup = {}

with open("alice.txt", encoding="utf-8") as soubor:
    obsah = soubor.read()
    obsah = obsah.lower()
    obsah = obsah.replace(" ", "")
    obsah = obsah.replace("\n", "")

    for znak in obsah:
        if znak in vystup:
            vystup[znak] += 1
        else:
            vystup[znak] = 1
# pokud tam ten znak je, tak zvýší jeho počet, pokud ne, tak je tam poprvý, tak se do slovníku dá jednička
with open("ukol1_output.json", "w", encoding="utf-8") as file:
    json.dump(vystup, file, ensure_ascii=False, indent=4, sort_keys=True)
