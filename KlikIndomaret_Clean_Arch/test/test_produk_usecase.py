import unittest
from usecase import produk_usecase

class TestProdukUsecase(unittest.TestCase):
    def setUp(self):
        self.db = [{'id': 1, 'nama': 'Beras', 'harga': 12000}]

    def test_cari_produk(self):
        hasil = produk_usecase.cari_produk("Beras", self.db)
        self.assertEqual(len(hasil), 1)

    def test_tambah_produk(self):
        baru = {'id': 2, 'nama': 'Gula', 'harga': 10000}
        self.assertEqual(len(produk_usecase.tambah_produk(self.db, baru)), 2)

    def test_edit_produk(self):
        result = produk_usecase.edit_produk(self.db, 1, nama="Beras Premium")
        self.assertEqual(result['nama'], "Beras Premium")

    def test_hapus_produk(self):
        result = produk_usecase.hapus_produk(self.db, 1)
        self.assertEqual(len(result), 0)

    def test_baca_produk(self):
        result = produk_usecase.baca_produk(self.db, 1)
        self.assertEqual(result['id'], 1)
