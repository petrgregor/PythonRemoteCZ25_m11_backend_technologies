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

## Spuštění serveru
```bash
python manage.py runserver
```

Případně můžeme zadat ručně číslo portu:
```bash
python manage.py runserver 8001
```

## Vytvoření aplikace
```bash
python manage.py startapp <nazev_aplikace>
```

> [!WARNING]
> Nesmíme zapomenout zaregistrovat aplikaci do souboru `settings.py`:
> ```python
> INSTALLED_APPS = [
>     'django.contrib.admin',
>     'django.contrib.auth',
>     'django.contrib.contenttypes',
>     'django.contrib.sessions',
>     'django.contrib.messages',
>     'django.contrib.staticfiles',
> 
>     'viewer',
> ]
> ```
 
### Struktura aplikace
- `viewer` - složka aplikace
  - `migrations` - složka obsahující migrační skripty
  - `__init__.py` - prázdný soubor, slouží k tomu, aby složka fungovala jako package
  - `admin.py` - zde uvádíme modely, které se budou zobrazovat v admin sekci
  - `apps.py` - nastavení aplikace
  - `models.py` - definice modelů (schéma databáze)
  - `tests.py` - testy
  - `views.py` - funcionalita

## Funkcionalita

- [ ] seznam všech filmů 
  - [ ] seřazení filmů
    - [ ] hodnocení 
    - [ ] délky
    - [ ] stáří
    - [ ] počet doporučení / počet hodnocení
    - [ ] počtu pozitivních cen ?
  - [ ] filtrování filmů
    - [ ] žánr
    - [ ] země původu
    - [ ] podle hodnocení
    - [ ] podle délky (interval)
    - [ ] počet doporučení / počet hodnocení (interval)
    - [ ] počtu pozitivních cen
  - [ ] streamovací služby (zda se nachází)
- [ ] detail filmu
  - [ ] propojení s hercema
  - [ ] streamovací služby (zda se nachází)
- [ ] informace o hercích/tvůrcích
  - [ ] ocenění ? 
- [ ] komentáře, reviews, hodnocení filmů
- [ ] watch list (viděl, chci vidět) ?
- [ ] vyhledávání
- [ ] vkládání, editace a mazání filmů
  - [ ] na základě nějakých práv uživatele 
- [ ] vkládání, editace a mazání herců/tvůrců
  - [ ] na základě nějakých práv uživatele
- [ ] admin dashboard
  - [ ] statistiky (počet uživatelů, filmů, herců)
- [ ] chat ?

## Databáze

### Modely

- [ ] subgenre
  - [ ] name
  - [ ] genre -> ForeignKey(genre)
- [ ] genre
  - [ ] name
  - [ ] movies -> ManyToMany(movie)
- [ ] stream_service
  - [ ] name
  - [ ] movies -> ManyToMany(movie)
- [x] user
- [ ] review
  - [ ] comment
  - [ ] rating
  - [ ] recommendation
  - [ ] user -> ForeignKey(user)
  - [ ] movie -> ForeignKey(movie)
- [ ] review_likes
  - [ ] like 
  - [ ] review -> ForeignKey(review)
  - [ ] reviewer -> ForeignKey(user)
- [ ] country
  - [ ] name
  - [ ] movies -> ManyToMany(movie)
- [ ] creator
  - [ ] name
  - [ ] surname
  - [ ] date_of_birth
  - [ ] country -> ForeignKey(country)
  - [ ] acting -> ManyToMany(movie)
  - [ ] directing -> ManyToMany(movie)
- [ ] movie
  - [ ] title_orig
  - [ ] title_cz
  - [ ] genres -> ManyToMany(genre)
  - [ ] countries -> ManyToMany(country)
  - [ ] length
  - [ ] description
  - [ ] released_date
  - [ ] released_year
  - [ ] cover_url
  - [ ] poster_url
  - [ ] trailer_url
  - [ ] stream_services -> ManyToMany(stream_services)
  - [ ] actors -> ManyToMany(creator)
  - [ ] directors -> ManyToMany(creator)

# Rady pro finální projekt
- jeden člen týmu vytvoří projekt
  - nainstaluje Django
  ```bash
  pip install django  
  ```
  - vytvoří soubor requirements.txt
  ```bash
  pip freeze > requirements.txt 
  ```
  - vytvoří Django projekt
  ```bash
  django-admin startproject <nazev_projektu> .
  ```
  - nainstaluje dotenv
  ```bash
  pip install python-dotenv
  ```
  - vytvoří soubor `.env`, který bude obsahovat citlivé informace a nebude součástí repozitáře
  - v `settings.py` nahradíme SECRET_KEY proměnnou z `.env` souboru 
  - vytvoří git repozitář
    - vytvoří .gitignore soubor
    ```git
    /.idea
    /.env
    /db.sqlite3
    ```
    - odešle repozitář na GitHub
    - nasdílí ostatním členům týmu adresu repozitáře
    - nastaví spolupracovníky (Settings -> Collaborators -> Add people)
- ostatní členové
  - naklonují si projekt
  - vytvoří virtuální prostředí (.venv)
  - nainstalují si potřebné balíčky ze souboru requirements.txt
  ```bash
  pip install -r requirements.txt 
  ```
  - vytvoří `.env` soubor obsahující SECRET_KEY