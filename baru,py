import pandas as pd 
import streamlit as st
import numpy as np
from st_aggrid import AgGrid, JsCode
from st_aggrid.grid_options_builder import GridOptionsBuilder

st.set_page_config(page_title='Verifikasi F3', layout="wide")

# Fungsi untuk membuat DataFrame gabungan
def copyDataframe(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini):
    # Membuat DataFrame untuk periode lalulalu
    juruslalulalu = pd.DataFrame({
        'BLTH': lalulalu.get('BLTH', pd.Series(dtype='object')),
        'IDPEL': lalulalu.get('IDPEL', pd.Series(dtype='int64')),
        'LWBPPAKAI': lalulalu.get('LWBPPAKAI', pd.Series(dtype='float64')) 
    })

    # Membuat DataFrame untuk periode lalu
    juruslalu = pd.DataFrame({
        'BLTH': lalu.get('BLTH', pd.Series(dtype='object')),
        'IDPEL': lalu.get('IDPEL', pd.Series(dtype='int64')),
        'LWBPPAKAI': lalu.get('LWBPPAKAI', pd.Series(dtype='float64'))
    })

    # Membuat DataFrame untuk periode akhir
    jurusakhir = pd.DataFrame({
        'BLTH': akhir.get('BLTH', pd.Series(dtype='object')),
        'IDPEL': akhir.get('IDPEL', pd.Series(dtype='int64')),
        'NAMA': akhir.get('NAMA', pd.Series(dtype='object')),
        'TARIF': akhir.get('TARIF', pd.Series(dtype='object')),
        'DAYA': akhir.get('DAYA', pd.Series(dtype='float64')),
        'SLALWBP': akhir.get('SLALWBP', pd.Series(dtype='float64')),
        'LWBPCABUT': akhir.get('LWBPCABUT', pd.Series(dtype='float64')),
        'LWBPPASANG': akhir.get('LWBPPASANG', pd.Series(dtype='float64')),
        'SAHLWBP': akhir.get('SAHLWBP', pd.Series(dtype='float64')),
        'LWBPPAKAI': akhir.get('LWBPPAKAI', pd.Series(dtype='float64')),
        'DLPD': akhir.get('DLPD', pd.Series(dtype='float64'))
    })

    # Menggabungkan DataFrames
    kroscek_temp_1 = pd.merge(juruslalulalu, juruslalu, on='IDPEL', how='right')
    kroscek_temp = pd.merge(kroscek_temp_1, jurusakhir, on='IDPEL', how='right')
    delta = kroscek_temp['LWBPPAKAI'] - kroscek_temp['LWBPPAKAI_y']

    # Definisi path untuk foto
    path_foto1 = 'https://portalapp.iconpln.co.id/acmt/DisplayBlobServlet1?idpel='
    path_foto2 = '&blth='

    # Membuat DataFrame akhir sesuai format yang diinginka
    kroscek = pd.DataFrame({
        'BLTH': blth_kini,
        'IDPEL': kroscek_temp['IDPEL'].astype(str),
        'NAMA': kroscek_temp['NAMA'],
        'TARIF': kroscek_temp['TARIF'],
        'DAYA': kroscek_temp['DAYA'],
        'SLALWBP': kroscek_temp['SLALWBP'],
        'LWBPCABUT': kroscek_temp['LWBPCABUT'],
        'SELISIH STAN BONGKAR': kroscek_temp['SLALWBP'] - kroscek_temp['LWBPCABUT'],
        'LWBP PASANG': kroscek_temp['LWBPPASANG'],
        'SAHLWBP': kroscek_temp['SAHLWBP'],
        'KWH 10': kroscek_temp['LWBPPAKAI'],
        'KWH 09': kroscek_temp['LWBPPAKAI_y'],
        'KWH 08': kroscek_temp['LWBPPAKAI_x'],
        'DELTA PEMKWH': delta,
    })

    # Perhitungan persentase sebagai numerik
    percentage = (delta) / kroscek_temp['LWBPPAKAI_y'] * 100

    # Isi kolom % dengan nilai numerik, set 0 jika SAHLWBP_y adalah 0
    kroscek['%'] = np.where(kroscek_temp['LWBPPAKAI'] != 0, percentage, 0)

    # Sortir dataframe berdasarkan kolom % dari terbesar ke terkecil
    
    #kroscek = kroscek.sort_values(by='%', ascending=False)

    # Tambahkan simbol % setelah pengurutan
    kroscek['%'] = kroscek['%'].astype(int).map('{}%'.format)

    # Buat kolom KET berdasarkan nilai percentage
    kroscek['KET'] = np.where(percentage >= 40, 'NAIK', 'TURUN')
    kroscek['DLPD'] = kroscek_temp['DLPD']
    kroscek['FOTO AKHIR'] = path_foto1 + kroscek_temp['IDPEL'].astype(str) + path_foto2 + blth_kini
    kroscek['FOTO LALU'] = path_foto1 + kroscek_temp['IDPEL'].astype(str) + path_foto2 + blth_lalu
    kroscek['FOTO LALU2'] = path_foto1 + kroscek_temp['IDPEL'].astype(str) + path_foto2 + blth_lalulalu
    kroscek['KET_KWH'] = ['SESUAI' for _ in range(len(kroscek))]
    #kroscek['KET_KWH'] = np.where(kroscek_temp['SAHLWBP_y'] == 0, 'SESUAI', 'TIDAK SESUAI')
    kroscek['TINDAK LANJUT'] = ''
    kroscek['HASIL PEMERIKSAAN'] = ''

    # Menambahkan tautan HTML ke kolom gambar
    kroscek['FOTO AKHIR'] = kroscek['FOTO AKHIR'].apply(lambda x: f'<a href="{x}" target="_blank"><button style="background-color: #007BFF; color: white; border: none; border-radius: 4px; padding: 5px 10px;">Lihat Foto</button></a>')
    kroscek['FOTO LALU'] = kroscek['FOTO LALU'].apply(lambda x: f'<a href="{x}" target="_blank"><button style="background-color: #007BFF; color: white; border: none; border-radius: 4px; padding: 5px 10px;">Lihat Foto</button></a>')
    kroscek['FOTO LALU2'] = kroscek['FOTO LALU2'].apply(lambda x: f'<a href="{x}" target="_blank"><button style="background-color: #007BFF; color: white; border: none; border-radius: 4px; padding: 5px 10px;">Lihat Foto</button></a>')

    # Mengembalikan dataframe kroscek
    return kroscek

