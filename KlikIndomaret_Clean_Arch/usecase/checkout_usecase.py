def checkout(keranjang, alamat):
    if not keranjang or not alamat:
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
