import streamlit as st
import numpy as np

# Judul aplikasi
st.title("Dekomposisi Nilai Singular (Singular Value Decomposition)")

# Fungsi untuk melakukan dekomposisi nilai singular
def svd_decomposition(matriks):
    U, s, V = np.linalg.svd(matriks)
    return U, s, V

# Input matriks
matriks = st.text_area("Masukkan matriks (dipisahkan dengan koma dan baris baru)", value="1, 2, 3\n4, 5, 6\n7, 8, 9")

# Mengubah input matriks menjadi array numpy
matriks = np.array([[float(x) for x in row.split(',')] for row in matriks.strip().split('\n')])

# Menampilkan matriks yang dimasukkan
st.subheader("Matriks yang Dimasukkan")
st.write(matriks)

# Melakukan dekomposisi nilai singular
U, s, V = svd_decomposition(matriks)

# Menampilkan hasil dekomposisi
st.subheader("Hasil Dekomposisi Nilai Singular")
st.write("Matriks U:")
st.write(U)
st.write("Matriks S (Nilai Singular):")
st.write(np.diag(s))
st.write("Matriks V Transpose:")
st.write(V)