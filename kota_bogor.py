#mengolah data
import pandas as pd

#visualisasi dasar 
import matplotlib.pyplot as plt

#visualisasi lanjutan estetika
import seaborn as sns

df = pd.read_csv("dinkes-od_17107_jml_balita__kategori_balita_gizi_buruk_v5_data.csv")

#menampilkan 5 baris pertama
print(df.head())

#apakah ada null?
df.info()
df.describe()
df.isnull().sum()
print(df['nama_kabupaten_kota'].value_counts())
print(df['kategori_gizi_buruk'].value_counts())

#filteringData untuk kota bogor
df_bogor = df[df['nama_kabupaten_kota'] == 'KOTA BOGOR']

#menampilkan 5 baris pertama
print(df_bogor.head())

#jumlahkan semua kategori gizi buruk berdasarkan tahun
df_bogor_grouped = df_bogor.groupby('tahun')['jumlah_balita'].sum()
#menampilkan hasil
df_plot = df_bogor_grouped.reset_index()
print(df_bogor_grouped)


#visualisasi data

#kanvas dengan lebar 10 inci dan tinggi 6 inci
fig, ax = plt.subplots(figsize=(10, 6))

#membuat bar chart dengan warna 'skyblue'
bars = df_bogor_grouped.plot(kind='bar', color = 'skyblue', ax=ax) 

#garis bantu untuk grid
plt.grid(True, axis = 'y' , linestyle = '--' , alpha  = 0.4)

#title
plt.title("Jumlah Balita Gizi Buruk di Kota Bogor (2019-2024)", fontdict={'fontsize': 16, 'fontweight': 'bold'})
plt.xlabel('tahun', fontsize = 12)
plt.ylabel('Jumlah Balita Gizi Buruk', fontsize = 12)
plt.xticks(rotation = 0)

#Menambahkan Label Angka di Atas Batang
# for bar in bars.patches:
#     plt.text(bar.get_x() + bar.get_width() / 2,
#              bar.get_height() + 100,
#              f'{int(bar.get_height())}',
#              ha = 'center' , va='bottom', fontsize = 10)
    
plt.tight_layout()
plt.show()
