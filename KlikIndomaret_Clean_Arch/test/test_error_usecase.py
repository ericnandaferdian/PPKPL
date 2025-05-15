import unittest
from usecase import error_usecase

class TestErrorUsecase(unittest.TestCase):
    def test_url_valid(self):
        result = error_usecase.akses_url("https://klikindomaret.com/home")
        self.assertEqual(result["status"], 200)

    def test_url_404(self):
        result = error_usecase.akses_url("https://klikindomaret.com/halaman-tidak-ada")
        self.assertEqual(result["status"], 404)
