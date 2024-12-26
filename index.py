import numpy as np
import pandas as pd

# Membuat dataset dalam bentuk dictionary
dataset = {
    'Siswa': ['S1', 'S2', 'S3', 'S4', 'S5'],
    'DTW': [2, 3, 4, 1, 3],
    'DTT': [4, 4, 3, 5, 2],
    'DMT': [4, 3, 2, 4, 1],
    'DDB': [3, 5, 5, 2, 3]
}

# Mengkonversi ke DataFrame dan set index
dataframe = pd.DataFrame(dataset).set_index('Siswa')

# Fungsi untuk menghitung jarak Manhattan
def hitung_jarak_manhattan(dataframe):
    jumlah_data = len(dataframe)
    matriks_jarak = np.zeros((jumlah_data, jumlah_data))
    
    for i in range(jumlah_data):
        for j in range(jumlah_data):
            matriks_jarak[i, j] = np.sum(np.abs(dataframe.iloc[i] - dataframe.iloc[j]))
    
    return matriks_jarak

# Menghitung matriks jarak
hasil_jarak = hitung_jarak_manhattan(dataframe)

# Membuat DataFrame untuk hasil perhitungan jarak
matriks_hasil = pd.DataFrame(
    hasil_jarak,
    index=dataframe.index,
    columns=dataframe.index
)

# Menampilkan hasil
print("\nData Kedisiplinan Siswa:")
print(dataframe)
print("\nMatriks Jarak Manhattan:")
print(matriks_hasil)