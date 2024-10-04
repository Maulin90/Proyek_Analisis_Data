import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Judul
st.title("Dashboard Analisis Data Bike Sharing")

# Load Dataset
day_df = pd.read_csv(r"C:\Users\nenda\Downloads\data\day.csv")  
hour_df = pd.read_csv(r"C:\Users\nenda\Downloads\data\hour.csv")  

# Sidebar - Pilihan Analisis
st.sidebar.title("Pilih Analisis")
analysis_type = st.sidebar.selectbox("Pilih Tipe Analisis", ["Hari Kerja vs Akhir Pekan", "Cuaca dan Musim"])

# Analisis 1: Apakah ada perbedaan jumlah penyewaan sepeda antara hari kerja dan akhir pekan?
if analysis_type == "Hari Kerja vs Akhir Pekan":
    st.header("Jumlah Penyewaan Sepeda: Hari Kerja vs Akhir Pekan")

    # Klasifikasi hari kerja dan akhir pekan
    day_df['day_type'] = day_df['workingday'].apply(lambda x: 'Hari Kerja' if x == 1 else 'Akhir Pekan')

    # Hitung total penyewaan
    summary = day_df.groupby('day_type')['cnt'].sum().reset_index()

    # Visualisasi Bar Plot
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x='day_type', y='cnt', data=summary, palette='pastel', ax=ax)
    ax.set_title('Jumlah Penyewaan Sepeda: Hari Kerja vs Akhir Pekan')
    ax.set_xlabel('Tipe Hari')
    ax.set_ylabel('Jumlah Penyewaan')
    st.pyplot(fig)

    # Uji statistik (t-test)
    hari_kerja = day_df[day_df['day_type'] == 'Hari Kerja']['cnt']
    akhir_pekan = day_df[day_df['day_type'] == 'Akhir Pekan']['cnt']
    t_stat, p_value = stats.ttest_ind(hari_kerja, akhir_pekan)

    # Tampilkan hasil uji t
    st.subheader("Hasil Uji Statistik (T-Test)")
    st.write(f"Statistik t: {t_stat:.4f}")
    st.write(f"Nilai p: {p_value:.4f}")

    # Tentukan hasil berdasarkan nilai p
    alpha = 0.05
    if p_value < alpha:
        st.write("Terdapat perbedaan signifikan antara jumlah penyewaan sepeda di hari kerja dan akhir pekan.")
    else:
        st.write("Tidak terdapat perbedaan signifikan antara jumlah penyewaan sepeda di hari kerja dan akhir pekan.")

# Analisis 2: Bagaimana faktor cuaca dan musim mempengaruhi jumlah penyewaan sepeda?
elif analysis_type == "Cuaca dan Musim":
    st.header("Pengaruh Cuaca dan Musim Terhadap Penyewaan Sepeda")

    # Mengklasifikasikan musim
    seasons = {1: 'Musim Dingin', 2: 'Musim Semi', 3: 'Musim Panas', 4: 'Musim Gugur'}
    day_df['season_name'] = day_df['season'].map(seasons)

    # Mengklasifikasikan cuaca
    weather_conditions = {1: 'Cerah', 2: 'Sedikit Berawan', 3: 'Berawan', 4: 'Hujan'}
    day_df['weather_name'] = day_df['weathersit'].map(weather_conditions)

    # Menghitung jumlah penyewaan berdasarkan musim
    season_summary = day_df.groupby('season_name')['cnt'].sum().reset_index()

    # Menghitung jumlah penyewaan berdasarkan kondisi cuaca
    weather_summary = day_df.groupby('weather_name')['cnt'].sum().reset_index()

    # Visualisasi Jumlah Penyewaan Berdasarkan Musim
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x='season_name', y='cnt', data=season_summary, palette='pastel', ax=ax)
    ax.set_title('Jumlah Penyewaan Sepeda Berdasarkan Musim')
    ax.set_xlabel('Musim')
    ax.set_ylabel('Jumlah Penyewaan')
    st.pyplot(fig)

    # Visualisasi Jumlah Penyewaan Berdasarkan Kondisi Cuaca
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x='weather_name', y='cnt', data=weather_summary, palette='pastel', ax=ax)
    ax.set_title('Jumlah Penyewaan Sepeda Berdasarkan Kondisi Cuaca')
    ax.set_xlabel('Kondisi Cuaca')
    ax.set_ylabel('Jumlah Penyewaan')
    st.pyplot(fig)

    # Tambahkan insight
    st.subheader("Insight Analisis")
    st.write("Musim dan kondisi cuaca berpengaruh signifikan terhadap jumlah penyewaan sepeda.")
    st.write("Jumlah penyewaan tertinggi terjadi selama musim panas dan ketika cuaca cerah,")
    st.write("sementara musim dingin dan cuaca berawan cenderung menurunkan aktivitas bersepeda.")
