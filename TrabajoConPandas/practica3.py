import pandas as pd
import requests

#   datos_covid=requests.get("https://api.covid19api.com/summary").json()
datos_covid=requests.get("https://covid-api.com/api/regions").json()

covid19=pd.DataFrame.from_dict(datos_covid["data"])

print(covid19)