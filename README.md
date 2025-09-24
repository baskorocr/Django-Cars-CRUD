# Car Management System

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

Sistem manajemen mobil berbasis web yang dibangun dengan Django. Aplikasi ini menyediakan operasi CRUD (Create, Read, Update, Delete) untuk data mobil dengan sistem autentikasi yang aman dan antarmuka yang responsif.

## ✨ Fitur

- **CRUD Operations**: Tambah, lihat, edit, dan hapus data mobil
- **Sistem Autentikasi**: Login/logout dengan validasi keamanan
- **Admin-Only Registration**: Hanya admin yang dapat membuat akun baru
- **User Management**: Manajemen pengguna melalui Django Admin
- **Responsive UI**: Antarmuka yang responsif dengan Bootstrap 5
- **Search & Filter**: Pencarian dan filter data mobil
- **Secure Access**: Proteksi halaman dengan decorator autentikasi

## 🛠️ Tech Stack

- **Backend**: Django 4.x
- **Database**: SQLite (default)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Icons**: Font Awesome
- **Authentication**: Django Built-in Auth System

## 📋 Prerequisites

Pastikan Anda telah menginstal:
- Python 3.8 atau lebih baru
- pip (Python package installer)
- Git (opsional, untuk clone repository)

## 🚀 Instalasi

### 1. Clone atau Download Project
```bash
# Clone repository (jika menggunakan Git)
git clone <repository-url>
cd django

# Atau download dan extract file project
```

### 2. Buat Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install django
# Atau jika ada requirements.txt:
# pip install -r requirements.txt
```

### 4. Database Migration
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Buat Superuser (Admin)
```bash
python manage.py createsuperuser
```
Ikuti instruksi untuk membuat username, email, dan password admin.

### 6. Jalankan Server
```bash
python manage.py runserver
```

Aplikasi akan berjalan di: `http://127.0.0.1:8000/`

## 📖 Cara Penggunaan

### Akses Aplikasi
1. Buka browser dan kunjungi `http://127.0.0.1:8000/`
2. Anda akan diarahkan ke halaman login

### Login & Register
- **Login**: Gunakan akun yang sudah dibuat atau akun superuser
- **Register**: Hanya admin yang dapat mengakses halaman registrasi
- **Logout**: Klik tombol "Logout" di navbar

### Operasi CRUD Mobil
1. **Lihat Daftar Mobil**: Halaman utama menampilkan semua mobil
2. **Tambah Mobil**: Klik "Tambah Mobil" di navbar
3. **Detail Mobil**: Klik "Detail" pada mobil yang diinginkan
4. **Edit Mobil**: Klik "Edit" pada mobil yang ingin diubah
5. **Hapus Mobil**: Klik "Hapus" pada mobil yang ingin dihapus

### Admin Panel
- Akses: `http://127.0.0.1:8000/admin/`
- Login dengan akun superuser
- Kelola data mobil dan pengguna

## 📁 Struktur Project

```
django/
├── car_management/          # Project settings
│   ├── __init__.py
│   ├── settings.py          # Konfigurasi Django
│   ├── urls.py             # URL routing utama
│   └── wsgi.py
├── cars/                   # App untuk manajemen mobil
│   ├── migrations/         # Database migrations
│   ├── templates/cars/     # Template HTML
│   ├── admin.py           # Konfigurasi Django Admin
│   ├── apps.py            # Konfigurasi aplikasi
│   ├── models.py          # Model database
│   ├── urls.py            # URL routing cars
│   └── views.py           # Logic aplikasi
├── accounts/              # App untuk autentikasi
│   ├── templates/accounts/ # Template login/register
│   ├── urls.py            # URL routing accounts
│   └── views.py           # Logic autentikasi
├── templates/             # Template global
│   └── base.html          # Template dasar
├── static/               # File statis (CSS, JS, images)
├── db.sqlite3           # Database SQLite
└── manage.py            # Django management script
```

## 🔧 Konfigurasi

### Model Mobil
Model `Car` memiliki field:
- `brand`: Merek mobil
- `model`: Model mobil
- `year`: Tahun produksi
- `price`: Harga (DecimalField)
- `description`: Deskripsi
- `created_at`: Tanggal dibuat
- `updated_at`: Tanggal diupdate

### Sistem Keamanan
- Halaman CRUD dilindungi dengan `@login_required`
- Registrasi hanya untuk admin (`@user_passes_test`)
- User yang sudah login tidak dapat akses halaman login

## 🌐 URL Testing

- **Homepage**: `http://127.0.0.1:8000/`
- **Login**: `http://127.0.0.1:8000/accounts/login/`
- **Register**: `http://127.0.0.1:8000/accounts/register/` (admin only)
- **Admin Panel**: `http://127.0.0.1:8000/admin/`
- **Tambah Mobil**: `http://127.0.0.1:8000/cars/add/`

## 🐛 Troubleshooting

### Error Umum
1. **ModuleNotFoundError**: Pastikan virtual environment aktif dan dependencies terinstal
2. **Database Error**: Jalankan `python manage.py migrate`
3. **Static Files**: Jalankan `python manage.py collectstatic` jika diperlukan
4. **Permission Denied**: Pastikan user memiliki akses yang sesuai

### Reset Database
```bash
# Hapus database dan migrations
rm db.sqlite3
rm cars/migrations/0*.py
rm accounts/migrations/0*.py

# Buat ulang migrations dan database
python manage.py makemigrations cars
python manage.py makemigrations accounts
python manage.py migrate
python manage.py createsuperuser
```

## 🤝 Contributing

1. Fork repository ini
2. Buat branch fitur (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📝 License

Project ini menggunakan MIT License. Lihat file `LICENSE` untuk detail lebih lanjut.

## 👨‍💻 Developer

Dikembangkan dengan ❤️ menggunakan Django Framework.

---

**Happy Coding! 🚗💨**