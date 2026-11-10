#!/usr/bin/env python3
import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = [
        "alice", "bob", "charlie", "dylan"
    ]
    actions = [
        "run", "eat", "sleep", "grab", "move",
        "climb", "swim", "use", "release"
    ]
    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


def consume_event(
    events: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while events:
        index = random.randrange(len(events))
        event = events.pop(index)
        yield (event)


def main() -> None:
    print("=== Game Data Stream Processor ===")
    gen = gen_event()
    for i in range(1000):
        player, action = next(gen)
        print(f"Event {i}: Player {player} did action {action}")

    events_list = [next(gen) for _ in range(10)]
    print(f"Built list of 10 events: {events_list}")

    for event in consume_event(events_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events_list}")


if __name__ == "__main__":
    main()
