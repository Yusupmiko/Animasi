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
        'IDPEL': lalulalu.get('IDPEL', pd.Series(dtype='int64')),
        'PEMKWH': lalulalu.get('PEMKWH', pd.Series(dtype='float64')),
        'TARIF': lalulalu.get('TARIF', pd.Series(dtype='object')),
        'DAYA': lalulalu.get('DAYA', pd.Series(dtype='float64')),
        'DLPD': lalulalu.get('DLPD', pd.Series(dtype='float64')),
        'LWBP_LALULALU': lalulalu.get('SLALWBP', pd.Series(dtype='float64')),
        'LWBP_CABUT': lalulalu.get('SAHLWBP_CABUT', pd.Series(dtype='float64')),
        'LWBP_PASANG': lalulalu.get('SLALWBP_PASANG', pd.Series(dtype='float64')),
        'LWBP_AKHIR': lalulalu.get('SAHLWBP', pd.Series(dtype='float64')),
        'WBP_LALULALU': lalulalu.get('SLAWBP', pd.Series(dtype='float64')),
        'WBP_CABUT': lalulalu.get('SAHWBP_CABUT', pd.Series(dtype='float64')),
        'WBP_PASANG': lalulalu.get('SLAWBP_PASANG', pd.Series(dtype='float64')),
        'WBP_AKHIR': lalulalu.get('SAHWBP', pd.Series(dtype='float64')),
        'JAM_NYALA': lalulalu.get('JAMNYALA', pd.Series(dtype='float64')),
        'FAKM': lalulalu.get('FAKM', pd.Series(dtype='float64')),
        'PEMKWH_REAL': (((lalulalu.get('SAHLWBP', 0) - lalulalu.get('SLALWBP_PASANG', 0))
                        + (lalulalu.get('SAHLWBP_CABUT', 0) - lalulalu.get('SLALWBP', 0)))
                        + ((lalulalu.get('SAHWBP', 0) - lalulalu.get('SLAWBP_PASANG', 0))
                        + (lalulalu.get('SAHWBP_CABUT', 0) - lalulalu.get('SLAWBP', 0))))
    })

    # Membuat DataFrame untuk periode lalu
    juruslalu = pd.DataFrame({
        'IDPEL': lalu.get('IDPEL', pd.Series(dtype='int64')),
        'PEMKWH': lalu.get('PEMKWH', pd.Series(dtype='float64')),
        'TARIF': lalu.get('TARIF', pd.Series(dtype='object')),
        'DAYA': lalu.get('DAYA', pd.Series(dtype='float64')),
        'DLPD': lalu.get('DLPD', pd.Series(dtype='float64')),
        'LWBP_LALULALU': lalu.get('SLALWBP', pd.Series(dtype='float64')),
        'LWBP_CABUT': lalu.get('SAHLWBP_CABUT', pd.Series(dtype='float64')),
        'LWBP_PASANG': lalu.get('SLALWBP_PASANG', pd.Series(dtype='float64')),
        'LWBP_AKHIR': lalu.get('SAHLWBP', pd.Series(dtype='float64')),
        'WBP_LALULALU': lalu.get('SLAWBP', pd.Series(dtype='float64')),
        'WBP_CABUT': lalu.get('SAHWBP_CABUT', pd.Series(dtype='float64')),
        'WBP_PASANG': lalu.get('SLAWBP_PASANG', pd.Series(dtype='float64')),
        'WBP_AKHIR': lalu.get('SAHWBP', pd.Series(dtype='float64')),
        'JAM_NYALA': lalu.get('JAMNYALA', pd.Series(dtype='float64')),
        'FAKM': lalu.get('FAKM', pd.Series(dtype='float64')),
        'PEMKWH_REAL': (((lalu.get('SAHLWBP', 0) - lalu.get('SLALWBP_PASANG', 0))
                        + (lalu.get('SAHLWBP_CABUT', 0) - lalu.get('SLALWBP', 0)))
                        + ((lalu.get('SAHWBP', 0) - lalu.get('SLAWBP_PASANG', 0))
                        + (lalu.get('SAHWBP_CABUT', 0) - lalu.get('SLAWBP', 0))))
    })

    # Membuat DataFrame untuk periode akhir
    jurusakhir = pd.DataFrame({
        'IDPEL': akhir.get('IDPEL', pd.Series(dtype='int64')),
        'NAMA': akhir.get('NAMA', pd.Series(dtype='object')),
        'PEMKWH': akhir.get('PEMKWH', pd.Series(dtype='float64')),
        'TARIF': akhir.get('TARIF', pd.Series(dtype='object')),
        'DAYA': akhir.get('DAYA', pd.Series(dtype='float64')),
        'DLPD': akhir.get('DLPD', pd.Series(dtype='float64')),
        'LWBP_LALULALU': akhir.get('SLALWBP', pd.Series(dtype='float64')),
        'LWBP_CABUT': akhir.get('SAHLWBP_CABUT', pd.Series(dtype='float64')),
        'LWBP_PASANG': akhir.get('SLALWBP_PASANG', pd.Series(dtype='float64')),
        'LWBP_AKHIR': akhir.get('SAHLWBP', pd.Series(dtype='float64')),
        'WBP_LALULALU': akhir.get('SLAWBP', pd.Series(dtype='float64')),
        'WBP_CABUT': akhir.get('SAHWBP_CABUT', pd.Series(dtype='float64')),
        'WBP_PASANG': akhir.get('SLAWBP_PASANG', pd.Series(dtype='float64')),
        'WBP_AKHIR': akhir.get('SAHWBP', pd.Series(dtype='float64')),
        'JAM_NYALA': akhir.get('JAMNYALA', pd.Series(dtype='float64')),
        'FAKM': akhir.get('FAKM', pd.Series(dtype='float64')),
        'PEMKWH_REAL': (((akhir.get('SAHLWBP', 0) - akhir.get('SLALWBP_PASANG', 0))
                        + (akhir.get('SAHLWBP_CABUT', 0) - akhir.get('SLALWBP', 0)))
                        + ((akhir.get('SAHWBP', 0) - akhir.get('SLAWBP_PASANG', 0))
                        + (akhir.get('SAHWBP_CABUT', 0) - akhir.get('SLAWBP', 0))))
    })

    # Menggabungkan DataFrames
    kroscek_temp_1 = pd.merge(juruslalulalu, juruslalu, on='IDPEL', how='right')
    kroscek_temp = pd.merge(kroscek_temp_1, jurusakhir, on='IDPEL', how='right')

    # Definisi path untuk foto
    path_foto1 = 'https://portalapp.iconpln.co.id/acmt/DisplayBlobServlet1?idpel='
    path_foto2 = '&blth='

    # Membuat DataFrame akhir sesuai format yang diinginkan
    kroscek = pd.DataFrame({
        'BLTH': blth_kini,
        'IDPEL': kroscek_temp['IDPEL'].astype(str),
        'NAMA': kroscek_temp['NAMA'],
        'TARIF': kroscek_temp['TARIF'],
        'DAYA': kroscek_temp['DAYA'],
        'SLALWBP': kroscek_temp['LWBP_LALULALU_y'],
        'LWBPCABUT': kroscek_temp['LWBP_CABUT_y'],
        'SELISIH STAN BONGKAR': kroscek_temp['LWBP_AKHIR_y'] - kroscek_temp['LWBP_LALULALU_y'],
        'LWBP PASANG': kroscek_temp['LWBP_PASANG_y'],
        'SAHLWBP': kroscek_temp['LWBP_AKHIR_y'],
        'KWH 10': kroscek_temp['PEMKWH_REAL_y'],
        'KWH 09': kroscek_temp['PEMKWH_REAL_x'],
        'KWH 08': kroscek_temp['PEMKWH_REAL_x'],
        'DELTA PEMKWH': kroscek_temp['PEMKWH_REAL_y'] - kroscek_temp['PEMKWH_REAL_x'],
        '%': np.where(kroscek_temp['PEMKWH_REAL_x'] == 0, '#DIV/0!', 
                      (kroscek_temp['PEMKWH_REAL_y'] - kroscek_temp['PEMKWH_REAL_x']) 
                      / kroscek_temp['PEMKWH_REAL_x'] * 100),
        'KET': np.where(kroscek_temp['PEMKWH_REAL_y'] == 0, 'SESUAI', 'TIDAK SESUAI'),
        'DLPD': kroscek_temp['DLPD_y'],
        'STAN 09': kroscek_temp['LWBP_AKHIR_x'],
        'STAN 08': kroscek_temp['LWBP_AKHIR_x'],
        'STAN 07': kroscek_temp['LWBP_LALULALU_x'],
        'LINK_FOTO_LALULALU': path_foto1 + kroscek_temp['IDPEL'].astype(str) + path_foto2 + blth_lalulalu,
        'LINK_FOTO_LALU': path_foto1 + kroscek_temp['IDPEL'].astype(str) + path_foto2 + blth_lalu,
        'LINK_FOTO_AKHIR': path_foto1 + kroscek_temp['IDPEL'].astype(str) + path_foto2 + blth_kini
    })

    # Convert the 'FOTO_LALU' and 'FOTO_AKHIR' columns into clickable HTML links (e.g., for display in a notebook)
    kroscek['LINK_FOTO_LALULALU'] = kroscek['LINK_FOTO_LALULALU'].apply(lambda x: f'<a href="{x}" target="_blank">View Image</a>')
    kroscek['LINK_FOTO_LALU'] = kroscek['LINK_FOTO_LALU'].apply(lambda x: f'<a href="{x}" target="_blank">View Image</a>')
    kroscek['LINK_FOTO_AKHIR'] = kroscek['LINK_FOTO_AKHIR'].apply(lambda x: f'<a href="{x}" target="_blank">View Image</a>')
    
    return kroscek

