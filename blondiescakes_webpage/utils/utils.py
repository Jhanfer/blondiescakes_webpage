import reflex as rx
import json
from decimal import Decimal

#Language#
def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'"),

#Page Preview#
preview="favicon.ico"


_meta=[
    {"property":"og:type","content":"website"},
    {"property":"og:image","content":preview},
    {"property":"instagram:card","content":"summary_large_image"},
    {"property":"instagram:site","content":"@blondies_cake"}]


#index@#
index_title="Blondie´s Cake"
index_description="Blondie´s Cake | En Blondie´s Cake, entendemos que cada pastel significa una ocasión especial. Por ello empleamos ingredientes de la mejor calidad y lo actual para elaborar postres a medida hechos a mano..."
index_meta=[
    {"property":"og:title","content":index_title},
    {"property":"og:description","content":index_description}]
index_meta.extend(_meta)


#About Us#
about_us_title="Blondie´s Cake | Nosotros"
about_us_description="Apesar de tener mas 8 años de experiencia en el sector, Blondies nace en un momento de aislamiento social con sus restricciones, la Pandemia del Covid 2019, tuve que enfrentar muchas dificultades por falta de trabajo, debido a..."
about_us_meta=[
    {"property":"og:title","content":about_us_title},
    {"property":"og:description","content":about_us_description}]
about_us_meta.extend(_meta)


#Routes#
INDEX_ROUTE="/"
ABOUTUS_ROUTE="/nosotros"


"""
#Schema Markup#

json_ld = {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Blondie´s Cake",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "Carrera 93 #2C - 126",
        "addressLocality": "Cali",
        "addressRegion": "Valle del Cauca",
        "postalCode": "760034"
    },
    "image": "https://blondiescakes.reflex.run/navbar/navbar.png",
    "telephone": "+57 322 5360402",
    "url": "https://blondiescakes.reflex.run",
    "paymentAccepted": [
        "cash"
    ],
    "openingHours": "Mo,Tu,We,Th,Fr,Sa 08:00-18:00",
    "openingHoursSpecification": [
        {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday"
        ],
        "opens": "08:00",
        "closes": "18:00"
        }
    ],
    "geo": {
        "@type": "GeoCoordinates",
        "latitude": "3.4516467",
        "longitude": "-76.5319854"
    },
    "priceRange": "$"
}

#HTML Inserter#

def json_script() -> rx.Component:
    json_ld_content = json.dumps(json_ld,ensure_ascii=False, indent=2)
    return rx.el.script( #se usa rx.el.script para asegurarse de que el script se coloque en el <head>
        json_ld_content,
        type="application/ld+json"
    )
"""

class JsonLDScript():
    def json_script() -> rx.Component:

        json_ld = {
    "@context": "http://www.schema.org",
    "@type": "Bakery",
    "name": "Blondie´s Cake",
    "url": "https://blondiescakes.reflex.run",
    "logo": "https://blondiescakes.reflex.run/navbar/navbar.png",
    "priceRange": "$",
    "image": "https://blondiescakes.reflex.run/navbar/navbar.png",
    "description": "Apesar de tener mas 8 años de experiencia en el sector, Blondies nace en un momento de aislamiento social con sus restricciones, la Pandemia del Covid 2019, tuve que enfrentar muchas dificultades por falta de trabajo, debido a que la empresa donde laboraba cerrò sus puertas, la falta de movilidad entre otros obstáculos, me vi en la necesidad de crear productos de pasteleria y reposterìa personalizados, ofreciendo una gran variedad de opciones y alternativas a mis clientes",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "Carrera 93 #2C - 126",
        "addressLocality": "Cali",
        "addressRegion": "Valle del Cauca",
        "postalCode": "760034",
        "addressCountry": "Colombia"
    },
    "geo": {
        "@type": "GeoCoordinates",
        "latitude": "3.375488267679746",
        "longitude": "-76.54964339278742"
    },
    "hasMap": "https://maps.app.goo.gl/V7B7aJhAvpMY4Fta7",
    "openingHours": "Mo 08:00-18:00 Tu 08:00-18:00 We 08:00-18:00 Th 08:00-18:00 Fr 08:00-18:00 Sa 08:00-18:00",
    "telephone": "+57 322 5360402"
    }
        
        return rx.el.script( #se usa rx.el.script para asegurarse de que el script se coloque en el <head>
            json.dumps(json_ld, indent=2, ensure_ascii=False),
            type="application/ld+json"
        )
