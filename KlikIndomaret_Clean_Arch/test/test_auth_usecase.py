import unittest
from usecase import auth_usecase

class TestAuthUsecase(unittest.TestCase):
    def test_login_success(self):
        self.assertEqual(auth_usecase.login("082358747380", "@Rumahsaya85"), "home")

    def test_login_fail(self):
        self.assertNotEqual(auth_usecase.login("user", "salah"), "home")

    def test_logout_active(self):
        self.assertEqual(auth_usecase.logout(True)["status"], "logged_out")

    def test_logout_no_session(self):
        self.assertEqual(auth_usecase.logout(False)["status"], "already_logged_out")