# Fungsi untuk menampilkan DataFrame dengan selectbox di kolom KET_KWH
def show_image_with_selectbox(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini):
    df = copyDataframe(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)
    if df.empty:
        st.warning("No data available after applying the filter.")
        return

    # Konfigurasi AgGrid
    gd = GridOptionsBuilder.from_dataframe(df)
    gd.configure_default_column(editable=True)
    gd.configure_column('KET_KWH', editable=True, cellEditor='agSelectCellEditor', cellEditorParams={'values': ['SESUAI', 'TIDAK SESUAI', 'FOTO BURAM']})
    
    grid_options = gd.build()

    # Tampilkan AgGrid dengan konfigurasi selectbox di kolom KET_KWH
    grid_response = AgGrid(df, gridOptions=grid_options, editable=True, height=400)

    # Akses dataframe yang sudah diperbarui oleh pengguna
    updated_df = grid_response['data']
    st.write("DataFrame yang diperbarui:")
    st.dataframe(updated_df)


def maksFilter(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini):
    kroscek = copyDataframe(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)
    maks_df = kroscek[kroscek['DLPD_KINI'].isin(['L STAND METER MUNDUR'])]
    return maks_df

def naikFilter(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini):
    kroscek = copyDataframe(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)

    # Filter untuk yang memiliki % >= 40
    naik_df = kroscek[kroscek['%'].str.rstrip('%').astype(int) >= 40]
    return naik_df

def turunFilter(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini):
    kroscek = copyDataframe(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)

    # Filter untuk yang memiliki % < 40
    turun_df = kroscek[kroscek['%'].str.rstrip('%').astype(int) < 40]
    return turun_df

def show_image_maks(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini):
    df = copyDataframe(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)
    if df.empty:
        st.warning("No data available after applying the filter.")
        return

    # Display the DataFrame with clickable links using st.markdown
    st.markdown(df.to_html(escape=False), unsafe_allow_html=True)

# Fungsi filter lain
def show_image_naik(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini):
    df = naikFilter(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)
    if df.empty:
        st.warning("No data available after applying the filter.")
        return

    # Display the DataFrame with clickable links using st.markdown
    st.markdown(df.to_html(escape=False), unsafe_allow_html=True)

def show_image_turun(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini):
    df = turunFilter(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)
    if df.empty:
        st.warning("No data available after applying the filter.")
        return

    # Display the DataFrame with clickable links using st.markdown
    st.markdown(df.to_html(escape=False), unsafe_allow_html=True)    

# Layout Columns
col = st.columns((1.5, 5), gap='medium')

with col[0]:
    st.header('Billing Management Application')

    # Input Bulan
    set_bulan = st.columns((0.75, 0.75, 0.75), gap='medium')
    with set_bulan[0]:
        blth_lalulalu = st.text_input('Masukkan periode bulan lalu2 (YYYYMM)')
    with set_bulan[1]:
        blth_lalu = st.text_input('Masukkan periode bulan lalu (YYYYMM)')
    with set_bulan[2]:
        blth_kini = st.text_input('Masukkan periode bulan kini (YYYYMM)')

    # File Uploader
    file_lalulalu = st.file_uploader("Upload Data 2 Periode Sebelumnya")
    file_lalu = st.file_uploader("Upload Data Periode Sebelumnya")
    file_akhir = st.file_uploader("Upload Data Periode Sekarang")

# Proses jika tombol ditekan dan file sudah diunggah
if st.button("Proses"):
    if file_lalulalu and file_lalu and file_akhir:
        lalulalu = pd.read_excel(file_lalulalu)
        lalu = pd.read_excel(file_lalu)
        akhir = pd.read_excel(file_akhir)

        # Display the DataFrame
        show_image_maks(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)

    else:
        st.warning("Mohon upload kedua file terlebih dahulu.")

# Tabs
with col[1]:
    st.markdown('#### Main')
    tabs = st.tabs(['SEMUA', 'DIATAS 40%', 'DIBAWAH 40%'])

    # Tab SEMUA
    with tabs[0]:
        st.write("Semua")
        if 'lalulalu' in locals() and 'lalu' in locals() and 'akhir' in locals():
            st.dataframe(copyDataframe(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini))

    # Tab DIATAS 40%
    with tabs[1]:
        st.write("NAIK")
        if 'lalulalu' in locals() and 'lalu' in locals() and 'akhir' in locals():
            show_image_naik(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)

    # Tab TURUN
    with tabs[2]:
        st.write("TURUN")
        if 'lalulalu' in locals() and 'lalu' in locals() and 'akhir' in locals():
            show_image_turun(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)
