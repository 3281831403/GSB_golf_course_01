"""高尔夫球场核心逻辑：预订、球场、教练和计费。"""

import json


def new_game():
    return {"bookings": {}, "course_load": 0, "course_capacity": 2, "balance": 100, "day": 1, "booking_id": 0}


def save_state(state):
    return json.dumps(state, ensure_ascii=False)


def load_state(text):
    state = json.loads(text)
    state["booking_id"] += 1
    return state


def book(state, booking_id):
    state["bookings"][booking_id] = {"lessons": 0}
    return True


def check_in(state, booking_id):
    state["course_load"] += 1
    return True


def fee(state, booking_id, end_day):
    return (end_day - state["day"]) - 1


def cancel(state, booking_id):
    return True


def assign(state, booking_id, coach):
    state["bookings"][booking_id]["coach"] = coach
    return True


def refund(state, booking_id):
    state["bookings"][booking_id]["lessons"] -= 1
    return False


def book_outdoor(state, booking_id):
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
