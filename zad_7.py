# Należy w pythonie zrobić klasę Brawery , która będzie zawierała takie atrybuty jakich
# dostarcza API wraz z odpowiednim typowaniem.
# W klasie należy zaimplementować magiczną metodę __str__ która będzie
# opisywała dane przechowywane w obiekcie.
# Skrypt ma się połączyć do API i pobrać 20 pierwszych obiektów, a następnie
# utworzyć listę 20 instancji klasy Brawery , którą przeiteruje i wyświetli każdy obiekt z
# osobna.
# import requests as requests

# response = requests.get("https://api.openbrewerydb.org/breweries")
# print(response.status_code)
# print(response.json())


# class Brawery:
#     def __init__(self, id, name, brewery_type, street, address_2, address_3, city, state, county_province,
#                  postal_code, #                  country, longitude, latitude, phone, website_url, updated_at,
#                  created_at):
#         self.id = id
#         self.name = name
#         self.brewery_type = brewery_type
#         self.street = street
#         self.address_2 = address_2
#         self.address_3 = address_3
#         self.city = city
#         self.state = state
#         self.county_province = county_province
#         self.postal_code = postal_code
#         self.country = country
#         self.longitude = longitude
#         self.latitude = latitude
#         self.phone = phone
#         self.website_url = website_url
#         self.updated_at = updated_at
#         self.created_at = created_at

#     def __str__(self):
#         return f'Browar {self.brewery_type} {self.name} miesci sie przy ulicy {self.street}) ' \
#               f'w miescie {self.city}, {self.country}. Telefon kontaktowy: {self.phone}. ' \
#               f'Adres strony internetowej: {self.website_url}'
