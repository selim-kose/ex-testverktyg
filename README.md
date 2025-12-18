# Instruktioner

## Starta testerna genom att skriva i terminalen

Installera python genom att följa instruktionerna på hemsidan:
[Link to python download] https://www.python.org/downloads/

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

Adress till appen: `https://forverkliga.se/JavaScript/whose-turn/`

---
