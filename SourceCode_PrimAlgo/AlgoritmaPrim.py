print("23343066")
print("Gema Pratama")

import sys

class Graf:
    def __init__(self, jumlah_simpul):
        self.jumlah_simpul = jumlah_simpul
        self.graf = [[0 for _ in range(jumlah_simpul)] for _ in range(jumlah_simpul)]

    def tambahkan_edge(self, simpul1, simpul2, bobot):
        self.graf[simpul1][simpul2] = bobot
        self.graf[simpul2][simpul1] = bobot

    def prim_mst(self):
        induk = [None] * self.jumlah_simpul
        bobot_minimum = [sys.maxsize] * self.jumlah_simpul
        bobot_minimum[0] = 0  
        mst_set = [False] * self.jumlah_simpul

        induk[0] = -1  

        for _ in range(self.jumlah_simpul):
            simpul_minimum = self.cari_simpul_minimum(bobot_minimum, mst_set)
            mst_set[simpul_minimum] = True

            for simpul in range(self.jumlah_simpul):
                if self.graf[simpul_minimum][simpul] > 0 and not mst_set[simpul] and bobot_minimum[simpul] > self.graf[simpul_minimum][simpul]:
                    bobot_minimum[simpul] = self.graf[simpul_minimum][simpul]
                    induk[simpul] = simpul_minimum

        self.cetak_mst(induk)

    def cari_simpul_minimum(self, bobot_minimum, mst_set):
        min_bobot = sys.maxsize
        min_simpul = -1

        for simpul in range(self.jumlah_simpul):
            if bobot_minimum[simpul] < min_bobot and not mst_set[simpul]:
                min_bobot = bobot_minimum[simpul]
                min_simpul = simpul

        return min_simpul

    def cetak_mst(self, induk):
        print("\nEdge \tBobot")
        for i in range(1, self.jumlah_simpul):
            print(f"{induk[i]} - {i}\t{self.graf[i][induk[i]]}")

if __name__ == "__main__":
    g = Graf(5)
    g.tambahkan_edge(0, 1, 2)
    g.tambahkan_edge(0, 3, 6)
    g.tambahkan_edge(1, 2, 3)
    g.tambahkan_edge(1, 3, 8)
    g.tambahkan_edge(1, 4, 5)
    g.tambahkan_edge(2, 4, 7)
    g.tambahkan_edge(3, 4, 9)

    g.prim_mst()