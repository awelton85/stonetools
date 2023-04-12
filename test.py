import unittest
from stonetools import calculate_piece_length, calculate_arc_length


class TestScriptFunctions(unittest.TestCase):
    def test_calculate_piece_length(self):
        self.assertAlmostEqual(
            calculate_piece_length(100, 5, 2),
            18.4, msg="Failed for overall_length=100, num_pieces=5, joint_spacing=2"
        )
        self.assertAlmostEqual(
            calculate_piece_length(50, 4, 1.5), 11.375,
            msg="Failed for overall_length=50, num_pieces=4, joint_spacing=1.5"
        )
        self.assertAlmostEqual(
            calculate_piece_length(75, 3, 2.5), 23.333333333333332,
            msg="Failed for overall_length=75, num_pieces=3, joint_spacing=2.5"
        )

    def test_calculate_arc_length(self):
        self.assertAlmostEqual(
            calculate_arc_length(10, 10),
            10.47197551196598,
            msg="Failed for radius=10, chord_length=10",
            places=8,
        )
        self.assertAlmostEqual(
            calculate_arc_length(5, 8),
            9.272952180016123,
            msg="Failed for radius=5, chord_length=8",
            places=8,
        )
        self.assertAlmostEqual(
            calculate_arc_length(20, 30),
            33.922483159259244,
            msg="Failed for radius=20, chord_length=30",
            places=8,
        )


if __name__ == "__main__":
    unittest.main()
