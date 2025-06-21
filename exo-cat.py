# --------------------------------------------------------Alle requirements------------------------------------------- #
#prettytable met kleurtjes
from prettytable.colortable import ColorTable, Themes
table = ColorTable()
#ASCII-art
from pyfiglet import Figlet
f = Figlet(font='starwars')
#humanize
import humanize
# Activeer de Nederlandse taal
humanize.i18n.activate("nl_NL")

#datum importen
import datetime as dt

# ----------------------------------------------Overige instellingen-------------------------------------------------- #
#CLI leegmaken
import os
import platform


def clear_screen():
    try:
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')
    except:
        pass
    
##Standaard instellingen van de tabel
table.theme = Themes.DYSLEXIA_FRIENDLY
table.align = "r"
table.float_format = '.2'

# ---------------------------------------Helpfuncties voor de tekst opmaak-------------------------------------------- #
# Tekstopmaak
vet = '\033[1m'
onderstreept = '\033[4m'

# Standaard tekstkleuren
rood = '\033[31m'
groen = '\033[32m'
geel = '\033[33m'
blauw = '\033[34m'
magenta = '\033[35m'
cyan = '\033[36m'
reset = '\033[0m'

# ------------------------------Kolom maken en woordenboek met diverse ruimte-objecten-------------------------------- #
# Kolom namen
table.field_names = ["Exoplaneet",
                     "Afstand (lichtjaar)",
                     "Jaar ontdekt",
                     "Massa (x Aarde)",
                     "Temperatuur (°C)",
                     "Aantal manen"]

# Rijen toevoegen
table.add_rows([
    ["Proxima Centauri b", 4.24, 2016, 1.27, -39, 0],
    ["TRAPPIST-1e", 39.5, 2017, 0.77, 27, 0],
    ["LHS 1140 b", 40.7, 2017, 6.98, -47, 0],
    ["Kepler-186f", 560, 2014, 1.44, -85, 1],
    ["K2-18b", 124, 2015, 8.63, -73, 2],
    ["Wolf 1061c", 14.04, 2015, 4.30, -20, 0],
    ["HD 209458 b", 159, 1999, 221, 760, 0],
    ["WASP-12b", 1410, 2008, 439, 2210, 0],
    ["Aarde", 0, 0, 1, 15, 1],
])

# Informatie over diverse ruimte-objecten
ruimte_objecten = {
    1: {
        "naam": "ISS (International Space Station)",
        "type": "satelliet",
        "snelheid": 27600,
        "lanceerjaar": 1998,
        "status": "Actief, permanent bewoond",
        "info": "Permanent bewoond onderzoekslab in een baan om de Aarde, "
                "een samenwerkingsproject van meerdere landen.\n "
                "Dient als microzwaartekracht- en ruimtelaboratorium."
    },
    2: {
        "naam": "Voyager 1",
        "type": "ruimtesonde",
        "snelheid": 61160,
        "lanceerjaar": 1977,
        "status": "Actief, in interstellaire ruimte",
        "info": "De verst verwijderde menselijke object, "
                "momenteel in de interstellaire ruimte.\n "
                "Draagt de 'Golden Record' met geluiden en beelden van de Aarde."
    },
    3: {
        "naam": "Parker Solar Probe",
        "type": "zonnesonde",
        "snelheid": 692000,
        "lanceerjaar": 2018,
        "status": "Actief",
        "info": "Ontworpen om de buitenste corona van de zon te bestuderen.\n "
                "Het snelste object ooit gebouwd door mensen, "
                "met als doel de mysteries van de zonnewind op te lossen."
    },
    4: {
        "naam": "Apollo 10 Command Module",
        "type": "ruimtevaartuig",
        "snelheid": 39897,
        "lanceerjaar": 1969,
        "status": "Niet in gebruik - Historisch (museumstuk)",
        "info": "Het enige ruimtevaartuig dat ooit een bemande maanlander (Snoopy) "
                "heeft meegenomen naar de maan zonder te landen,\n als 'generale repetitie' voor de Apollo 11 landing."
    },
    5: {
        "naam": "Hubble Space Telescope",
        "type": "satelliet",
        "snelheid": 28000,
        "lanceerjaar": 1990,
        "status": "Actief",
        "info": "Een iconische ruimtetelescoop die sinds 1990 spectaculaire beelden van het heelal levert.\n "
                "Heeft onze kennis van kosmische afstanden en de leeftijd van het universum enorm uitgebreid."
    },
    6: {
        "naam": "Breakthrough Starshot Nanocraft",
        "type": "conceptuele interstellaire sonde",
        "snelheid": 2158500000,
        "lanceerjaar": "N.v.t. (concept)",
        "status": "Conceptueel",
        "info": "Een concept voor een piepkleine sonde die met lichtzeilen en krachtige lasers "
                "naar de dichtstbijzijnde sterren (Alpha Centauri) wil reizen,\n mogelijk binnen decennia."
    },
    7: {
        "naam": "James Webb Space Telescope (JWST)",
        "type": "ruimtetelescoop",
        "snelheid": 3600,
        "lanceerjaar": 2021,
        "status": "Actief",
        "info": "De opvolger van Hubble, geoptimaliseerd voor infraroodwaarnemingen "
                "om de vroegste sterrenstelsels en exoplaneten te bestuderen."
    },
    8: {
        "naam": "Sputnik 1",
        "type": "satelliet",
        "snelheid": 29000,
        "lanceerjaar": 1957,
        "status": "Niet in gebruik - Historisch",
        "info": "De eerste kunstmatige satelliet die door de mens in een baan om de Aarde werd gebracht,\n "
                "wat het ruimtetijdperk inluidde."
    },
    9: {
        "naam": "New Horizons",
        "type": "ruimtesonde",
        "snelheid": 58536,
        "lanceerjaar": 2006,
        "status": "Actief, op weg naar de Kuipergordel",
        "info": "De eerste sonde die Pluto en zijn manen van dichtbij bestudeerde,\n "
                "en daarna doorvloog naar objecten in de Kuipergordel zoals Arrokoth."
    }
}
lengte_woordenboek = len(ruimte_objecten)
# -------------------------------------------Alle functies uit men code----------------------------------------------- #

