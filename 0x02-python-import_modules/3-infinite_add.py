#!/usr/bin/python3
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("integers", metavar="N", nargs="*", type=int)
    args = parser.parse_args()
    print(sum(args.integers))
