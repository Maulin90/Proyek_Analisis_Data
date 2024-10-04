import pandas as pd

# Membaca Dataset
day_df = pd.read_csv("data/day.csv")  # Gantilah dengan jalur yang sesuai
hour_df = pd.read_csv("data/hour.csv")  # Gantilah dengan jalur yang sesuai

# Menggabungkan DataFrame day_df dan hour_df
all_df = pd.concat([day_df, hour_df], ignore_index=True)

# Menyimpan DataFrame gabungan ke dalam file CSV
all_df.to_csv("data/all_data.csv", index=False)

print("Data berhasil digabungkan dan disimpan sebagai all_data.csv")
