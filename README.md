
# Examination Testverktyg

I detta projekt testar vi hemsidan "Läslistan" som är en webbsida där man kan 
välja ut sina favoriter från en katalog med böcker, eller lägga till nya. Beställaren är en organisation som vill öka barns och ungas läsande.

## Vad som testas

1. Favorit-markering av böcker
2. Lägg till ny bok
3. Favorit-markerade böcker hamnar i en lista

För mer detaljer se user stories i STORIES.md

## Instruktioner

Installera python genom att följa instruktionerna på hemsidan:
<https://www.python.org/downloads/>

### Starta testerna genom att skriva i terminalen

```commandline
git clone https://github.com/selim-kose/ex-testverktyg.git
cd ex-testverktyg
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
cd src
playwright install
behave
```

Adress till appen: <https://tap-vt25-testverktyg.github.io/exam--reading-list/>

---
