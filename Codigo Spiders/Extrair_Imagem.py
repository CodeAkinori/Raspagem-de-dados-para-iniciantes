import requests
import urllib.request
from bs4 import BeautifulSoup

try:
    response = requests.get('https://github.com/')
    response.raise_for_status()
    content = response.content
    site_html = BeautifulSoup(content, 'html.parser')

    img = site_html.find('img', attrs={'class': 'width-full height-auto js-globe-fallback-image'})
    if img:
        link = img.attrs['src']

        urllib.request.urlretrieve(f'{link}', 'img.png')
    else:
        print("Imagem não encontrada.")
except requests.exceptions.RequestException as e:
    print(f"Erro ao fazer a requisição: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")
