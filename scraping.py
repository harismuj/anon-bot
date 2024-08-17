import requests
from bs4 import BeautifulSoup
import re

def clean_text(text):
    # Menghapus tag HTML
    clean_html = re.sub(r'<[^>]*>', '', text)
    # Menghapus whitespace yang tidak perlu
    clean_whitespace = re.sub(r'\s+', ' ', clean_html)
    # Menghilangkan teks yang berawal dengan "ADVERTISEMENT"
    clean_ad = re.sub(r'ADVERTISEMENT.*', '', clean_whitespace)
    return clean_ad.strip()

# Mengirimkan permintaan HTTP ke halaman web
url = 'https://detik.com'  # Ganti dengan URL yang ingin Anda scrap
response = requests.get(url)

# Membuat objek BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

h2_tags = soup.find_all('h2', class_='media__title')

# Print the text content of each h2 tag
index = 0  # Change index here to display the desired h2 tag
if 0 <= index < len(h2_tags):
    # Mengambil link artikel dari tag <a>
    article_link = h2_tags[index].find('a')['href']

    # Melakukan permintaan HTTP ke artikel tersebut
    article_response = requests.get(article_link)
    article_soup = BeautifulSoup(article_response.text, 'html.parser')

    # Mengambil judul artikel
    article_title = article_soup.find('h1', class_='detail__title').text.strip()

    # Mengambil isi artikel
    article_content_tag = article_soup.find('div', class_='detail__body-text')
    # Membersihkan teks artikel
    article_content = clean_text(article_content_tag.get_text())
    
    # Menampilkan judul dan isi artikel yang bersih
    print(article_title.upper())
    print(article_content)

else:
    print("Index out of range.")
