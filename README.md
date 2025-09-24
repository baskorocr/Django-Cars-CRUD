# Car Management System

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

Sistem manajemen mobil berbasis web yang dibangun dengan Django. Aplikasi ini menyediakan operasi CRUD (Create, Read, Update, Delete) untuk data mobil dengan sistem autentikasi yang aman dan antarmuka yang responsif.

## ✨ Fitur

- **CRUD Operations**: Tambah, lihat, edit, dan hapus data mobil
- **Sistem Autentikasi**: Login/logout dengan validasi keamanan
- **Permission System**: Sistem izin berbasis role untuk kontrol akses granular
- **Admin-Only Registration**: Hanya admin yang dapat membuat akun baru
- **User Management**: Manajemen pengguna melalui Django Admin
- **Responsive UI**: Antarmuka yang responsif dengan Bootstrap 5
- **Search & Filter**: Pencarian dan filter data mobil
- **Secure Access**: Proteksi halaman dengan decorator autentikasi dan permission

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
- **Permission System**: Kontrol akses berbasis izin untuk setiap operasi

## 🔐 Permission System

Sistem ini menggunakan Django's built-in permission system dengan custom permissions untuk kontrol akses yang lebih granular.

### Custom Permissions
Model `Car` memiliki custom permissions:
- `can_view_all_cars`: Dapat melihat semua mobil
- `can_add_car`: Dapat menambah mobil baru
- `can_change_car`: Dapat mengubah data mobil
- `can_delete_car`: Dapat menghapus mobil

### Setup Permission System

#### 1. Buat dan Apply Migration
```bash
# Buat migration untuk custom permissions
python manage.py makemigrations cars

# Apply migration ke database
python manage.py migrate
```

#### 2. Buat Superuser (jika belum ada)
```bash
python manage.py createsuperuser
```

#### 3. Akses Django Admin
1. Jalankan server: `python manage.py runserver`
2. Buka browser: `http://127.0.0.1:8000/admin/`
3. Login dengan akun superuser

### Permission Management

#### Assign Permissions ke User
1. Di Django Admin, pilih **Users**
2. Pilih user yang ingin diatur
3. Scroll ke bagian **User permissions**
4. Pilih permissions yang diinginkan:
   - `cars | car | Can view all cars`
   - `cars | car | Can add car`
   - `cars | car | Can change car`
   - `cars | car | Can delete car`
5. Klik **Save**

#### Membuat dan Manage Groups
1. Di Django Admin, pilih **Groups**
2. Klik **Add group**
3. Beri nama group (contoh: "Car Managers", "Viewers Only")
4. Pilih permissions untuk group
5. Assign users ke group di halaman user

#### Contoh Role-Based Setup

**Role: Car Manager (Full Access)**
```bash
# Permissions yang diperlukan:
- can_view_all_cars
- can_add_car
- can_change_car
- can_delete_car
```

**Role: Car Viewer (Read Only)**
```bash
# Permissions yang diperlukan:
- can_view_all_cars
```

**Role: Car Editor (No Delete)**
```bash
# Permissions yang diperlukan:
- can_view_all_cars
- can_add_car
- can_change_car
```

### Testing Permission System

#### Skenario Testing
1. **Test User tanpa Permission**:
   - Login dengan user baru
   - Coba akses `/cars/` → Akan redirect ke login
   - UI tidak menampilkan tombol/link yang tidak diizinkan

2. **Test User dengan Permission Terbatas**:
   - Buat user dengan hanya `can_view_all_cars`
   - Login dan cek bahwa tombol "Tambah", "Edit", "Hapus" tidak muncul
   - Coba akses langsung URL `/cars/add/` → Akan redirect ke login

3. **Test User dengan Full Permission**:
   - Assign semua permissions ke user
   - Pastikan semua fitur dapat diakses

#### Command untuk Testing
```bash
# Buat test user via Django shell
python manage.py shell

# Di shell Python:
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from cars.models import Car

# Buat user test
user = User.objects.create_user('testuser', 'test@example.com', 'password123')

# Ambil permission
content_type = ContentType.objects.get_for_model(Car)
view_permission = Permission.objects.get(codename='view_car', content_type=content_type)

# Assign permission
user.user_permissions.add(view_permission)
```

### UI Permission Checks

Template menggunakan `perms` context processor untuk menyembunyikan elemen UI:

```html
<!-- Contoh di template -->
{% if perms.cars.add_car %}
    <a href="{% url 'car_create' %}" class="btn btn-success">
        Tambah Mobil
    </a>
{% endif %}

{% if perms.cars.change_car %}
    <a href="{% url 'car_update' car.pk %}" class="btn btn-warning">
        Edit
    </a>
{% endif %}
```

### Troubleshooting Permission

#### Masalah Umum
1. **User tidak bisa akses meskipun punya permission**:
   - Pastikan migration sudah dijalankan
   - Cek apakah permission benar-benar ter-assign
   - Logout dan login ulang

2. **Permission tidak muncul di Admin**:
   ```bash
   # Jalankan ulang migration
   python manage.py migrate --run-syncdb
   ```

3. **Template tidak menyembunyikan elemen**:
   - Pastikan menggunakan `{% if perms.cars.permission_name %}`
   - Cek apakah context processor aktif di settings

#### Debug Permission
```bash
# Cek permission user via shell
python manage.py shell

# Di shell:
from django.contrib.auth.models import User
user = User.objects.get(username='username')
print(user.get_all_permissions())
print(user.has_perm('cars.add_car'))
```

#### Reset Permissions
```bash
# Hapus semua permissions dan buat ulang
python manage.py shell

# Di shell:
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from cars.models import Car

# Hapus custom permissions
content_type = ContentType.objects.get_for_model(Car)
Permission.objects.filter(content_type=content_type).delete()

# Keluar shell dan jalankan migration ulang
# python manage.py migrate
```

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