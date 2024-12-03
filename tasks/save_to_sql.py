import sqlite3

def save_to_sql(database_name, table_name, url, text_cleaned, summary):
    try:
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        
        # Membuat tabel jika belum ada
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT,
            text_cleaned TEXT,
            summary TEXT
        )
        """)
        
        # Menyisipkan data ke tabel
        cursor.execute(f"""
        INSERT INTO {table_name} (url, text_cleaned, summary)
        VALUES (?, ?, ?)
        """, (url, text_cleaned, summary))
        
        conn.commit()
        conn.close()
        print("Data berhasil disimpan ke database.")
    except Exception as e:
        print(f"Error: Terjadi kesalahan saat menyimpan data ke database - {e}")