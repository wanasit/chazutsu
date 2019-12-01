import os
import sys
import shutil
import unittest
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
import chazutsu.datasets


DATA_ROOT = os.path.join(os.path.dirname(__file__), "data/katakana")
if not os.path.exists(DATA_ROOT):
    os.mkdir(DATA_ROOT)


class TestKatakana(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(DATA_ROOT):
            shutil.rmtree(DATA_ROOT)

    def test_download_full(self):
        d = chazutsu.datasets.Katakana()
        r = d.download(test_size=0.5)
        self.assertEqual(r.train_data().shape[1], 2)
        self.assertGreater(r.train_data().shape[0], 50000)
        self.assertGreater(r.test_data().shape[0], 50000)
        self.assertGreater(r.data().shape[0], 50000)

    def test_download_sample(self):
        d = chazutsu.datasets.Katakana()
        r = d.download(test_size=0.1, sample_count=1000)

        self.assertEqual(r.sample_data().shape, (1000, 2))
        self.assertEqual(r.train_data().shape, (900, 2))
        self.assertEqual(r.test_data().shape, (100, 2))


if __name__ == "__main__":
    unittest.main()
