# 📚 Zadání domácích úkolů Python

## 📝 Úkol 1

### 🔍 Zadání
Napiš skript v Pythonu, který otevře soubor `alice.txt` a spočítá četnost (počet výskytů) všech znaků.

#### 📜 Pravidla:
- 🔠 **Velká písmena** převeď na **malá**.  
- 🚫 Ignoruj **mezery** a **znaky nového řádku**.  
- 🔣 Ostatní znaky (např. čárky nebo závorky) **zařaď do výsledku**.  

### 📥 Výstup
Jako výstup musí program vytvořit soubor `ukol1_output.json`. Výstupní soubor musí:

1. 📄 Být ve formátu **JSON**.  
2. 📊 Obsahovat **slovník**, kde klíče jsou znaky a hodnoty jejich četnost.  
3. 🔄 **Volitelné**: Slovník má být **seřazen podle klíčů**.  

🔗 **Zde odkaz na výsledný skript**: [antosova_daniela_1.py](https://github.com/DanielaAntosova/Domaci-ukoly-Python/blob/main/antosova_daniela_1.py)

---

### 📊 Příklad výsledku:
Pokud by soubor `alice.txt` obsahoval větu:  
> *Datová akademie se mi moc líbila.*  

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
```

## 🎬 Úkol 2

### 🔍 Zadání
V tomto úkolu budeš pracovat se souborem `netflix_titles.tsv`. Jedná se o textový soubor ve formátu **TSV** (Tabulator Separated Values), kde jsou jako oddělovače sloupců použity **tabulátory** (`\t`).  

Tvým úkolem bude:

1. 📥 **Načíst soubor**.  
2. 🗂️ **Vytáhnout z něj některé údaje**.  
3. 💾 **Uložit data ve formátu JSON**.  

---

### ✅ **Požadavky**:
Z každého řádku nás budou zajímat tyto údaje:

- 🎬 **PRIMARYTITLE** (název),  
- 🎥 **DIRECTOR** (režisér/režiséři),  
- 👥 **CAST** (herci),  
- 🎭 **GENRES** (seznam žánrů),  
- 🗓️ **STARTYEAR** (rok vydání).  

---

### 📋 Formát dat:
Údaje o filmech převeď do seznamu, kde bude každý film reprezentován jako **slovník** obsahující následující položky:

- 🎬 `title`: název filmu,  
- 🎥 `directors`: seznam všech režisérů nebo prázdný seznam, pokud není režisér uveden,  
- 👥 `cast`: seznam všech herců nebo prázdný seznam, pokud není žádný herec uveden,  
- 🎭 `genres`: seznam všech žánrů, do kterých byl film zařazen,  
- 📅 `decade`: dekáda, ve které film vznikl.  

---

### 🔗 **Herci a režiséři**:
V souboru jsou uvedeni jako jeden řetězec, jednotlivé hodnoty jsou oddělené **čárkami** (např. `Morgan Freeman, Monica Potter, Michael Wincott`).  

Ve formátu JSON použij **seznam**, aby bylo jasné, kolik herců nebo režisérů v seznamu je. Například:

```json
["Morgan Freeman", "Monica Potter", "Michael Wincott"]
```


🔗 **Zde odkaz na výsledný skript**: [antosova_daniela_2.py](https://github.com/DanielaAntosova/Domaci-ukoly-Python/blob/main/antosova_daniela_2.py)

