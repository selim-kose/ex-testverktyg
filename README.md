
# Examination Testverktyg

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
