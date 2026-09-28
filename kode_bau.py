"""Modul contoh fungsi yang sudah dirapikan sesuai PEP 8."""


def jumlahkan_dan_cetak(nilai_a, nilai_b, daftar, tambahan):
    """Menjumlahkan beberapa nilai lalu mencetak hasilnya.

    Args:
        nilai_a: Bilangan pertama.
        nilai_b: Bilangan kedua.
        daftar: List yang elemen pertamanya ikut dijumlahkan.
        tambahan: Bilangan tambahan.

    Returns:
        Total penjumlahan, atau None jika daftar kosong.
    """
    if not daftar:
        return None
    total = daftar[0] + tambahan + nilai_a + nilai_b
    print(total)
    return total


def main():
    """Fungsi utama program."""
    jumlahkan_dan_cetak(1, 2, [2], 3)


if __name__ == "__main__":
    main()
    