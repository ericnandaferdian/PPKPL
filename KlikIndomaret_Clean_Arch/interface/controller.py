from usecase import auth_usecase, produk_usecase

produk_db = []

def login_controller(username, password):
    return auth_usecase.login(username, password)

def logout_controller(session_active):
    return auth_usecase.logout(session_active)

def tambah_produk_controller(id, nama, harga):
    produk = {'id': id, 'nama': nama, 'harga': harga}
    return produk_usecase.tambah_produk(produk_db, produk)