def space_travel():
    """Met deze functie kan de gebruiker een denkbeeldige reis maken naar een interstellair object"""
    # Hier kiest de gebruiker een vaartuig uit de lijst
    lijst_met_ruimte_objecten()
    list_repeat = extra_info()
    if list_repeat =="y":
        lijst_met_ruimte_objecten()
        extra_info()
    trip = int(input(f'\n{groen}Kies je vaartuig voor de reis naar een exoplaneet '
                     f'(voer het nummer in, 1-{lengte_woordenboek}): {reset}'))
    # Een beveiliging om foute invoer af te vangen
    if trip <= lengte_woordenboek:
        travel = ruimte_objecten[trip]

        # Hier kiest de gebruiker een exo-planeet uit de lijst
        for nummer, rij in enumerate(table.rows, start=1):
            print(f'{nummer}. {rij[0]} - Afstand: {rij[1]} ly')
        which_exo_planet = int(input(f'\n{groen}Met {travel["type"]} "{travel["naam"]}" aan boord, '
                                     f'naar welke exoplaneet wil je reizen? {reset}'))
        transform = which_exo_planet - 1
        choice_exo_planet = table.rows[transform]

        # snelheid voertuig en afstand tot exoplaneet extraheren uit dict en lijst
        snelheid_voertuig = travel['snelheid']
        afstand_exo_planeet = choice_exo_planet[1]

        # Berekenen van de afstand en reistijd naar een exoplaneet
        light_speed_kmu = 299_792.458 * 3600
        aantal_uur_per_jaar = 24 * 365.25
        afstand_exo_planeet_in_km = afstand_exo_planeet * light_speed_kmu * aantal_uur_per_jaar
        interstellar_reistijd = (afstand_exo_planeet_in_km / snelheid_voertuig) / aantal_uur_per_jaar

        # aankomst-jaar berekenen naar ruimtereis
        huidig_jaar = dt.datetime.now().year
        aankomst_jaar = huidig_jaar + interstellar_reistijd.__floor__()

        print(f'{geel}-De afstand tot: "{choice_exo_planet[0]}" is {humanize.intword(afstand_exo_planeet_in_km)} km. '
              f'\n-De reistijd met: "{travel["naam"]}" is {humanize.intword(interstellar_reistijd.__floor__())} jaar '
              f'\n-Als je vandaag zou vertrekken, '
              f'zou je aankomen in het jaar {humanize.intcomma(aankomst_jaar)}.{reset}')
    else:
        print(f'{rood}{trip} is geen geldige keuze{reset}')
    clear_screen()
    return

