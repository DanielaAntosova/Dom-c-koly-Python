# Zadání domácích úkolů Python


Úkol 1
Napiš skript v Pythonu, který otevře soubor alice.txt (Alice’s Adventures in Wonderland od Lewise Carrolla) - ke stažení v [1] a spočítá četnost (počet výskytů) všech znaků. Velká písmena převeď za malá a ignoruj mezery a znaky nového řádku (ostatní znaky jako čárky nebo závorky zařaď do výsledku).
Jako výstup musí program vytvořit soubor ukol1_output.json. Vzorový výstup najdeš v souboru ukol1_output_vzor.json. Dodrž prosím následující pravidla
soubor ukol1_output.json je ve formátu JSON,
obsahuje slovník, kde klíče jsou znaky a hodnoty jejich četnost,
volitelně: slovník je seřazen podle klíčů

Jako řešení úkolu odevzdej program pojmenovaný jako prijmeni_jmeno_1.py. Soubor uploaduj na Google drive (nebo jiné úložiště), vytvoř na něj odkaz viditelný pro všechny a tento odkaz odevzdej přes moje.czechitas.cz.
Příklad výsledku
Pokud by soubor alice.txt obsahoval jen větu: 
 	‘datova akademie se mi moc libila’

dostali bychom následující výstup:

{
    "a": 5,
    "b": 1,
    "c": 1,
    "d": 2,
    "e": 3,
    "i": 4,
    "k": 1,
    "l": 2,
    "m": 3,
    "o": 2,
    "s": 1,
    "t": 1,
    "v": 1
}
