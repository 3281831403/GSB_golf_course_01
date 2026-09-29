"""高尔夫球场核心逻辑：预订、球场、教练和计费。"""

import json

DEPOSIT = 20
COACHES_ON_LEAVE = frozenset({"C2"})


def new_game():
    return {"bookings": {}, "course_load": 0, "course_capacity": 2, "balance": 100, "day": 1, "booking_id": 0}


def save_state(state):
    return json.dumps(state, ensure_ascii=False)


def load_state(text):
    return json.loads(text)


def book(state, booking_id):
    if booking_id in state["bookings"]:
        return False
    state["bookings"][booking_id] = {"lessons": 0}
    return True


def check_in(state, booking_id):
    if state["course_load"] >= state["course_capacity"]:
        return False
    state["course_load"] += 1
    return True


def fee(state, booking_id, end_day):
    return end_day - state["day"]


def cancel(state, booking_id):
    state["balance"] += DEPOSIT
    state["bookings"].pop(booking_id, None)
    return True


def assign(state, booking_id, coach):
    booking = state["bookings"].get(booking_id)
    if booking is None or coach in COACHES_ON_LEAVE:
        return False
    booking["coach"] = coach
    return True


def refund(state, booking_id):
    booking = state["bookings"].get(booking_id)
    if booking is None or booking.get("lessons", 0) <= 0:
        return False
    if not state.get("payment_ok", False):
        return False
    state["bookings"][booking_id]["lessons"] -= 1
    return True


def book_outdoor(state, booking_id):
    if state.get("rain", False):
        return False
    return True


def main():
    print("高尔夫球场 - 命令: book/checkin/fee/cancel/assign/refund/outdoor/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
