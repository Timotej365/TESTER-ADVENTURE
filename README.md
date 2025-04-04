# 🧪 TESTER-ADVENTURE

Interaktívna textová hra napísaná v Pythone, v ktorej sa hráč ocitá v jaskyni plnej testerských hádaniek, pascí a rozhodnutí. Projekt vznikol ako tréning základov Pythonu a manuálneho testovania.

---

## 🎮 O hre

- Hráč má 3 životy a pohybuje sa v jaskyni výberom smerov: `vľavo`, `vpravo`, `dopredu`.
- V každej miestnosti sa môže stať niečo iné:
  - `vľavo` – pasca (strácaš život),
  - `vpravo` – hádanka z oblasti testovania,
  - `dopredu` – východ z jaskyne (potrebuješ kľúč).
- Kľúč získaš, ak správne odpovieš na jednu z náhodných testerských otázok.
- Hra sa končí, keď:
  - hráč získa kľúč a unikne,
  - alebo stratí všetky životy.

---

## 🔑 Cieľ projektu

- Precvičiť si **základy Pythonu**: podmienky, cykly, funkcie, zoznamy, slovníky, množiny.
- Vytvoriť jednoduchý **testovateľný projekt** s použitím:
  - vlastnej logiky,
  - simulovaného testovania pomocou manuálnych **test cases**.

---

## 🧪 Testovanie

Testovací dokument: [`TESTY.md`](./TESTY.md)  
Obsahuje manuálne testy: pozitívne, negatívne aj zlyhávajúci scenár.

---

## 🚀 Spustenie

1. Otvor súbor [`tester_adventure.py`](./tester_adventure.py)
2. Alebo si ho stiahni a spusť lokálne:

```bash
python tester_adventure.py