# Function to filter and display images
def amrFilter(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini):
    kroscek = copyDataframe(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)
    criteria1 = ['L STAND MUNDUR', 'N KWH N O R M A L', 'K KWH NOL', 'C KWH < 40 JAM', 'J REKENING PECAHAN']

    amr_df = kroscek[kroscek['DLPD_KINI'].isin(criteria1)]
    amr_df = amr_df[amr_df['SELISIH 50%'].isin(["Selisih Besar"])]
    del amr_df['FOTO_LALU']
    del amr_df['FOTO_AKHIR']
    return amr_df

def maksFilter(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini):
    kroscek = copyDataframe(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)
    maks_df = kroscek[kroscek['DLPD_KINI'].isin(['L STAND METER MUNDUR'])]
    return maks_df

def norm1Filter(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini):
    kroscek = copyDataframe(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)

    norm1_df = kroscek[kroscek['DLPD_KINI'].isin(['N KWH N O R M A L'])]
    norm1_df = norm1_df[norm1_df['SELISIH 50%'].isin(["Selisih Besar"])]
    norm1_df = norm1_df[norm1_df['SUBS_NONSUBS'].isin(["Subs"])]
    return norm1_df

def norm2Filter(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini):
    kroscek = copyDataframe(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)

    norm2_df = kroscek[kroscek['DLPD_KINI'].isin(['N KWH N O R M A L'])]
    norm2_df = norm2_df[norm2_df['SELISIH 50%'].isin(["Selisih Besar"])]
    norm2_df = norm2_df[norm2_df['SUBS_NONSUBS'].isin(["Nonsubs"])]
    return norm2_df

