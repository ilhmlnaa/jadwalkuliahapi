<h2 align=center>Api to Get Class Data</h2>

<pre>Api to get class data at Gunadarma University. made in python using web scraping and flask</pre>


## Routes Api Endpoints

| Endpoints    | Query | Type  | Description            |
| ------------ | ----- | ----- | ---------------------- |
| `/api/jadkul`| kelas | route | Get data |

## Example Output
```
{
    "jadwal": {
        "Kamis": [
            {
                "dosen": "MEILANI B SIREGAR",
                "mataKuliah": "Sistem Berkas *",
                "ruang": "G224",
                "waktu": "3/4"
            },
            {
                "dosen": "MUHAMMAD RIDHA ALFARABI ISTIQLAL",
                "mataKuliah": "Statistika 2 **",
                "ruang": "G224",
                "waktu": "5/6/7"
            },
            {
                "dosen": "DIANA TRI SUSETIANINGTIAS",
                "mataKuliah": "Bisnis Informatika",
                "ruang": "G342",
                "waktu": "9/10"
            }
        ],
        "Sabtu": [
            {
                "dosen": "SANDHI PRAJAKA",
                "mataKuliah": "Arsitektur Komputer *",
                "ruang": "G115",
                "waktu": "1/2"
            },
            {
                "dosen": "MUHAMMAD EDY SUPRIYADI",
                "mataKuliah": "Pemrograman Berbasis Objek **",
                "ruang": "G115",
                "waktu": "3/4/5"
            },
            {
                "dosen": "RIRIN YULIYANTI",
                "mataKuliah": "Riset Operasional",
                "ruang": "G115",
                "waktu": "7/8"
            }
        ],
        "Selasa": [
            {
                "dosen": "DEA ADLINA",
                "mataKuliah": "Sistem Operasi */**",
                "ruang": "E228",
                "waktu": "1/2/3"
            },
            {
                "dosen": "NURHANAN",
                "mataKuliah": "Matematika Informatika 4 *",
                "ruang": "E228",
                "waktu": "4/5/6"
            },
            {
                "dosen": "M. ABDUL RIVAI",
                "mataKuliah": "Matematika Lanjut 2",
                "ruang": "E228",
                "waktu": "8/9/10"
            }
        ]
    },
    "kelas": "2ia09",
    "status": "sukses"
}
```




