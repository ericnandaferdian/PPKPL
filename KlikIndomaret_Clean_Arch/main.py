from interface import controller

print("Login:", controller.login_controller("082358747380", "@Rumahsaya85"))
controller.tambah_produk_controller(1, "Beras", 12000)
controller.tambah_produk_controller(2, "Gula", 10000)
print("Produk setelah tambah:", controller.produk_db)
