# ✅ Testovanie – Tester Adventure

Manuálne testy pre textovú Python hru z prostredia testovania. Testujú základnú logiku, výhry, prehratia a reakcie na chybné vstupy.

---

## 🧪 TC01 – Zobrazenie úvodnej obrazovky
- **Popis:** Overenie, že sa správne zobrazí uvítanie pri spustení hry.
- **Vstupné podmienky:** Hra spustená.
- **Kroky:** Spusti `tester_adventure.py`
- **Očakávaný výsledok:** Zobrazí sa „VITAJ V JASKYNI TESTERA“
- **Skutočný výsledok:** ✅ Zobrazilo sa
- **Stav:** ✅ PASS

---

## 🧪 TC02 – Správna odpoveď na hádanku
- **Popis:** Hráč odpovie správne a získa kľúč.
- **Kroky:**  
  1. Vyber „vpravo“  
  2. Zadaj správnu odpoveď na otázku
- **Očakávaný výsledok:** Do inventára sa pridá „kľúč“
- **Skutočný výsledok:** ✅ Kľúč bol pridaný
- **Stav:** ✅ PASS

---

## 🧪 TC03 – Nesprávna odpoveď na hádanku
- **Popis:** Hráč odpovie zle, príde o život, dostane novú otázku.
- **Kroky:**  
  1. Vyber „vpravo“  
  2. Zadaj nesprávnu odpoveď (napr. „neviem“)
- **Očakávaný výsledok:** Život -1, nová otázka
- **Skutočný výsledok:** ✅ Správne zníženie a nová otázka
- **Stav:** ✅ PASS

---

## 🧪 TC04 – Výhra po získaní kľúča
- **Kroky:**  
  1. Získaj kľúč  
  2. Vyber „dopredu“
- **Očakávaný výsledok:** Hra gratuluje a ukončí sa
- **Skutočný výsledok:** ✅ Funguje správne
- **Stav:** ✅ PASS

---

## 🧪 TC05 – Smrť v pasci
- **Kroky:**  
  1. Vyber „vľavo“ (pasca)  
  2. Opakuj, kým životy neklesnú na 0
- **Očakávaný výsledok:** Hráč zomrie
- **Skutočný výsledok:** ✅ Hra končí správne
- **Stav:** ✅ PASS

---

## 🧪 TC06 – Pokus o útek bez kľúča
- **Kroky:**  
  1. Vyber „dopredu“ bez toho, aby si šiel vpravo
- **Očakávaný výsledok:** Dvere sú zamknuté
- **Skutočný výsledok:** ✅ Funguje správne
- **Stav:** ✅ PASS

---

## 🧪 TC07 – Neplatný vstup
- **Kroky:**  
  1. Zadaj „hore“ alebo „123“ pri výbere smeru
- **Očakávaný výsledok:** „Nerozumiem. Skús: vľavo / vpravo / dopredu“
- **Skutočný výsledok:** ✅ Zobrazilo sa
- **Stav:** ✅ PASS

---

## ⚠️ TC08 – Simulovaný neúspešný test (vysvetlenie rizika)
- **Popis:** Pokus o návrat do už vyriešenej miestnosti
- **Kroky:**  
  1. Vyber „vpravo“ a vyrieš hádanku  
  2. Skús ísť znova „vpravo“
- **Očakávaný výsledok:** Hra oznámi, že si už v miestnosti bol
- **Skutočný výsledok:** ✅ Hráč bol správne presmerovaný
- **Stav:** ✅ PASS

> Tento test bol pôvodne označený ako potenciálne nefunkčný (FAIL), ale reálne v kóde všetko funguje korektne.  
> V teste teda len simulujeme prípad, ktorý by mohol vzniknúť pri odstránení `vypisane_miestnosti.add()`.

---

## ❌ TC09 – Zadanie číselnej odpovede na hádanku (nevalidný vstup)
- **Popis:** Hráč pri hádanke zadá číslo namiesto textovej odpovede
- **Kroky:**  
  1. Vyber možnosť „vpravo“  
  2. Zadaj odpoveď „123“ alebo „??“
- **Očakávaný výsledok:** Hra upozorní na neplatný vstup (napr. „Zadaj slovo“)
- **Skutočný výsledok:** 🔴 Hra odpoveď považuje za chybnú a odpočíta život bez varovania
- **Stav:** ❌ FAIL
- **Poznámka:**  
  Toto správanie je technicky v poriadku, ale v reálnej aplikácii by sa očakávala validácia vstupu (napr. `odp.isalpha()`).

---

## 🧾 Poznámka k validáciám:

- Vstup pri výbere smeru je ošetrený.
- Odpovede na hádanky nie sú validované – používateľ môže zadať čísla, znaky alebo prázdny vstup, a systém ich berie ako chybnú odpoveď.
- Hra je funkčná a spoľahlivá, no neimplementuje pokročilú kontrolu vstupu (čo je v rámci zadania v poriadku).

---
