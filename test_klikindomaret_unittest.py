import unittest

# ==================== SIMULASI FUNGSIONAL ====================

def login(username, password):
    if username == "082358747380" and password == "@Rumahsaya85":
        return "home"
    return "login_failed"

def logout(session_active):
    if session_active:
        return {"status": "logged_out", "redirect": "home"}
    return {"status": "already_logged_out"}

def tambah_alamat(label, alamat_lengkap, nama, no_hp):
    if all([label, alamat_lengkap, nama, no_hp]):
        return "alamat_disimpan"
    return "gagal"

def cari_produk(kata_kunci):
    produk_database = ["beras", "gula", "minyak", "susu"]
    return [p for p in produk_database if kata_kunci.lower() in p]

def filter_produk(produk_list, kategori=None, brand=None):
    return [
        p for p in produk_list
        if (kategori in p["kategori"]) and (p["brand"] == brand)
    ]

def tambah_ke_keranjang(keranjang, produk, jumlah):
    if jumlah <= 0:
        return keranjang
    if produk in keranjang:
        keranjang[produk] += jumlah
    else:
        keranjang[produk] = jumlah
    return keranjang

def update_kuantitas(keranjang, produk, tambahan_kuantitas):
    if produk not in keranjang or tambahan_kuantitas <= 0:
        return keranjang
    keranjang[produk]["jumlah"] += tambahan_kuantitas
    keranjang[produk]["total_harga"] = keranjang[produk]["jumlah"] * keranjang[produk]["harga"]
    return keranjang

def hapus_dari_keranjang(keranjang, produk):
    if produk in keranjang:
        del keranjang[produk]
        return f"{produk} dihapus"
    return "Produk tidak ditemukan"

def checkout(keranjang, alamat_aktif):
    if not keranjang or not alamat_aktif:
        return "checkout_gagal"
    return "menu_pembayaran"

def pembayaran(metode):
    if metode == "BRI Virtual Account":
        return {
            "status": "menunggu_pembayaran",
            "va_number": "1234567890",
            "batas_waktu": "24 jam"
        }
    return {"status": "metode_tidak_dikenal"}

def akses_url(url):
    halaman_tersedia = [
        "/home", "/produk", "/keranjang", "/checkout"
    ]
    if any(url.endswith(path) for path in halaman_tersedia):
        return {"status": 200, "content": "halaman ditemukan"}
    return {
        "status": 404,
        "content": "Halaman tidak ditemukan. Mungkin URL salah. Kembali ke Klik Indomaret"
    }

# ==================== TEST CASES ====================

class TestLoginFunction(unittest.TestCase):
    def test_login_valid(self):
        self.assertEqual(login("082358747380", "@Rumahsaya85"), "home")
    def test_login_invalid_username(self):
        self.assertNotEqual(login("invalid", "@Rumahsaya85"), "home")
    def test_login_invalid_password(self):
        self.assertNotEqual(login("082358747380", "wrong"), "home")

class TestLogout(unittest.TestCase):
    def test_logout_berhasil(self):
        hasil = logout(True)
        self.assertEqual(hasil["status"], "logged_out")
        self.assertEqual(hasil["redirect"], "home")
    def test_logout_tanpa_sesi(self):
        self.assertEqual(logout(False)["status"], "already_logged_out")
    def test_logout_response_structure(self):
        hasil = logout(True)
        self.assertIn("status", hasil)
        self.assertIn("redirect", hasil)

class TestTambahAlamat(unittest.TestCase):
    def test_tambah_alamat_valid(self):
        self.assertEqual(tambah_alamat("Rumah", "Jalan 1 No. 32", "Eric", "082358747380"), "alamat_disimpan")
    def test_tambah_alamat_kosong(self):
        self.assertNotEqual(tambah_alamat("", "Jalan 1", "Eric", "082358747380"), "alamat_disimpan")
    def test_tambah_alamat_tanpa_hp(self):
        self.assertNotEqual(tambah_alamat("Rumah", "Jalan 1", "Eric", ""), "alamat_disimpan")

class TestPencarianProduk(unittest.TestCase):
    def test_pencarian_valid(self):
        self.assertIn("beras", cari_produk("beras"))
    def test_pencarian_kosong(self):
        self.assertEqual(len(cari_produk("rokok")), 0)
    def test_pencarian_case_insensitive(self):
        self.assertIn("beras", cari_produk("BeRaS"))

