import unittest
import main as m


class check_answer(unittest.TestCase):
    def test_correct(self):
        answer = 4
        x = 2
        y = 2
        self.assertEqual(m.check_answer(answer,x,y), 1)
        self.assertEqual(m.get_points(), 1)
        m.I.points = 0

    def test_wrong(self):
        answer = 5
        x = 2
        y = 2
        self.assertEqual(m.check_answer(answer,x,y), 0)
        self.assertEqual(m.get_points(), 0)


class check_timer(unittest.TestCase):
    def test_timer_count(self):
        m.I.time_left = 1
        m.timer()
        self.assertEqual(m.I.time_left, 0)
        self.assertEqual(m.I.duration, 1)
        self.assertEqual(m.I.game_end, 1)
        m.Initiation()

if __name__ == '__main__':
    unittest.main()
