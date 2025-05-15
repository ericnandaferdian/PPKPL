# KlikIndomaret Full Project - Clean Architecture

## Struktur
- `entity/`: struktur data user dan produk
- `usecase/`: semua logika bisnis (auth, produk, checkout, error)
- `interface/`: controller layer (pemanggilan)
- `test/`: semua unittest (min 3 per fungsi)
- `main.py`: contoh pemanggilan program

## Cara Menjalankan
1. `python main.py` → coba pemanggilan login & tambah produk
2. `python -m unittest discover -s test` → jalankan semua unit test
