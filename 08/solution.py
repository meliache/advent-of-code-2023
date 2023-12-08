#!/usr/bin/env python3
import logging
from dataclasses import dataclass
from itertools import cycle
from pathlib import Path

IN_FPATH = Path(__file__).parent / "input"


def get_directions() -> cycle:
    """Return cycle of 'L'/'R' strings"""
    with open(IN_FPATH) as infile:
        return cycle([*infile.readline().strip()])


def get_node_name_dict() -> dict[str, tuple[str, str]]:
    """Return dictionary of node names to tuples of daughter names"""
    node_name_dict = {}
    with open(IN_FPATH) as infile:
        for line in infile.readlines()[2:]:
            name, children = line.split(" = ")
            children = tuple(children.strip(" \n)(").split(", "))
            node_name_dict[name] = children
    return node_name_dict


def main():
    directions = get_directions()
    node_dict = get_node_name_dict()

    node = "AAA"
    n_steps: int = 0
    for direction in directions:
        logging.info(f"{n_steps=}, {node=}, {direction=}")
        if node == "ZZZ":
            return n_steps
        match direction:
            case "L":
                node = node_dict[node][0]
            case "R":
                node = node_dict[node][1]
            case _:
                raise ValueError(f"Direction should be L or R but is {direction}")
        n_steps += 1
    return n_steps


if __name__ == "__main__":
    log_path = Path(__file__).parent / "log"
    logging.basicConfig(
        filename=log_path,
        encoding="utf-8",
        level=logging.INFO,
        filemode="w",
    )
    n_steps = main()
    print(f"Steps needed: {n_steps:d}")