class TestFilterProduk(unittest.TestCase):
    def setUp(self):
        self.produk = [
            {"nama": "Beras Lahap Lele", "kategori": "Beras & Biji-bijian", "brand": "Lahap Lele"},
            {"nama": "Gula", "kategori": "Gula", "brand": "Gulavit"}
        ]
    def test_filter_kategori_dan_brand(self):
        hasil = filter_produk(self.produk, "Beras & Biji-bijian", "Lahap Lele")
        self.assertEqual(hasil[0]["brand"], "Lahap Lele")
    def test_filter_brand_tidak_ada(self):
        self.assertEqual(len(filter_produk(self.produk, "Beras & Biji-bijian", "XXX")), 0)
    def test_filter_kategori_saja(self):
        hasil = filter_produk(self.produk, "Beras & Biji-bijian", "Lahap Lele")
        self.assertEqual(hasil[0]["nama"], "Beras Lahap Lele")

class TestTambahKeKeranjang(unittest.TestCase):
    def setUp(self):
        self.keranjang = {}
    def test_tambah_produk_baru(self):
        hasil = tambah_ke_keranjang(self.keranjang, "Beras", 1)
        self.assertEqual(hasil["Beras"], 1)
    def test_tambah_produk_duplikat(self):
        self.keranjang = {"Beras": 2}
        hasil = tambah_ke_keranjang(self.keranjang, "Beras", 3)
        self.assertEqual(hasil["Beras"], 5)
    def test_tambah_produk_dengan_jumlah_0(self):
        hasil = tambah_ke_keranjang(self.keranjang, "Gula", 0)
        self.assertNotIn("Gula", hasil)

class TestUpdateKuantitasKeranjang(unittest.TestCase):
    def setUp(self):
        self.keranjang = {"Beras": {"jumlah": 1, "harga": 10000, "total_harga": 10000}}
    def test_tambah_kuantitas_berhasil(self):
        hasil = update_kuantitas(self.keranjang, "Beras", 1)
        self.assertEqual(hasil["Beras"]["jumlah"], 2)
        self.assertEqual(hasil["Beras"]["total_harga"], 20000)
    def test_update_produk_tidak_ada(self):
        hasil = update_kuantitas(self.keranjang, "Susu", 1)
        self.assertNotIn("Susu", hasil)
    def test_update_dengan_kuantitas_0(self):
        hasil = update_kuantitas(self.keranjang, "Beras", 0)
        self.assertEqual(hasil["Beras"]["jumlah"], 1)

class TestHapusProdukKeranjang(unittest.TestCase):
    def setUp(self):
        self.keranjang = {"Beras": 2, "Gula": 1}
    def test_hapus_produk_berhasil(self):
        hasil = hapus_dari_keranjang(self.keranjang, "Gula")
        self.assertEqual(hasil, "Gula dihapus")
    def test_hapus_produk_tidak_ada(self):
        hasil = hapus_dari_keranjang(self.keranjang, "Susu")
        self.assertEqual(hasil, "Produk tidak ditemukan")
    def test_hapus_produk_terakhir(self):
        self.keranjang = {"Minyak": 1}
        hasil = hapus_dari_keranjang(self.keranjang, "Minyak")
        self.assertEqual(self.keranjang, {})

class TestCheckout(unittest.TestCase):
    def test_checkout_berhasil(self):
        self.assertEqual(checkout({"Beras": 2}, "Jalan 1"), "menu_pembayaran")
    def test_checkout_tanpa_produk(self):
        self.assertEqual(checkout({}, "Jalan 1"), "checkout_gagal")
    def test_checkout_tanpa_alamat(self):
        self.assertEqual(checkout({"Beras": 2}, ""), "checkout_gagal")

class TestPembayaran(unittest.TestCase):
    def test_pembayaran_virtual_account_berhasil(self):
        hasil = pembayaran("BRI Virtual Account")
        self.assertEqual(hasil["status"], "menunggu_pembayaran")
        self.assertIn("va_number", hasil)
        self.assertIn("batas_waktu", hasil)
    def test_pembayaran_metode_tidak_dikenal(self):
        self.assertEqual(pembayaran("QRIS")["status"], "metode_tidak_dikenal")
    def test_va_number_valid_format(self):
        hasil = pembayaran("BRI Virtual Account")
        self.assertTrue(hasil["va_number"].isdigit())

class TestHalamanError(unittest.TestCase):

    def test_url_valid(self):
        hasil = akses_url("https://klikindomaret.com/home")
        self.assertEqual(hasil["status"], 200)
        self.assertIn("halaman ditemukan", hasil["content"])

    def test_url_tidak_ditemukan(self):
        hasil = akses_url("https://klikindomaret.com/halaman-tidak-ada")
        self.assertEqual(hasil["status"], 404)
        self.assertIn("Halaman tidak ditemukan", hasil["content"])

    def test_tautan_kembali_beranda(self):
        hasil = akses_url("https://klikindomaret.com/salah-url")
        self.assertIn("Klik Indomaret", hasil["content"])

# ==================== MAIN ====================
if __name__ == '__main__':
    unittest.main()
