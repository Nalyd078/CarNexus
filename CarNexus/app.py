from flask import Flask, render_template, request

app = Flask(__name__)

merken = [
    {
        "merknaam": "Acura",
        "logo": "img/acura_logo.png",
        "production": "1986 - Heden",
        "1st_production_car": "img/acura-legend.webp",
        "recent_production_car": "img/acura-zdx.webp",
        "landvlag": "usa-flag-round.svg",
        "landvlag_id": "flag_usa",
        "herkomst": "Verenigde Staten",
        "populariteitscore": "0",
        "merk_info": {
            "merk_beschrijving": "Acura, opgericht in 1986 als Honda&#39;s luxe divisie, was het eerste Japanse premium automerk, gericht op innovatie en prestatie. Met iconische modellen zoals de Integra en NSX, staat Acura bekend om zijn &#39;Precision Crafted Performance&#39;, die luxe, comfort en geavanceerde technologieën combineert.<br><br> Gericht op de Noord-Amerikaanse markt en uitbreidend naar regio&#39;s zoals China, biedt Acura een reeks sportieve sedans en veelzijdige SUV&#39;s. Het merk zet sterk in op duurzaamheid en elektrificatie, waarmee het de toekomst van luxe mobiliteit blijft vormgeven."
        }
    },
    {
        "merknaam": "Audi",
        "logo": "img/audi_logo.png",
        "production": "1965 - Heden",
        "1st_production_car": "img/audi_type_a_1000.webp",
        "recent_production_car": "img/audi-q6-e-tron.webp",
        "landvlag": "germany-flag-round.svg",
        "landvlag_id": "flag_germany",
        "herkomst": "Duitsland",
        "populariteitscore": "7",
        "merk_info": {
            "merk_beschrijving": "Audi, met zijn oorsprong die teruggaat tot 1909 in Duitsland, staat symbool voor vooruitstrevende technologie en geavanceerd design. Onder het motto &apos;Vorsprung durch Technik&apos; (Voorsprong door techniek) heeft Audi zich gepositioneerd als een merk dat innovatie en luxe combineert, met toonaangevende modellen zoals de elegante A8 en de sportieve R8 die de essentie van het merk belichamen.<br><br>In het huidige tijdperk zet Audi sterk in op elektrificatie en duurzaamheid, met de e-tron lijn die de toekomst van elektrisch rijden vormgeeft. Deze toewijding aan innovatie en het streven naar een groenere toekomst, samen met hun rijke erfgoed in motorsport, versterkt Audi&#39;s reputatie als een fabrikant van voertuigen die prestaties, stijl en geavanceerde technologieën naadloos integreren."
        }
    },
    {
        "merknaam": "BMW",
        "logo": "img/bmw_logo.png",
        "production": "1927 - Heden",
        "1st_production_car": "img/bmw-dixi.webp",
        "recent_production_car": "img/bmw-i7.webp",
        "landvlag": "germany-flag-round.svg",
        "landvlag_id": "flag_germany",
        "herkomst": "Duitsland",
        "populariteitscore": "8",
        "merk_info": {
            "merk_beschrijving": "BMW, opgericht in München in 1916, begon met het bouwen van vliegtuigmotoren en evolueerde tot een symbool van sportieve luxe. Met modellen zoals de dynamische 3 Serie en de krachtige M-lijn, belichaamt BMW &#39;Freude am Fahren&#39;, een mix van rijplezier, technische innovatie en esthetische verfijning.<br><br>Deze Duitse fabrikant, wereldwijd geroemd, combineert traditioneel vakmanschap met toekomstgerichte technologieën, zoals te zien in hun i-serie elektrische voertuigen. BMW&#39;s toewijding aan sportiviteit en luxe blijft de kern vormen van zijn identiteit en aanbod."
        }
    },
    {
        "merknaam": "Chevrolet",
        "logo": "img/chevrolet_logo.png",
        "production": "1912 - Heden",
        "1st_production_car": "img/chevrolet-classic-six.webp",
        "recent_production_car": "img/chevrolet-traverse.webp",
        "landvlag": "usa-flag-round.svg",
        "landvlag_id": "flag_usa",
        "herkomst": "Verenigde Staten",
        "populariteitscore": "2",
        "merk_info": {
            "merk_beschrijving": "Chevrolet, opgericht in 1911 door Louis Chevrolet en William C. Durant in de Verenigde Staten, heeft zich ontwikkeld van een bescheiden begin tot een van de meest herkenbare automerken wereldwijd. Met een breed scala aan voertuigen, van de robuuste Silverado trucks tot de iconische Corvette en Camaro sportwagens, belichaamt Chevrolet de Amerikaanse geest van avontuur en vrijheid.<br><br>In recente jaren heeft Chevrolet zich gericht op innovatie en duurzaamheid, met de introductie van de Bolt EV als voorbeeld van hun inzet voor elektrische mobiliteit. Deze mix van historische betekenis, culturele invloed en toekomstgerichte technologieën maakt Chevrolet tot een merk dat zowel traditie eert als de toekomst van autorijden omarmt."
        }
    },
    {
        "merknaam": "Dacia",
        "logo": "img/dacia_logo.png",
        "production": "1968 - Heden",
        "1st_production_car": "img/dacia-1100.webp",
        "recent_production_car": "img/dacia-sandero.webp",
        "landvlag": "romania-flag-round.svg",
        "landvlag_id": "flag_romania",
        "herkomst": "Roemenië",
        "populariteitscore": "5",
        "merk_info": {
            "merk_beschrijving": "Dacia, oorspronkelijk opgericht in 1966 in Roemenië, begon als een producent van betaalbare auto&#39;s onder licentie van Renault. Het merk heeft zich sindsdien ontwikkeld tot een symbool van functionele eenvoud en waarde, en biedt betrouwbare voertuigen tegen toegankelijke prijzen. Met modellen zoals de Duster, een robuuste en veelzijdige SUV, en de Sandero, een praktische stadswagen, heeft Dacia een sterke positie verworven in de Europese markt en daarbuiten.<br><br>Dacia&#39;s recente focus ligt op het toegankelijk maken van duurzame technologieën, zoals te zien in hun Spring Electric, die elektrisch rijden binnen het bereik van een breder publiek brengt. Deze benadering, die waarde en duurzaamheid combineert, onderstreept Dacia&#39;s missie om efficiënte en betaalbare mobiliteitsoplossingen te bieden voor de moderne consument."
        }
    },
    {
        "merknaam": "Ferrari",
        "logo": "img/ferrari_logo.png",
        "production": "1947 - Heden",
        "1st_production_car": "img/ferrari-125-s.webp",
        "recent_production_car": "img/ferrari-sf90-stradale.webp",
        "landvlag": "italy-flag-round.svg",
        "landvlag_id": "flag_italy",
        "herkomst": "Italië",
        "populariteitscore": "1",
        "merk_info": {
            "merk_beschrijving": "Ferrari, opgericht door Enzo Ferrari in 1939 en officieel het merk gestart in 1947 in Maranello, Italië, is synoniem met snelheid, passie en exclusiviteit. Bekend om zijn opvallende rode racewagens en superieure prestaties op het circuit, heeft Ferrari een legendarische status verworven in de autosport, met talloze overwinningen in de Formule 1.<br><br>Buiten de racewereld staat Ferrari bekend om zijn luxe sportwagens zoals de 488 en de SF90 Stradale, die innovatieve technologie, baanbrekende ontwerpfilosofieën en ongeëvenaarde rijervaringen bieden. Ferrari blijft de grenzen van innovatie en design verleggen, terwijl het trouw blijft aan zijn erfgoed, waardoor het een tijdloos icoon blijft in de wereld van high-performance auto&#39;s."
        }
    },
    {
        "merknaam": "Honda",
        "logo": "img/honda_logo.png",
        "production": "1949 - Heden",
        "1st_production_car": "img/honda-t360.webp",
        "recent_production_car": "img/honda-prologue.webp",
        "landvlag": "japan-flag-round.svg",
        "landvlag_id": "flag_japan",
        "herkomst": "Japan",
        "populariteitscore": "6",
        "merk_info": {
            "merk_beschrijving": "Honda, opgericht in 1948 door Soichiro Honda in Japan, begon als een motorfietsenfabrikant en groeide uit tot een van de grootste en meest veelzijdige automerken ter wereld. Bekend om zijn innovatie, betrouwbaarheid en efficiëntie, biedt Honda een breed scala aan voertuigen, van de compacte Civic en de veelzijdige CR-V tot de geavanceerde Accord.<br><br>Honda zet zich ook in voor duurzame mobiliteit met ontwikkelingen in hybride en elektrische voertuigen, zoals de Insight en de volledig elektrische Honda e. Met een diepe betrokkenheid bij technologische vooruitgang en milieubewustzijn, blijft Honda zich richten op het creëren van auto&#39;s die plezierig zijn om in te rijden en die bijdragen aan een duurzamere toekomst."
        }
    },
    {
        "merknaam": "Nissan",
        "logo": "img/nissan_logo.png",
        "production": "1951 - Heden",
        "1st_production_car": "img/datsun-model-15.webp",
        "recent_production_car": "img/nissan-z.webp",
        "landvlag": "japan-flag-round.svg",
        "landvlag_id": "flag_japan",
        "herkomst": "Japan",
        "populariteitscore": "4",
        "merk_info": {
            "merk_beschrijving": "Nissan, opgericht in 1933 in Japan, heeft zich ontwikkeld tot een wereldwijde speler in de auto-industrie, bekend om zijn innovatieve ontwerpen en technologieën. Met een breed assortiment dat varieert van de betrouwbare Altima en de veelzijdige Rogue tot de sportieve 370Z, biedt Nissan voor ieder wat wils.<br><br>Een pionier in elektrische mobiliteit, Nissan lanceerde de Leaf, een van de eerste en bestverkochte elektrische auto&#39;s ter wereld, wat het merk&#39;s toewijding aan duurzaamheid en innovatie onderstreept. Nissan blijft vooroplopen in de ontwikkeling van elektrische en autonome voertuigtechnologieën, gericht op het aanbieden van slimme, veilige en milieuvriendelijke transportoplossingen."
        }
    },
    {
        "merknaam": "Opel",
        "logo": "img/opel_logo.png",
        "production": "1924 - Heden",
        "1st_production_car": "img/opel-patentmotorwagen.webp",
        "recent_production_car": "img/opel-corsa.webp",
        "landvlag": "germany-flag-round.svg",
        "landvlag_id": "flag_germany",
        "herkomst": "Duitsland",
        "populariteitscore": "3",
        "merk_info": {
            "merk_beschrijving": "Opel, opgericht in 1862 in Duitsland en oorspronkelijk een fabrikant van naaimachines en fietsen, stapte in 1899 de automobielindustrie binnen. Dit merk staat bekend om zijn betrouwbare, praktische auto&#39;s die een uitstekende waarde bieden, zoals de compacte Corsa en de ruime Astra.<br><br>Opel, nu onderdeel van de Stellantis-groep, blijft innoveren met een focus op duurzame mobiliteit, zoals blijkt uit de introductie van elektrische modellen zoals de Corsa-e en de Mokka-e. Met een rijke geschiedenis die zich uitstrekt over meer dan een eeuw, blijft Opel zich inzetten voor het leveren van kwaliteitsvoertuigen die Europese engineering en design combineren met functionaliteit en efficiëntie."
        }
    },
    {
        "merknaam": "Peugeot",
        "logo": "img/peugeot_logo.png",
        "production": "1947 - Heden",
        "1st_production_car": "img/peugeot-type2.webp",
        "recent_production_car": "img/peugeot-e3008.webp",
        "landvlag": "france-flag-round.svg",
        "landvlag_id": "flag_france",
        "herkomst": "Frankrijk",
        "populariteitscore": "5",
        "merk_info": {
            "merk_beschrijving": "Peugeot, opgericht in 1810 in Frankrijk en begonnen als fabrikant van koffiemolens en fietsen, maakte zijn entree in de automobielindustrie in 1889. Het merk staat bekend om zijn stijlvolle ontwerpen en innovatieve technologieën, zoals te zien in de elegante 508 en de veelzijdige 3008 SUV.<br><br>Peugeot heeft zich stevig gepositioneerd in de voorhoede van de transitie naar elektrische mobiliteit, met modellen zoals de volledig elektrische e-208 en de e-2008, die moderne technologie combineren met milieubewustzijn. Met een rijke erfenis die zich uitstrekt over meer dan twee eeuwen, blijft Peugeot zich richten op het leveren van auto&#39;s die design, comfort en efficiëntie naadloos integreren."
        }
    },
    {
        "merknaam": "Saab",
        "logo": "img/saab_logo.png",
        "production": "1950 - 2014",
        "1st_production_car": "img/saab-92.webp",
        "recent_production_car": "img/saab-9-3.webp",
        "landvlag": "sweden-flag-round.svg",
        "landvlag_id": "flag_sweden",
        "herkomst": "Zweden",
        "populariteitscore": "1",
        "merk_info": {
            "merk_beschrijving": "Saab, oorspronkelijk opgericht in 1937 in Zweden als een vliegtuigfabrikant, maakte de overstap naar de automobielindustrie in 1949 met de lancering van de Saab 92. Het merk stond bekend om zijn innovatieve ontwerp en techniek, met een sterke focus op veiligheid en turbotechnologie, zoals te zien in modellen zoals de 900 en de 9-3.<br><br>Ondanks zijn sterke erfgoed en loyale aanhang, heeft Saab financiële uitdagingen gekend en stopte met het produceren van auto&#39;s in 2011. De erfenis van Saab leeft echter voort, gewaardeerd voor zijn unieke benadering van autodesign en zijn bijdragen aan automotive engineering en veiligheidsinnovaties."
        }
    },
    {
        "merknaam": "Volkswagen",
        "logo": "img/vw_logo.png",
        "production": "1938 - Heden",
        "1st_production_car": "img/vw_type1_beetle.webp",
        "recent_production_car": "img/volkswagen-id-4.webp",
        "landvlag": "germany-flag-round.svg",
        "landvlag_id": "flag_germany",
        "herkomst": "Duitsland",
        "populariteitscore": "9",
        "merk_info": {
            "merk_beschrijving": "Volkswagen, opgericht in 1937 in Duitsland, is een van de grootste automerken ter wereld, bekend om zijn iconische modellen zoals de Beetle en de Golf. Volkswagen, wat &#39;de auto van het volk&#39; betekent, heeft zich altijd gericht op het bieden van betrouwbare, toegankelijke voertuigen voor een breed publiek.<br><br>In recente jaren heeft Volkswagen een grote verschuiving gemaakt richting duurzame mobiliteit, met de introductie van de ID. serie, waaronder de ID.3 en ID.4, die de toekomst van het merk in elektrische mobiliteit markeren. Met een sterke nadruk op innovatie, kwaliteit en duurzaamheid, blijft Volkswagen zich inzetten voor het ontwikkelen van voertuigen die aan de behoeften van moderne bestuurders voldoen."
        }
    }
]

merken = sorted(merken, key=lambda d: d['populariteitscore'], reverse=True)

@app.route("/")
@app.route("/home")
def home():
    return render_template("pages/home.html", merken=merken)

@app.route("/get_svg/<target>")
def get_svg(target):
    return render_template("svg/" + target)