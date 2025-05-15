def cari_produk(kata_kunci, database):
    return [p for p in database if kata_kunci.lower() in p['nama'].lower()]

def tambah_produk(db, produk):
    db.append(produk)
    return db

def edit_produk(db, id_produk, nama=None, harga=None):
    for p in db:
        if p['id'] == id_produk:
            if nama: p['nama'] = nama
            if harga: p['harga'] = harga
            return p
    return None

def hapus_produk(db, id_produk):
    return [p for p in db if p['id'] != id_produk]

def baca_produk(db, id_produk):
    for p in db:
        if p['id'] == id_produk:
            return p
    return None
