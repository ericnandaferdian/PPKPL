def akses_url(url):
    halaman_tersedia = ["/home", "/produk", "/keranjang", "/checkout"]
    if any(url.endswith(path) for path in halaman_tersedia):
        return {"status": 200, "content": "halaman ditemukan"}
    return {
        "status": 404,
        "content": "Halaman tidak ditemukan. Mungkin URL salah. Kembali ke Klik Indomaret"
    }
