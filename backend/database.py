import sqlite3

DB_NAME = "database.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS images (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_name TEXT,
            bib_number TEXT,
            image_url TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_image_data(image_name, bib_number, image_url):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO images (image_name, bib_number, image_url) VALUES (?, ?, ?)",
                   (image_name, bib_number, image_url))
    conn.commit()
    conn.close()

def search_images_by_number(bib_number):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT image_url FROM images WHERE bib_number=?", (bib_number,))
    results = cursor.fetchall()
    conn.close()
    return [r[0] for r in results]

if __name__ == "__main__":
    init_db()
