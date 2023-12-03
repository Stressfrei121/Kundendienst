import os
import random

from fashionsday import FashionsdayAPI
from webador import Webador


def main():
    api = FashionsdayAPI(os.getenv("FASHIONSDAY_API_KEY"))

    webador = Webador(os.getenv("WEBADOR_ACCESS_TOKEN"))

    products = api.get_products()

    webador.send_message("Hallo! Ich bin der Fashionsday-Bot. Wie kann ich Ihnen heute helfen?")

    interests = webador.get_input("Welchen Stil suchen Sie?")

    product = random.choice([product for product in products if product.category == interests])
    webador.send_message(f"Ich empfehle Ihnen das Produkt '{product.name}'. Es kostet {product.price} Euro und ist in der Kategorie '{product.category}' erhältlich. Klicken Sie hier, um weitere Informationen zu erhalten: {product.url}")

    webador.send_message("Können Sie mir sonst noch bei etwas helfen?")


if __name__ == "__main__":
    main()
