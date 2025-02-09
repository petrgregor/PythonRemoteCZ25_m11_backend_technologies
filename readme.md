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

- [x] seznam všech filmů (feature 1 - movies)
  - [ ] seřazení filmů
    - [ ] hodnocení 
    - [ ] délky
    - [ ] stáří
    - [ ] počet doporučení / počet hodnocení
    - [ ] počtu pozitivních cen ?
  - [ ] filtrování filmů
    - [x] žánr (feature 3.1)
    - [ ] země původu (Domácí úkol)
    - [ ] podle hodnocení
    - [ ] podle délky (interval)
    - [ ] počet doporučení / počet hodnocení (interval)
    - [ ] počtu pozitivních cen
  - [ ] streamovací služby (zda se nachází)
- [x] detail filmu (feature 2 - movie)
  - [ ] propojení s hercema
  - [ ] streamovací služby (zda se nachází)
- [ ] informace o hercích/tvůrcích (feature 4)
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
- [x] genre
  - [x] name
  - [x] movies -> ManyToMany(movie)
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
- [x] country
  - [x] name
  - [ ] movies -> ManyToMany(movie)
- [ ] creator
  - [ ] name
  - [ ] surname
  - [ ] date_of_birth
  - [ ] country -> ForeignKey(country)
  - [ ] acting -> ManyToMany(movie)
  - [ ] directing -> ManyToMany(movie)
- [x] movie
  - [x] title_orig
  - [x] title_cz
  - [x] genres -> ManyToMany(genre)
  - [ ] countries -> ManyToMany(country)
  - [x] length (minuty)
  - [x] description
  - [x] released_date
  - [x] released_year
  - [ ] cover_url
  - [ ] poster_url
  - [ ] trailer_url
  - [ ] stream_services -> ManyToMany(stream_services)
  - [ ] actors -> ManyToMany(creator)
  - [ ] directors -> ManyToMany(creator)

### Migrace
Migrace databáze se skládá ze dvou kroků:
- `python manage.py makemigrations` - vytvoření migračních skriptů
- `python manage.py migrate` - spuštění migračních skriptů -> změna schématu databáze

### Administrační panel
Musíme nejprve vytvořit superuser: `python manage.py createsuperuser`

### DUMP/LOAD databáze
```bash
pip install django-dump-load-utf8
```

DUMP - uložení dat z aplikace `viewer` do json souboru:
Přidáme `'django_dump_load_utf8',` do seznamu nainstalovaných
aplikací `INSTALLED_APPS` v souboru `settings.py`.

LOAD - načtení dat z json souboru do databáze:
```bash
python manage.py loaddatautf8 .\files\fixtures.json
```

> [!WARNING]
>
> Pozor! Přepíšou se původní hodnoty v databázi.

### Queries - práce s databází
#### .all()
Vrací kolekci všech nalezených záznamů z tabulky:
`Movie.objects.all()`

#### .get()
Vrátí jeden nalezený záznam (první, který splňuje podmínky):
`Movie.objects.get(pk=1)`

#### .filter()
Vrací kolekci záznamů, které splňují podmínky:
`Movie.objects.filter(pk=1)`

`Movie.objects.filter(title_orig="The Green Mile")`

`Movie.objects.filter(released_year=1995)`

`Movie.objects.filter(released_year__gt=1995)` -- `__gt` => "větší než" (greater then)

`Movie.objects.filter(released_year__gte=1995)` -- `__gte` => "větší rovno" (greater then equal)

`Movie.objects.filter(released_year__lt=1995)` -- `__lt` => "menší než" (less then)

`Movie.objects.filter(released_year__lte=1995)` -- `__lte` => "menší rovno" (less then equal)

`drama = Genre.objects.get(name="Drama")`

`Movie.objects.filter(genres=drama)`

`Movie.objects.filter(genres=Genre.objects.get(name="Drama"))`

`Movie.objects.filter(genres__name="Drama")`

`Movie.objects.filter(title_orig__contains="Gump")`

`Movie.objects.filter(genres__name="Drama", released_year=1995)` -- více podmínek, defaultně AND

`Movie.objects.filter(genres__name="Drama").filter(released_year=1995)` -- metody lze řetězit za sebe

`Movie.objects.filter(title_orig__in=["Forrest Gump", "Se7en"])`

`Movie.objects.filter(released_year=1995)`

`Movie.objects.exclude(released_year=1995)`

Test, zda existuje alespoň jeden záznam:
`Movie.objects.filter(released_year=1995).exists()`

Spočítáme počet vyhovujících záznamů:
`Movie.objects.filter(released_year=1995).count()`

Agregační funkce:
`from django.db.models import Avg, Min, Max`

`Movie.objects.aggregate(Avg("length"))`

`Movie.objects.aggregate(Avg("length"), Min("length"), Max("length"))`

Group_by:
`from django.db.models import Count`

`Movie.objects.values("genres").annotate(count=Count("genres"))`

Uspořádání výsledků:
`Movie.objects.all()`

`Movie.objects.all().order_by("released_year")` -- uspořádání vzestupně

`Movie.objects.all().order_by("-released_year")` -- uspořádání sestupně

### Create
`thriller = Genre.objects.create(name="Thriller")`

```python
scifi = Genre(name="Sci-fi")
scifi.save()
```

### Update
`Movie.objects.filter(id=5).update(description="Nový popis")`

```python
movie = Movie.objects.get(pk=5)
movie.description = "Nový popis"
movie.save()
```

### Delete
`Movie.objects.get(id=3).delete()`

`Movie.objects.filter(genres__name="Dokumentární").delete()`

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