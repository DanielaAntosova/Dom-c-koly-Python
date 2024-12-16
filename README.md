# Zadání domácích úkolů Python


# Úkol 1

## Zadání
Napiš skript v Pythonu, který otevře soubor `alice.txt` (*Alice’s Adventures in Wonderland* od Lewise Carrolla) - ke stažení v [1] a spočítá četnost (počet výskytů) všech znaků. 

- **Pravidla**:
  - Velká písmena převeď na malá.
  - Ignoruj mezery a znaky nového řádku.
  - Ostatní znaky (např. čárky nebo závorky) zařaď do výsledku.

Jako výstup musí program vytvořit soubor `ukol1_output.json`. Výstupní soubor musí:

1. Být ve formátu JSON.
2. Obsahovat slovník, kde klíče jsou znaky a hodnoty jejich četnost.
3. **Volitelné**: Slovník má být seřazen podle klíčů.

Zde odkaz na výsledný script: 

- **Příklad výsledku**:
  Pokud by soubor `alice.txt` obsahoval větu: Datová akademie se mi moc líbila. 

Výstup by byl následující:

```json
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
