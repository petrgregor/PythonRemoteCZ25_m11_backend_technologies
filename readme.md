# Project Hollymovies

## Popis projektu 
TBD (to be done)

## Struktura projektu
- `hollymovies` - složka projektu (obsahuje informace o celém projektu)
  - `__init__.py` - je zde jen proto, aby daná složka byla package
  - `asgi.py` - nebudeme potřebovat
  - `settings.py` - nastavení celého projektu
  - `urls.py` - zde jsou nastavené url cesty
  - `wsgi.py` - nebudeme používat
- `manage.py` - hlavní skript pro spouštění serveru, testů, migrací,... 

# Rady pro finální projekt
- jeden člen týmu vytvoří projekt
  - nainstaluje Django
```bash
pip install django  
```
  - vytvoří soubor requrements.txt
```bash
pip freeze > requrements.txt 
```
  - vytvoží Sjango projekt
```bash
django-admin startproject <nazev_projektu> .
```
  - nainstaluje dotenv
```bash
pip install python-dotenv
```
  - vytvoří soubor `.env`, který bude obsahovat citlivé informace a nebude součástí repozitáře
  - v `settings.py` nahradíme SECRET_KEY proměnnou z `.env` souboru 