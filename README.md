# Marathon Photo Finder

## 📜 Deskripsi Proyek
**Marathon Photo Finder** adalah aplikasi berbasis web yang memungkinkan peserta lari maraton menemukan foto mereka dengan mudah berdasarkan nomor dada. Sistem ini menggunakan **Google Drive API** untuk mengambil foto dari Google Drive dan **Google Vision API** untuk mendeteksi nomor dada yang ada dalam gambar.

---

## 📁 Struktur Folder
```
marathon-photo-finder/
│── backend/
│   │── app.py                # Backend Flask utama
│   │── database.py           # Inisialisasi database SQLite
│   │── drive_api.py          # Google Drive API untuk mengambil gambar
│   │── vision_api.py         # Google Vision API untuk membaca nomor dada
│   └── static/
│       └── images/           # Folder penyimpanan gambar sementara
│── frontend/
│   │── index.html            # UI utama
│   │── script.js             # JavaScript untuk interaksi dengan backend
│   │── styles.css            # Styling halaman
│── database.db               # Database SQLite (otomatis dibuat)
│── README.md                 # Dokumentasi proyek
```

---

## 🛠 Teknologi yang Digunakan
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite
- **AI & API:**
  - **Google Drive API** → Mengambil gambar dari Google Drive
  - **Google Vision API** → Mendeteksi nomor dada dalam gambar

---

## 🚀 Cara Menjalankan Proyek

### 1️⃣ Persiapan
- **Aktifkan API Google Drive & Google Vision API** di [Google Cloud Console](https://console.cloud.google.com/)
- **Buat dan unduh file `credentials.json`** untuk OAuth 2.0
- **Pastikan Python 3 terinstal**

### 2️⃣ Instalasi Dependensi
Jalankan perintah berikut di terminal:
```bash
pip install flask google-auth google-auth-oauthlib google-auth-httplib2 googleapiclient opencv-python sqlite3
```

### 3️⃣ Inisialisasi Database
```bash
cd backend
python database.py
```

### 4️⃣ Jalankan Backend
```bash
python app.py
```

### 5️⃣ Jalankan Frontend
Buka `frontend/index.html` langsung di browser atau jalankan:
```bash
cd frontend
python -m http.server 8000
```
Akses di **http://localhost:8000**

---

## 🔍 Fitur Aplikasi
1. **Input Nomor Dada** → Pengguna memasukkan nomor dada.
2. **Analisis Gambar** → AI memindai semua foto dan mendeteksi nomor dada.
3. **Pencocokan Nomor** → Menampilkan foto yang cocok dengan nomor dada yang diinput.
4. **Galeri Foto** → Menampilkan hasil pencarian dalam bentuk galeri.

---

## 💡 Catatan
- Pastikan API Key dari Google sudah benar.
- Jika database kosong, jalankan `database.py` untuk inisialisasi.
- Untuk akses gambar di Google Drive, folder harus diatur ke **“Anyone with the link”** agar bisa dibaca oleh aplikasi.

---
