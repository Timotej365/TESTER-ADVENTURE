import time
import random

# 🧠 Testovacie hádanky (otázka + správna odpoveď)
hadanky = [
    {"otazka": "Aký typ testovania vykonáva používateľ? (funkcne, regresne, akceptacne)", "odpoved": "akceptacne"},
    {"otazka": "Ako nazývame dokument, kde zapisujeme chyby? (bug, report, testplan)", "odpoved": "report"},
    {"otazka": "Ako sa volá test, ktorý overuje opravenú chybu? (regresny, retest, unit)", "odpoved": "retest"},
    {"otazka": "Ktorý test kontroluje celé správanie systému? (unit, system, smoke)", "odpoved": "system"}
]

# Úvodná obrazovka
def uvod():
    print("\n🧪 VITAJ V JASKYNI TESTERA")
    print("Prebudil si sa uprostred temnej jaskyne.")
    print("Si junior tester na skúšobnej misii... a niečo sa pokazilo.")
    print("Tvoj cieľ: dostať sa von a prežiť.\n")
    time.sleep(2)

# Funkcia na náhodné vybranie hádanky
def hadanka_otazka():
    vybrana = random.choice(hadanky)
    print(f"❓ {vybrana['otazka']}")
    odp = input("> ").strip().lower()
    if odp == vybrana["odpoved"]:
        print("✅ Správne!")
        return True
    else:
        print("❌ Nesprávne. Strácaš 1 život.")
        return False

# Hlavná hra
def hra():
    zivoty = 3
    inventar = []
    vypisane_miestnosti = set()  # Pamätá si, kde hráč už bol

    def vypis_stav():
        print(f"\n❤️ Životy: {zivoty} | 🎒 Inventár: {inventar}")

    print("🔦 Rozhliadaš sa okolo seba...")

    # Hlavný herný cyklus – opakuje sa, kým hráč nezomrie alebo nevyhrá
    while True:
        vypis_stav()
        print("\nMáš tri možnosti: vľavo, vpravo, dopredu")
        vyber = input("Kam sa vydáš? ").lower()

        # ✅ VĽAVO – pasca (iba raz)
        if vyber in ["vľavo", "vlavo"] and "pasca" not in vypisane_miestnosti:
            print("💥 Vbehol si do miestnosti s pascou! Spadol kameň a zasiahol ťa.")
            zivoty -= 1
            vypisane_miestnosti.add("pasca")
            if zivoty == 0:
                print("☠️ Zomrel si. Hra končí.")
                break  # ← Ukončí hlavný cyklus = koniec hry

        # ✅ VPRAVO – hádanky z testovania
        elif vyber == "vpravo" and "hadanka" not in vypisane_miestnosti:
            print("📘 Našiel si starý terminál s testovacími otázkami.")
            # Cyklicky kladieme nové náhodné otázky, kým hráč neodpovie správne alebo nezomrie
            while True:
                spravne = hadanka_otazka()
                if spravne:
                    if "kľúč" not in inventar:
                        print("🔑 Z terminálu vypadol kľúč.")
                        inventar.append("kľúč")
                    break  # ← Ukončí len cyklus hádaniek, nie celú hru
                else:
                    zivoty -= 1
                    if zivoty == 0:
                        print("☠️ Zomrel si pri riešení hádaniek.")
                        return  # ← Ukončí CELÚ funkciu `hra()`
            vypisane_miestnosti.add("hadanka")

        # ✅ DOPREDU – východ (potrebuješ kľúč)
        elif vyber == "dopredu":
            print("🚪 Prišiel si k veľkým železným dverám.")
            if "kľúč" in inventar:
                print("🔓 Použil si kľúč a otvoril dvere.")
                print("🎉 GRATULUJEM! Unikol si z jaskyne testera.")
                break  # ← Hráč vyhral → koniec hry
            else:
                print("🔒 Dvere sú zamknuté. Potrebuješ kľúč.")

        # Hráč sa snaží ísť znova do tej istej miestnosti
        elif vyber in vypisane_miestnosti:
            print("🔁 V tejto miestnosti si už bol. Skús inú cestu.")

        # Neplatný vstup
        else:
            print("❓ Nerozumiem. Skús: vľavo / vpravo / dopredu")

    # ✅ Po výhre alebo prehre – možnosť hrať znova (iba y/n)
    while True:
        znova = input("\nChceš hrať znova? (y/n): ").lower()
        if znova == "y":
            hra()
            break
        elif znova == "n":
            print("👋 Vďaka za hru! Testuj ďalej.")
            exit()
        else:
            print("Zadaj iba 'y' pre áno alebo 'n' pre nie.")

# Spustenie hry
uvod()
hra()

