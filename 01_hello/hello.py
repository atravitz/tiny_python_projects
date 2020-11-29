#!/usr/bin/env python

import argparse


def main():
    parser = argparse.ArgumentParser(description="Say hello")
    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        type=str,
        default="World",
        help="The name to greet (default: World)",
    )
    args = parser.parse_args()
    print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()

