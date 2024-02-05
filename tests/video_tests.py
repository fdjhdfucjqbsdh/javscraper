import unittest
from javscraper import *


class VideoTests(unittest.TestCase):
    def test_javlibrary_en(self):
        base = JAVLibrary()
        base.debug = True

        result = base.get_video("abcdefghijklm")
        self.assertIsNone(result)

        result = base.get_video("SDAB-187")
        self.assertIsNotNone(result)
        self.assertEqual(result.code, "SDAB-187")
        self.assertEqual(result.studio, "SOD Create")
        self.assertEqual(len(result.actresses), 1)
        self.assertEqual(result.actresses[0], "Kamon Non")
        self.assertIsNone(result.sample_video)
        self.assertTrue(result.image.startswith("http"))
        self.assertTrue(result.score > 1)

    def test_javlibrary_ja(self):
        base = JAVLibrary("ja")

        result = base.get_video("abcdefghijklm")
        self.assertIsNone(result)

        result = base.get_video("SDAB-187")
        self.assertIsNotNone(result)
        self.assertEqual(result.code, "SDAB-187")
        self.assertEqual(result.studio, "SODクリエイト")
        self.assertEqual(len(result.actresses), 1)
        self.assertEqual(result.actresses[0], "花門のん")
        self.assertIsNone(result.sample_video)
        self.assertTrue(result.image.startswith("http"))
        self.assertTrue(result.score > 1)

    def test_javlibrary_tw(self):
        base = JAVLibrary("tw")

        result = base.get_video("abcdefghijklm")
        self.assertIsNone(result)

        result = base.get_video("SDAB-187")
        self.assertIsNotNone(result)
        self.assertEqual(result.code, "SDAB-187")
        self.assertEqual(result.studio, "SOD Create")
        self.assertEqual(len(result.actresses), 1)
        self.assertEqual(result.actresses[0], "花門のん")
        self.assertIsNone(result.sample_video)
        self.assertTrue(result.image.startswith("http"))
        self.assertTrue(result.score > 1)

    def test_javlibrary_cn(self):
        base = JAVLibrary("cn")

        result = base.get_video("abcdefghijklm")
        self.assertIsNone(result)

        result = base.get_video("SDAB-187")
        self.assertIsNotNone(result)
        self.assertEqual(result.code, "SDAB-187")
        self.assertEqual(result.studio, "SOD Create")
        self.assertEqual(len(result.actresses), 1)
        self.assertEqual(result.actresses[0], "花門のん")
        self.assertIsNone(result.sample_video)
        self.assertTrue(result.image.startswith("http"))
        self.assertTrue(result.score > 1)

    def test_mgstage(self):
        base = MGStage()
        base.debug = True

        result = base.get_video("345SIMM_600")
        self.assertIsNone(result)

        result = base.get_video("345SIMM-600")
        self.assertIsNotNone(result)
        self.assertEqual(result.code, "345SIMM-600")
        self.assertEqual(result.studio, "DOC")
        self.assertTrue(result.image.startswith("http"))
        self.assertEqual(len(result.actresses), 1)
        self.assertEqual(result.actresses[0], "りなちゃん")
        self.assertIsNotNone(result.sample_video)
        self.assertIsNotNone(result.description)
        self.assertTrue(result.sample_video.startswith("http"))
        self.assertTrue(result.score > 4)

    def test_s1(self):
        base = S1()

        result = base.get_video("SSIS_140")
        self.assertIsNone(result)

        result = base.get_video("SSIS-140")
        self.assertIsNotNone(result)
        self.assertEqual(result.code, "SSIS-140")
        self.assertTrue(result.image.startswith("https"))
        self.assertEqual(len(result.actresses), 1)
        self.assertEqual(result.actresses[0], "藤田こずえ")
        self.assertIsNotNone(result.sample_video)
        self.assertIsNotNone(result.description)
        self.assertTrue(result.sample_video.startswith("http"))

    def test_sod(self):
        base = SOD()

        result = base.get_video("OKS_116")
        self.assertIsNone(result)

        result = base.get_video("OKS-116")
        self.assertIsNotNone(result)
        self.assertEqual(result.code, "OKS-116")
        self.assertEqual(result.studio, "親父の個撮")
        self.assertTrue(result.image.startswith("https"))
        self.assertEqual(len(result.actresses), 1)
        self.assertEqual(result.actresses[0], "宮崎リン")
        self.assertIsNotNone(result.description)
        self.assertIsNone(result.sample_video)

    def test_10musume(self):
        base = TenMusume()

        result = base.get_video("1")
        self.assertIsNone(result)

        result = base.get_video("080521_01")
        self.assertIsNotNone(result)
        self.assertEqual(result.code, "080521_01")
        self.assertEqual(result.studio, "10musume")
        self.assertTrue(result.image.startswith("https"))
        self.assertEqual(len(result.actresses), 1)
        self.assertEqual(result.actresses[0], "竹田しょうこ")
        self.assertIsNotNone(result.description)
        self.assertIsNone(result.sample_video)
        self.assertTrue(2 < result.score < 3)

        base = TenMusume(english=True)
        result = base.get_video("080521_01")
        self.assertIsNotNone(result)
        self.assertEqual(result.code, "080521_01")
        self.assertEqual(result.studio, "10musume")
        self.assertTrue(result.image.startswith("https"))
        self.assertEqual(len(result.actresses), 1)
        self.assertEqual(result.actresses[0], "Shouko Takeda")
        self.assertEqual(result.description, "")
        self.assertIsNone(result.sample_video)

    def test_ideapocket(self):
        base = IdeaPocket()

        result = base.get_video("IPX-10000")
        self.assertIsNone(result)

        result = base.get_video("IPX-445")
        self.assertIsNotNone(result)
        self.assertEqual(result.code, "IPX-445")
        self.assertEqual(result.studio, "IdeaPocket")
        self.assertTrue(result.image.startswith("https"))
        self.assertEqual(len(result.actresses), 1)
        self.assertEqual(result.actresses[0], "希島あいり")
        self.assertIsNotNone(result.description)
        self.assertIsNotNone(result.sample_video)

    def test_caribbeancom_ja(self):
        base = Caribbeancom()

        result = base.get_video("zzzzzzzzz")
        self.assertIsNone(result)

        result = base.get_video("Caribbeancom-080621_001")
        self.assertIsNotNone(result)
        self.assertEqual(result.code, "080621-001")
        self.assertEqual(result.studio, "Caribbeancom")
        self.assertTrue(result.image.startswith("https"))
        self.assertIsNotNone(result.sample_video)
        self.assertTrue(result.sample_video.startswith("https"))
        self.assertEqual(len(result.actresses), 1)
        self.assertEqual(result.actresses[0], "輝月あんり")
        self.assertIsNotNone(result.description)

    def test_caribbeancom_en(self):
        base = Caribbeancom("en")

        result = base.get_video("zzzzzzzzz")
        self.assertIsNone(result)

        result = base.get_video("Caribbeancom-080621_001")
        self.assertIsNotNone(result)
        self.assertEqual(result.code, "080621-001")
        self.assertEqual(result.studio, "Caribbeancom")
        self.assertTrue(result.image.startswith("https"))
        self.assertIsNotNone(result.sample_video)
        self.assertTrue(result.sample_video.startswith("https"))
        self.assertEqual(len(result.actresses), 1)
        self.assertEqual(result.actresses[0], "Anri Kizuki")
        self.assertIsNotNone(result.description)

    def test_kmproduce(self):
        base = KMProduce()

        result = base.get_video("zzzzzzzzz")
        self.assertIsNone(result)

        result = base.get_video("BAZX-304")
        self.assertIsNotNone(result)
        self.assertEqual(result.code, "BAZX-304")
        self.assertEqual(result.studio, "K.M.Produce")
        self.assertTrue(result.image.startswith("https"))
        self.assertIsNone(result.sample_video)
        self.assertEqual(len(result.actresses), 0)
        self.assertIsNotNone(result.description)

        result = base.get_video("okax-206")
        self.assertIsNotNone(result)
        self.assertEqual(result.code, "OKAX-206")
        self.assertEqual(result.studio, "K.M.Produce")
        self.assertTrue(result.image.startswith("https"))
        self.assertIsNone(result.sample_video)
        # self.assertTrue(result.sample_video.startswith("https"))
        self.assertEqual(len(result.actresses), 1)
        self.assertEqual(result.actresses[0], "素人モニター13人")
        self.assertIsNotNone(result.description)
        self.assertEqual(result.release_date.year, 2017)
        self.assertEqual(result.release_date.month, 4)

    def test_max_a(self):
        base = MaxA()

        result = base.get_video("zzzzzzzzz")
        self.assertIsNone(result)

        result = base.get_video("XVSR-604")
        self.assertIsNotNone(result)
        self.assertEqual(result.code, "XVSR-604")
        self.assertEqual(result.studio, "MAX-A")
        self.assertTrue(result.image.startswith("https"))
        self.assertIsNone(result.sample_video)
        self.assertEqual(len(result.actresses), 1)
        self.assertEqual(result.actresses[0], "最上一花/佐藤花")
        self.assertIsNotNone(result.description)

    def test_aircontrol(self):
        base = AirControl()

        result = base.get_video("zzzzzzzzz")
        self.assertIsNone(result)

        result = base.get_video("ome-401")
        self.assertIsNotNone(result)
        self.assertEqual(result.code, "OME-401")
        self.assertEqual(result.studio, "Air Control")
        self.assertTrue(result.image.startswith("https"))
        self.assertIsNotNone(result.sample_video)
        self.assertTrue(result.sample_video.startswith("https"))
        self.assertEqual(len(result.actresses), 1)
        self.assertEqual(result.actresses[0], "清瀬汐希")
        self.assertIsNotNone(result.description)

    def test_alicejapan(self):
        base = AliceJapan()

        result = base.get_video("zzzzzzzzz")
        self.assertIsNone(result)

        result = base.get_video("DVAJ-528")
        self.assertIsNotNone(result)
        self.assertEqual(result.code, "DVAJ-528b")
        self.assertEqual(result.studio, "Alice Japan")
        self.assertTrue(result.image.startswith("http"))
        self.assertIsNone(result.sample_video)
        self.assertEqual(len(result.actresses), 1)
        self.assertEqual(result.actresses[0], "前乃菜々")
        self.assertIsNotNone(result.description)

    def test_aroma(self):
        base = Aroma()

        result = base.get_video("zzzzzzzzz")
        self.assertIsNone(result)

        result = base.get_video("ARM-999")
        self.assertIsNotNone(result)
        self.assertEqual(result.code, "ARM-999")
        self.assertEqual(result.studio, "Aroma Kikaku")
        self.assertTrue(result.image.startswith("http"))
        self.assertIsNotNone(result.sample_video)
        self.assertTrue(result.sample_video.startswith("http"))
        self.assertEqual(len(result.actresses), 5)
        self.assertEqual(result.actresses[0], "あおいれな")
        self.assertIsNotNone(result.description)

    def test_attackers(self):
        base = Attackers()

        result = base.get_video("zzzzzzzzz")
        self.assertIsNone(result)

        result = base.get_video("ADN-330")
        self.assertIsNotNone(result)
        self.assertEqual(result.code, "ADN-330")
        self.assertEqual(result.studio, "Attackers")
        self.assertTrue(result.image.startswith("http"))
        self.assertIsNone(result.sample_video)
        self.assertEqual(len(result.actresses), 1)
        self.assertEqual(result.actresses[0], "二宮ひかり")
        self.assertIsNotNone(result.description)

    def test_auroraproject(self):
        base = AuroraProject()

        result = base.get_video("APKH-185")
        self.assertIsNotNone(result)
        self.assertEqual(result.code, "APKH-185")
        self.assertEqual(result.studio, "Aurora Project Annex")
        self.assertTrue(result.image.startswith("http"))
        self.assertEqual(result.sample_video, None)
        self.assertEqual(len(result.actresses), 1)
        self.assertEqual(result.actresses[0], "香椎みすず")
        self.assertIsNotNone(result.description)
        self.assertEqual(len(result.genres), 12)

        result = base.get_video("zzzzzzzzz")
        self.assertIsNone(result)

    def test_befree(self):
        base = BeFree()

        result = base.get_video("zzzzzzzzz")
        self.assertIsNone(result)

        result = base.get_video("BF-640")
        self.assertIsNotNone(result)
        self.assertEqual(result.code, "BF-640")
        self.assertEqual(result.studio, "BeFree")
        self.assertTrue(result.image.startswith("http"))
        self.assertIsNotNone(result.sample_video)
        self.assertTrue(result.sample_video.startswith("http"))
        self.assertEqual(len(result.actresses), 1)
        self.assertEqual(result.actresses[0], "朝倉ここな")
        self.assertIsNotNone(result.description)

    def test_bi(self):
        base = Bi()

        result = base.get_video("zzzzzzzzz")
        self.assertIsNone(result)

        result = base.get_video("CJOD-307")
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.name)
        self.assertEqual(result.code, "CJOD-307")
        self.assertEqual(result.studio, "Bi")
        self.assertTrue(result.image.startswith("http"))
        self.assertIsNotNone(result.sample_video)
        self.assertTrue(result.sample_video.startswith("http"))
        self.assertEqual(len(result.actresses), 3)
        self.assertEqual(result.actresses[0], "初川みなみ")
        self.assertIsNotNone(result.description)

    def test_bigmorkal(self):
        base = BigMorkal()

        result = base.get_video("zzzzzzzzz")
        self.assertIsNone(result)

        result = base.get_video("BDSR-459")
        self.assertIsNotNone(result)
        self.assertEqual(result.code, "BDSR-459")
        self.assertEqual(result.studio, "BIGMORKAL")
        self.assertTrue(result.image.startswith("http"))
        self.assertIsNone(result.sample_video)
        self.assertEqual(len(result.actresses), 1)
        self.assertEqual(result.actresses[0], "イチャラブエッチなオンナたち22人")
        self.assertIsNotNone(result.description)

    def test_deeps(self):
        base = Deeps()

        result = base.get_video("zzzzzzzzz")
        self.assertIsNone(result)

        result = base.get_video("DVDMS-699")

        self.assertIsNotNone(result)
        self.assertEqual(result.code, "DVDMS-699")
        self.assertEqual(result.studio, "Deeps")
        self.assertTrue(result.image.startswith("http"))
        self.assertIsNotNone(result.sample_video)
        self.assertTrue(result.sample_video.startswith("http"))
        self.assertIsNone(result.description)

    def test_dmm_pro(self):
        base = DMM()

        result = base.get_video("zzzzzzzzz")
        self.assertIsNone(result)

        result = base.get_video("JUFE-202")
        self.assertIsNotNone(result)
        self.assertEqual(result.code, "JUFE-202")
        self.assertEqual(result.studio, "Fitch")
        self.assertTrue(result.image.startswith("http"))
        self.assertIsNotNone(result.sample_video)
        self.assertTrue(result.sample_video.startswith("http"))
        self.assertIsNotNone(result.description)
        self.assertEqual(result.release_date.year, 2020)
        self.assertEqual(result.release_date.month, 9)
        self.assertEqual(len(result.actresses), 1)
        self.assertEqual(result.actresses[0], "桃園怜奈")
        self.assertGreater(result.score, 4)

    def test_dmm_amateur(self):
        base = DMM()

        result = base.get_video("zzzzzzzzz")
        self.assertIsNone(result)

        search = base.search("POW-006")
        search = [x for x in search if "videoc" in x][0]

        result = base.get_video(search)
        self.assertIsNotNone(result)
        self.assertEqual(result.code, "POW-006")
        self.assertEqual(result.studio, "素人ホイホイpower")
        self.assertTrue(result.image.startswith("http"))
        self.assertIsNotNone(result.sample_video)
        self.assertTrue(result.sample_video.startswith("http"))
        self.assertIsNotNone(result.description)
        self.assertEqual(result.release_date.year, 2020)
        self.assertEqual(result.release_date.month, 5)
        self.assertEqual(len(result.actresses), 0)
        self.assertGreater(result.score, 4.5)

    def test_1pondo(self):
        base = OnePondo()

        result = base.get_video("zzzzzzzzz")
        self.assertIsNone(result)

        result = base.get_video("061915_100")
        self.assertEqual("モデルコレクション リゾート 佐伯ゆきな", result.name)
        self.assertEqual("061915_100", result.code)
        self.assertEqual("1pondo", result.studio)
        self.assertIsNotNone(result.image)
        self.assertTrue(result.image.startswith("https"))
        self.assertEqual(len(result.actresses), 1)
        self.assertTrue("佐伯ゆきな", result.actresses[0])
        self.assertTrue(2015, result.release_date.year)
        self.assertIsNotNone(result.description)

        base = OnePondo(english=True)
        result = base.get_video("061915_100")
        self.assertEqual("Model Collection: Yukina Saeki", result.name)
        self.assertEqual("061915_100", result.code)
        self.assertEqual("1pondo", result.studio)
        self.assertIsNotNone(result.image)
        self.assertTrue(result.image.startswith("https"))
        self.assertEqual(len(result.actresses), 1)
        self.assertTrue("Yukina Saeki", result.actresses[0])
        self.assertTrue(2015, result.release_date.year)
        self.assertIsNotNone(result.description)

    def test_heyzo(self):
        base = Heyzo()

        result = base.get_video("zzzzzzzzz")
        self.assertIsNone(result)

        result = base.get_video("2478")
        self.assertEqual("ねっとりベロチュー、みっちりセックス～グチョグチョにしてほしい～", result.name)
        self.assertEqual("Heyzo-2478", result.code)
        self.assertEqual("Heyzo", result.studio)
        self.assertIsNotNone(result.image)
        self.assertTrue(result.image.startswith("https"))
        self.assertEqual(len(result.actresses), 1)
        self.assertTrue("森田みゆ", result.actresses[0])
        self.assertTrue(2021, result.release_date.year)
        self.assertIsNotNone(result.description)

        base = Heyzo(english=True)
        result = base.get_video("2478")
        self.assertEqual("Deep Kiss, Furious Sex -Make Me Wet-", result.name)
        self.assertEqual("Heyzo-2478", result.code)
        self.assertEqual("Heyzo", result.studio)
        self.assertIsNotNone(result.image)
        self.assertTrue(result.image.startswith("https"))
        self.assertEqual(len(result.actresses), 1)
        self.assertTrue("Miyu Morita", result.actresses[0])
        self.assertTrue(2021, result.release_date.year)
        self.assertEqual(result.description, "")


if __name__ == '__main__':
    unittest.main()
