import unittest
from usecase import checkout_usecase

class TestCheckoutUsecase(unittest.TestCase):
    def test_checkout_success(self):
        result = checkout_usecase.checkout({'item': 1}, "Alamat")
        self.assertEqual(result, "menu_pembayaran")

    def test_checkout_fail_empty_cart(self):
        result = checkout_usecase.checkout({}, "Alamat")
        self.assertEqual(result, "checkout_gagal")

    def test_pembayaran_bri(self):
        result = checkout_usecase.pembayaran("BRI Virtual Account")
        self.assertEqual(result["status"], "menunggu_pembayaran")
