"""返朔（FANSHUO）算子骨架单测：名帖完整、桩位齐整、只增不覆盖。"""
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

    def test_snapshot_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.snapshot(None)

    def test_rollback_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.rollback(None)


if __name__ == "__main__":
    unittest.main()
