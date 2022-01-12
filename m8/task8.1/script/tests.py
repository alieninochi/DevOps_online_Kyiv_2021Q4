import unittest
import quad_equation


class TestEquation(unittest.TestCase):
    def test_discriminant(self):
        self.assertEqual(quad_equation.discriminant(7, 0, 10), -280)
        self.assertEqual(quad_equation.discriminant(0, 7, 6), 49)
        self.assertEqual(quad_equation.discriminant(1, 0, -21), 84)
        self.assertEqual(quad_equation.discriminant(16, 8, 1), 0)
        self.assertEqual(quad_equation.discriminant(-1, -1, 0), 1)

    def test_roots(self):
        self.assertEqual(quad_equation.roots(-280, 7, 0, 10), (complex(0, 1.195), complex(0, -1.195)))
        self.assertEqual(quad_equation.roots(49, 0, 7, 6), (None, None))
        self.assertEqual(quad_equation.roots(84, 1, 0, -21), (4.583, -4.583))
        self.assertEqual(quad_equation.roots(0, 16, 8, 1), -0.25)
        self.assertEqual(quad_equation.roots(1, -1, -1, 0), (-1, 0))

    def test_equation_solve(self):
        self.assertEqual(quad_equation.solv_square(1, 2, 3), (complex(-1, 1.414), complex(-1, -1.414)))
        self.assertEqual(quad_equation.solv_square(0, 62, -129), (None, None))
        self.assertEqual(quad_equation.solv_square(17, -20, 1), (1.124, 0.052))
        self.assertEqual(quad_equation.solv_square(-6, 66, 6), (-0.090, 11.090))
        self.assertEqual(quad_equation.solv_square(1, -6, 9), 3)


if __name__ == "__main__":
    unittest.main()
