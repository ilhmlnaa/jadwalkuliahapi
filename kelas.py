import requests
from bs4 import BeautifulSoup

def scrape_jadwal(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tabel_jadwal = soup.find('table', class_='table-custom')
    jadwal = {}

   
    if tabel_jadwal:
        rows = tabel_jadwal.find_all('tr')[1:]

        for row in rows:
            kolom = row.find_all('td')
            hari = kolom[1].get_text().strip()
            mata_kuliah = kolom[2].get_text().strip()
            waktu = kolom[3].get_text().strip()
            ruang = kolom[4].get_text().strip()
            dosen = kolom[5].get_text().strip()

            if hari not in jadwal:
                jadwal[hari] = []

            jadwal[hari].append({
                'mataKuliah': mata_kuliah,
                'waktu': waktu,
                'ruang': ruang,
                'dosen': dosen
            })

    return jadwal


