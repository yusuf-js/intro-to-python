class hewan: #  hewan itu nama_dari kelas
    nama_hewan = "default" #nama_hewan ini property sifat public
    _umur_hewan = 10 #ini sifat private

    def __init__(self,nama):
        self.nama_hewan = nama

    def makan(self) : #method
        print("Hewan sedang makan")

kucing = hewan("gh")
kucing.nama_hewan = "tom"
print(f"nama kucing {kucing.nama_hewan}")
print("kucing sedang apa?")
kucing.makan()

