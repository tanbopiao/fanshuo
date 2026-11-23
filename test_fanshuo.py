"""返朔（FANSHUO）算子单测：名帖完整、行为达标、只增不覆盖。"""
import unittest

from fanshuo import Fanshuo


class TestFanshuo(unittest.TestCase):
    def setUp(self):
        self.op = Fanshuo()

    def test_describe(self):
        d = self.op.describe()
        self.assertEqual(d["repo"], "fanshuo")
        self.assertEqual(d["code"], "FANSHUO")
        self.assertTrue(d["anchor"].startswith("Ω₀⊂⊙∞⊂Ω"))
        self.assertTrue(d["mingwen"])

    def test_snapshot_rollback(self):
        sid = self.op.snapshot({"v": 1})
        self.assertEqual(self.op.rollback(sid), {"v": 1})
        with self.assertRaises(KeyError):
            self.op.rollback("SHUO-9999")


if __name__ == "__main__":
    unittest.main()
