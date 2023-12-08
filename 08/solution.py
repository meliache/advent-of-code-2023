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


def part1():
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


def part2():
    directions = get_directions()
    node_dict = get_node_name_dict()

    nodes: list[str] = [node for node in node_dict if node.endswith("A")]
    n_steps: int = 0
    for direction in directions:
        print(f"{n_steps=}, {nodes=}, {direction=}")
        if all(node.endswith("Z") for node in nodes):
            return n_steps
        match direction:
            case "L":
                nodes = [node_dict[node][0] for node in nodes]
            case "R":
                nodes = [node_dict[node][1] for node in nodes]
            case _:
                raise ValueError(f"Direction should be L or R but is {direction}")
        n_steps += 1
    return n_steps


if __name__ == "__main__":
    # n_steps_p2 = part1()
    # print(f"Part1: Steps needed: {n_steps_p2:d}")

    n_steps_p2 = part2()
    print(f"Part1: Steps needed: {n_steps_p2:d}")
