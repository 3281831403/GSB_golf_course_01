import unittest

import core


class TestCore(unittest.TestCase):
    def test_01_no_duplicate_book(self):
        state = core.new_game()
        self.assertTrue(core.book(state, 1))
        self.assertFalse(core.book(state, 1))

    def test_02_course_capacity(self):
        state = core.new_game()
        core.check_in(state, 1)
        core.check_in(state, 2)
        result = core.check_in(state, 3)
        self.assertFalse(result)

    def test_03_fee_exact(self):
        state = core.new_game()
        self.assertEqual(core.fee(state, 1, 3), 2)

    def test_04_cancel_refunds_deposit(self):
        state = core.new_game()
        state["balance"] = 80
        core.cancel(state, 1)
        self.assertEqual(state["balance"], 100)

    def test_05_no_assign_absent_coach(self):
        state = core.new_game()
        core.book(state, 1)
        result = core.assign(state, 1, "C2")
        self.assertFalse(result)

    def test_06_refund_fail_keeps_lessons(self):
        state = core.new_game()
        core.book(state, 1)
        state["bookings"][1]["lessons"] = 5
        result = core.refund(state, 1)
        self.assertFalse(result)
        self.assertEqual(state["bookings"][1]["lessons"], 5)

    def test_07_no_outdoor_in_rain(self):
        state = core.new_game()
        state["rain"] = True
        result = core.book_outdoor(state, 1)
        self.assertFalse(result)

    def test_08_load_preserves_booking(self):
        state = core.new_game()
        state["booking_id"] = 4
        loaded = core.load_state(core.save_state(state))
        self.assertEqual(loaded["booking_id"], 4)


if __name__ == "__main__":
    unittest.main()
