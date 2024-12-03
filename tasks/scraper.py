import requests
from bs4 import BeautifulSoup
from newspaper import Article

def scrape_and_clean_text(base_url, target_class):
    try:
        # Mengirimkan permintaan HTTP ke halaman utama
        response = requests.get(base_url)
        if response.status_code != 200:
            return f"Error: Gagal mengakses {base_url}, status code {response.status_code}"
        
        # Mengurai HTML dengan BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Menemukan elemen <a> dengan kelas target
        link = soup.find('a', class_=target_class)
        if not link:
            return "Link dengan kelas yang ditentukan tidak ditemukan."
        
        # Mengambil href dari elemen <a>
        href = link.get('href')
        if not href.startswith('http'):
            href = base_url.rstrip('/') + href  # Menangani link relatif jika diperlukan
        
        # Menggunakan newspaper untuk mengambil artikel
        article = Article(href)
        article.download()
        article.parse()
        
        # Mendapatkan teks artikel
        text = article.text
        
        # Preprocessing: Menghapus karakter newline (\n) dan spasi berlebih
        text_cleaned = text.replace('\n', ' ').strip()
        
        return text_cleaned
    except Exception as e:
        return f"Error: Terjadi kesalahan - {e}"

# Contoh penggunaan fungsi
base_url = "https://www.liputan6.com/"
target_class = "breaking-news__click"

cleaned_text = scrape_and_clean_text(base_url, target_class)
print(cleaned_text)