def extra_info():
    """"Deze functie geeft de gebruiker extra info wanneer hierom gevraagd wordt"""
    want_more_info = input(f'{geel}\nWil je meer informatie over een ruimte object? y/n{reset}')
    while True:
        if want_more_info.lower() =="y":
            more_info = int(input(f'{geel}Over welk object wil je meer info? (1-{lengte_woordenboek}){reset}'))
            # Controle of het getal dat de gebruiker invoert wel voorkomt in je keys uit de dict "ruimte_objecten"
            if more_info in ruimte_objecten.keys():
                voertuig_data = ruimte_objecten[more_info]

                ## Hier wordt Actief (groen) als het voorkomt bij "status" uit het woordenboek "ruimte_objecten".
                if "Actief" in voertuig_data['status']:
                    print(f'{magenta}{vet}-----{voertuig_data['naam']}-----{reset} '
                          f'\n{vet}{onderstreept}Lanceer jaar:\n{reset} {voertuig_data['lanceerjaar']}'
                          f'\n{vet}{onderstreept}Status:\n{reset} {groen}{voertuig_data['status']}{reset}'
                          f'\n{vet}{onderstreept}Info:\n{reset} {voertuig_data['info']}\n')
                ## Als dit niet het geval is wordt de tekst uit "status" (geel).
                else:
                    print(f'{magenta}{vet}-----{voertuig_data['naam']}-----{reset} '
                      f'\n{vet}{onderstreept}Lanceer jaar:\n{reset} {voertuig_data['lanceerjaar']}'
                      f'\n{vet}{onderstreept}Status:\n{reset} {rood}{voertuig_data['status']}{reset}'
                      f'\n{vet}{onderstreept}Info:\n{reset} {voertuig_data['info']}\n')
                # Vraag of de gebruiker verdere object informatie wil.
                know_more = input(f'{geel}Wil je meer weten over een object uit de lijst? y/n{reset}')
                if know_more.lower() == "n":
                    break
        # Hier volgt wat fout afhandeling
            else:
                print(f'{rood}{more_info} is hier geen geldige keuze{reset}')
        elif want_more_info.lower() =="n":
            break
        else:
            print(f'{rood}{want_more_info} is hier geen geldige keuze{reset}')
            break
    # Vraag of de gebruiker de lijst met ruimte-objecten opnieuw wil zien en geef een antwoord mee.
    nog_een_lijstje = input(f'{geel}Wil je nogmaals het lijstje met ruimte objecten zien? (y/n){reset}')
    lower = nog_een_lijstje.lower()
    return lower

def lijst_met_ruimte_objecten():
    for nummer, data in ruimte_objecten.items():
        print(f"{nummer}: "
              f"{magenta}{vet}{data['naam']}{reset} is een "
              f"{magenta}{vet}{data['type']}{reset} met snelheid "
              f"{magenta}{vet}{humanize.intcomma(data['snelheid'])}{reset} km/u.")
    return

def data_sorteren():
    """Met deze functie kan de data worden gesorteerd op grootte en alfabetische volgorde"""
    mijn_kolomnamen = {}
    ## hier worden alle kolommen uit de tabel genummerd en in een tijdelijk woordenboek gestopt
    for nummer, kolom in enumerate(table.field_names, start=1):
        print(f"{nummer}. {kolom}")
        mijn_kolomnamen[nummer] = kolom
    ## Op deze manier haal ik het woord uit de dict met een key die ik toewijs in de regel hierboven
    welke_waarde_sorteren = int(
        input(f"\n{groen}Maak een keuze: op welke kolom wil je sorteren? (1-{len(table.field_names)}): {reset}"))
    kolom_naam = mijn_kolomnamen[welke_waarde_sorteren]
    table.sortby = kolom_naam
    sorteerkeuze = int(input(
        f'{groen}In welke richting wil je "{kolom_naam}" sorteren?{reset}'
        f'\n{geel}'
        '\n1. Aflopend (hoog naar laag, Z-A)'
        '\n2. Oplopend (laag naar hoog, A-Z)'
        f'\nKies een optie (1 of 2): {reset}'
    ))
    if sorteerkeuze ==1:
        print(f'{groen}\nDe tabel is succesvol gesorteerd op "{kolom_naam}" '
              f'in aflopende volgorde (hoog naar laag / Z tot A).{reset}')
        table.reversesort = True
    elif sorteerkeuze ==2:
        table.reversesort = False
        print(f'{groen}\nDe tabel is succesvol gesorteerd op "{kolom_naam}" '
              f'in oplopende volgorde (laag naar hoog / A tot Z).{reset}')
    else:
        print(f'{rood}{sorteerkeuze} is geen geldige keuze.{reset}')
    print(table)
    clear_screen()
    return

