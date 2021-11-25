import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.maito = Tuote("Maito", 3)
        self.kahvi = Tuote('Kahvi', 7)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_sama_kuin_tuotteen_hinta(self):
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_2_tavaraa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.kahvi)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_tuotteiden_hintojen_summa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.kahvi)

        self.assertEqual(self.kori.hinta(), 10)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_2_tavaraa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_tuotteiden_hintojen_summa(self):
        self.kori.lisaa_tuote(self.kahvi)
        self.kori.lisaa_tuote(self.kahvi)

        self.assertEqual(self.kori.hinta(), 14)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        self.kori.lisaa_tuote(self.maito)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        self.kori.lisaa_tuote(self.maito)

        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), 'Maito')
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosoliota(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.kahvi)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_kori_sisaltaa_yhden_ostosolion(self):
        self.kori.lisaa_tuote(self.kahvi)
        self.kori.lisaa_tuote(self.kahvi)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_kori_sisaltaa_yhden_ostosolion_jolla_sama_nimi_kuin_tuotteella_ja_lkm_on_2(self):
        self.kori.lisaa_tuote(self.kahvi)
        self.kori.lisaa_tuote(self.kahvi)

        ostokset = self.kori.ostokset()[0]
        self.assertEqual(ostokset.tuotteen_nimi(), 'Kahvi')
        self.assertEqual(ostokset.lukumaara(), 2)

    def test_korissa_kaksi_samaa_tuotetta_ja_yhden_poistamisen_jalkeen_korissa_ostos_jossa_tuotetta_yksi_kappale(self):
        self.kori.lisaa_tuote(self.kahvi)
        self.kori.lisaa_tuote(self.kahvi)
        ostokset = self.kori.ostokset()[0]
        self.assertEqual(ostokset.tuotteen_nimi(), 'Kahvi')
        self.assertEqual(ostokset.lukumaara(), 2)
        
        self.kori.poista_tuote(self.kahvi)

        ostokset = self.kori.ostokset()[0]
        self.assertEqual(ostokset.tuotteen_nimi(), 'Kahvi')
        self.assertEqual(ostokset.lukumaara(), 1)

    def test_jos_lisatty_tuote_joka_poistetaan_niin_kori_on_tyhja(self):
        self.kori.lisaa_tuote(self.kahvi)
        self.kori.poista_tuote(self.kahvi)
        ostokset = self.kori.ostokset()[0]
        self.assertEqual(ostokset.lukumaara(), 0)

    def test_metodi_tyhjenna_tyhjentaa_ostoskorin(self):
        self.kori.lisaa_tuote(self.kahvi)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
        self.kori.tyhjenna()
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