def minNolFilter(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini):
    kroscek = copyDataframe(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)

    minNol_df = kroscek[kroscek['DLPD_KINI'].isin(['K KWH NOL'])]
    minNol_df = minNol_df[minNol_df['MIN_NOL'].isin(['No'])]
    return minNol_df

def show_image_maks(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini):
    df = copyDataframe(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)
    if df.empty:
        st.warning("No data available after applying the filter.")
        return

    # Display the DataFrame with clickable links using st.markdown
    st.markdown(df.to_html(escape=False), unsafe_allow_html=True)

# Fungsi filter lain
def show_image_norm1(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini):
    df = copyDataframe(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)
    if df.empty:
        st.warning("No data available after applying the filter.")
        return

    # Display the DataFrame with clickable links using st.markdown
    st.markdown(df.to_html(escape=False), unsafe_allow_html=True)

def show_image_norm2(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini):
    df = copyDataframe(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)
    if df.empty:
        st.warning("No data available after applying the filter.")
        return

    # Display the DataFrame with clickable links using st.markdown
    st.markdown(df.to_html(escape=False), unsafe_allow_html=True)

def show_image_minnol(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini):
    df = copyDataframe(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)
    if df.empty:
        st.warning("No data available after applying the filter.")
        return

    # Display the DataFrame with clickable links using st.markdown
    st.markdown(df.to_html(escape=False), unsafe_allow_html=True)

def amrFilter(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini):
    df = copyDataframe(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)
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
    tabs = st.tabs(['SEMUA', 'KWH MAKS', 'NORMAL', 'NORMAL > 900', '0-40 JN', 'AMR'])

    # Tab SEMUA
    with tabs[0]:
        st.write("Semua")
        if 'lalulalu' in locals() and 'lalu' in locals() and 'akhir' in locals():
            st.dataframe(copyDataframe(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini))

    # Tab KWH MAKS
    with tabs[1]:
        st.write("KWH Maks > 720 JN")
        if 'lalulalu' in locals() and 'lalu' in locals() and 'akhir' in locals():
            show_image_maks(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)

    # Tab NORMAL 450-900 VA
    with tabs[2]:
        st.write("Normal Daya 450-900 VA")
        if 'lalulalu' in locals() and 'lalu' in locals() and 'akhir' in locals():
            show_image_norm1(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)

    # Tab NORMAL > 900 VA
    with tabs[3]:
        st.write("Normal Daya > 900")
        if 'lalulalu' in locals() and 'lalu' in locals() and 'akhir' in locals():
            show_image_norm2(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)

    # Tab 0-40 JN
    with tabs[4]:
        st.write("KWH Nol 40 JN")
        if 'lalulalu' in locals() and 'lalu' in locals() and 'akhir' in locals():
            show_image_minnol(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)
    # Tab AMR
    with tabs[5]:
        st.write("Hasil AMR")
        if 'lalulalu' in locals() and 'lalu' in locals() and 'akhir' in locals():
            st.dataframe(amrFilter(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini))
 # Tab SGR
    with tabs[6]:
        st.write("Hasil AMR")
        if 'lalulalu' in locals() and 'lalu' in locals() and 'akhir' in locals():
            st.dataframe(amrFilter(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini))