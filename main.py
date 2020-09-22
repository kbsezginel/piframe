import time
import argparse

from piframe.display import Display
from piframe.switch import Switch


def parse():
    parser = argparse.ArgumentParser(
        description="""
        PiFrame | Raspberry PI Photo Frame
        """,
        epilog="""
    Example:
    > python3 piframe.py
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    # Optional arguments
    parser.add_argument("--switch", "-s", default=26, type=int, help="Switch pin no (default: 26)")
    args = parser.parse_args()
    return args


def main(args):
    switch = Switch(args.switch)
    display = Display()
    while True:
        switch.read()
        if switch.on and display.state == "off":
            display.toggle("on")
        elif not switch.on and display.state == "on":
            display.toggle("off")
        time.sleep(0.5)
        print(display)


if __name__ == "__main__":
    args = parse()
    main(args)
