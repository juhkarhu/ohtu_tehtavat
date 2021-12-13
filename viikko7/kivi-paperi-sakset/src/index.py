from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from kps import KPS




def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus.endswith("a"):

            peli = KPSPelaajaVsPelaaja()
            peli.pelaa()

        elif vastaus.endswith("b"):

            peli = KPSTekoaly()
            peli.pelaa()

        elif vastaus.endswith("c"):

            peli = KPSParempiTekoaly()
            peli.pelaa()
        
        else:
            break


if __name__ == "__main__":
    main()
