import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 3:
                return 0
            return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, 'kahvi', 6)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        self.kauppa.aloita_asiointi()

    def test_edellisen_ostoksen_hinta_ei_nay_uudessa_ostoksessa(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with('pekka', 42, '12345', self.kauppa._kaupan_tili, 5)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("joonatan", "0012358")
        self.pankki_mock.tilisiirto.assert_called_with('joonatan', 42, '0012358', self.kauppa._kaupan_tili, 6)
        
    def test_ostokset_onnistuu_kun_toinen_tuote_poistetaan(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(2)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with('pekka', 42, '12345', self.kauppa._kaupan_tili, 5)

    def test_kauppa_kutsuu_uuden_viitenumeron_jokaisen_ostoksen_yhteydessä(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 1)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("joonatan", "0012358")
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään ostokset
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostokset_paatyttya_pankin_tilisiirtoa_kutsutaan_oikeilla_parametreilla(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with('pekka', self.viitegeneraattori_mock.uusi(), '12345', self.kauppa._kaupan_tili , 5)

    def test_ostokset_paattyy_oikein_kahdella_ostoksella(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu('kalle', '54321')

        self.pankki_mock.tilisiirto.assert_called_with('kalle', self.viitegeneraattori_mock.uusi(), '54321', self.kauppa._kaupan_tili, 11)

    def test_ostokset_paattyy_oikein_kahdella_samalla_ostoksella(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu('joonas', '0112358')

        self.pankki_mock.tilisiirto.assert_called_with('joonas', self.viitegeneraattori_mock.uusi(), '0112358', self.kauppa._kaupan_tili, 10)

    def test_ostokset_paattyy_oikein_kun_toisen_ostoksen_saldo_on_loppu(self):
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu('matias', '0112358')

        self.pankki_mock.tilisiirto.assert_called_with('matias', self.viitegeneraattori_mock.uusi(), '0112358', self.kauppa._kaupan_tili, 6)