def delete_row():
    """Met deze functie wordt een rij verwijderd"""
    for nummer, rij in enumerate(table.rows, start=1):
        print(f'{nummer}. {rij[0]}')
    print(f'\nElke exoplaneet in de tabel bevat {len(table.field_names)-1} verschillende datapunten.')
    welke_rij_verwijderen = int(input(f'\n{groen}Welke rij wil je verwijderen? 1-{len(table.rows)}: {reset}'))
    verwijder_rij = table.rows[welke_rij_verwijderen-1]
    print(f'{rood}Exoplaneet "{verwijder_rij[0]}" is met succes verwijderd{reset}')
    table.del_row(welke_rij_verwijderen-1)
    clear_screen()
    return

def delete_all_rows():
    """Deze functie verwijdert alle rijen uit je tabel"""
    verwijder_alle_rijen = int(input(
        f'{rood}Ben je er zeker van dat je alle rijen wilt verwijderen?{reset}\n'
        f'\n1: Bevestigen \n2: Annuleren\n> '
    ))
    if verwijder_alle_rijen == 1:
        print(f'{groen}Alle rijen verwijderd. Je keert terug naar het hoofdmenu.{reset}')
        table.clear_rows()
    elif verwijder_alle_rijen == 2:
        print(f'{geel}Geen wijzigingen doorgevoerd. Je keert terug naar het hoofdmenu.{reset}')
    else:
        print(f'{rood}{verwijder_alle_rijen} is geen geldige keuze.{reset}')
    clear_screen()
    return

def add_row():
    """hier kan de gebruiker een extra rij toevoegen en alle bijbehorende gegevens invullen"""
    entry = []
    # kwam er later achter dat het sorteren van de data crashte na het toevoegen van een nieuwe rij,
    # omdat variable = 'x' hier eerst altijd datatype str opleverde, omdat het stond gedefinieerd als
    #     for kolom in table.field_names:
    #     x = int(input(f'Wat wil je invullen voor {kolom}?'))
    #     entry.append(x)
    # Toen heb ik hier later slicing aan toegevoegd en de input als 'int' afgedwongen voor de overige kolommen
    x = input(f'{groen}Wat wil je invullen voor {table.field_names[0]}?{reset}')
    entry.append(x.title())
    for kolom in table.field_names[1::]:
        y = float(input(f'{geel}Wat wil je invullen voor {kolom}?{reset}'))
        #Deze sortering heb ik bedacht om bijvoorbeeld jaartellen niet als float in de tabel te krijgen
        if y.__floor__() - y ==0:
            entry.append(int(y))
        else:
            entry.append(y)
    table.add_row(entry)
    clear_screen()
    return

def add_column():
   """hier kan de gebruiker een extra kolom toevoegen en een waarde invullen voor iedere exoplaneet """
   nieuwe_waarden = []
   extra_column = input(
       f'{groen}Welke nieuwe eigenschap wil je toevoegen voor alle exoplaneten '
       f'(bijv. "Omlooptijd" of "Atmosfeer")?{reset}')
   for rij in table.rows:
       # Vraag de gebruiker om de waarde voor de nieuwe kolom voor elke exoplaneet in de tabel.
       waarde = float(
           input(f'{geel}Voer de waarde in voor \'{extra_column.title()}\' van exoplaneet \'{rij[0]}\':{reset} '))
       if waarde.__floor__() - waarde == 0:
           nieuwe_waarden.append(int(waarde))
       else:
           nieuwe_waarden.append(waarde)
    #toevoegen van de extra kolom en de nieuwe waarden als lijst
   table.add_column(extra_column.title(), nieuwe_waarden)
   clear_screen()
   return

