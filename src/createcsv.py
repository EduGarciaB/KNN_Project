import pandas as pd
import requests

# URL del CSV
url = 'https://raw.githubusercontent.com/4GeeksAcademy/k-nearest-neighbors-project-tutorial/main/tmdb_5000_credits.csv'

# Hacer la solicitud usando requests con verificación SSL desactivada
response = requests.get(url, verify=False)

# Leer el contenido del CSV desde la respuesta
csv_content = response.content

# Guardar el contenido en un archivo CSV en la computadora
with open("tmdb_5000_credits.csv", "wb") as file:
    file.write(csv_content)



