def delete_column():
    """Met deze functie wordt een kolom verwijderd uit de tabel met exoplaneten"""
    tijdelijke_dict_verwijderen = {}
    for nummer, kolom in enumerate(table.field_names, start=1):
        print(f"{nummer}. {kolom}")
        tijdelijke_dict_verwijderen[nummer] = kolom
    welke_kolom_verwijderen = int(input(f'\n{groen}Welke kolom wil je verwijderen?: {reset}'))
    # Beveiliging zodat de kolom exoplaneten niet verwijderd kan worden
    if welke_kolom_verwijderen ==1:
        print(f'{rood}Je kunt de kolom: {tijdelijke_dict_verwijderen[1]} niet verwijderen{reset}')
        return
    # Beveiliging zodat de kolom afstand niet verwijderd kan worden
    elif welke_kolom_verwijderen ==2:
        print(f'{rood}Je kunt de kolom: {tijdelijke_dict_verwijderen[2]} niet verwijderen{reset}')
        return
    else:
        kolom_naam_verwijderen = tijdelijke_dict_verwijderen[welke_kolom_verwijderen]
        print(f'{rood}Kolom "{kolom_naam_verwijderen}" is met succes verwijderd{reset}')
        table.del_column(kolom_naam_verwijderen)
        clear_screen()
        return

def choice_of_theme():
    """Loop door de directory met thema's voor de package prettytable en vraag de gebruiker 1 te selecteren"""
    thema = {}
    for nummer, theme in enumerate(dir(Themes), start=1):
        if not theme.startswith("__"):
            print(f"{nummer}. {theme}")
            thema[nummer] = theme
    welk_thema = int(input(f'\n{groen}Welk thema wil je gebruiken? (1-{len(thema)}){reset}'))
    keuze_thema = thema[welk_thema]
    print(f'{cyan}Je hebt gekozen voor het thema {keuze_thema}{reset}')
    clear_screen()
    return keuze_thema

def hoofdmenu():
    """Hier kan de gebruiker een keuze maken welke bewerking uitgevoerd moet worden."""
    print(f.renderText('Exo-cat'))
    print(f"{blauw}{vet}Navigatiepaneel Exoplaneten Database{reset}")
    choice = int(input(
        '\n1. Exoplaneten lijst'
        '\n2. Sorteer Gegevens'
        '\n3. Nieuwe Planeet Toevoegen'
        '\n4. Planeet Verwijderen'
        '\n5. Database Leegmaken'
        '\n6. Nieuwe Eigenschap Toevoegen'
        '\n7. Eigenschap Verwijderen'
        '\n8. Thema Kiezen'
        '\n9. Start Ruimtereis!'
        '\n10. Afsluiten'
        '\n> '
    ))
    return choice
# -----------------------------------------De while loop met het keuze-menu------------------------------------------- #
while True:
    keuze = hoofdmenu()
    if keuze ==1:
        print(f'{cyan}{vet}Overzicht Exoplaneten:{reset}\n')
        print(table)
    elif keuze ==2:
        print(f'{cyan}{vet}Gegevens sorteren:{reset}\n')
        data_sorteren()
    elif keuze ==3:
        print(f'{cyan}{vet}Nieuwe Planeet Toevoegen:{reset}\n')
        add_row()
    elif keuze ==4:
        print(f'{cyan}{vet}Planeet Verwijderen:{reset}\n')
        delete_row()
    elif keuze == 5:
        print(f'{cyan}{vet}Database Leegmaken:{reset}\n')
        delete_all_rows()
    elif keuze ==6:
        print(f'{cyan}{vet}Nieuwe Eigenschap Toevoegen:{reset}\n')
        add_column()
    elif keuze ==7:
        print(f'{cyan}{vet}Eigenschap Verwijderen:{reset}\n')
        delete_column()
    elif keuze ==8:
        print(f'{cyan}{vet}Thema Kiezen:{reset}\n')
        thema_naam = choice_of_theme()
        # Voor de build-in functie 'getattr()' had ik toch echt even hulp van chatGPT nodig, ik had eerst gewoon
        # table.theme = thema_naam maar dat werkte niet. Na het even gebruiken van ChatGPT als docent heb ik begrepen
        # als je keuzes wilt maken je die functie uit een library niet zomaar een 'string' op die plaats kunt zetten.
        # Maar dat je ook letterlijk het attribuut (object) moet fetchen uit de library colortable.py
        table.theme = getattr(Themes, thema_naam)
    elif keuze ==9:
        print(f'{cyan}{vet}Start Ruimtereis!:{reset}\n')
        space_travel()
    elif keuze ==10:
        print(f'\n{blauw}Bedankt voor het gebruik van Exo-cat! Tot de volgende missie!{reset}')
        break

#Met plezier geschreven,
#Opgedragen aan m'n vader (L.M. Boer) die mij als kind vaak mee nam naar het Planetarium in Dwingeloo.