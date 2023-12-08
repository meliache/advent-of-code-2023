#!/usr/bin/env python3
import logging
from functools import reduce
from itertools import cycle
from math import lcm
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
    for n_steps, direction in enumerate(directions):
        logging.info(f"{n_steps=}, {node=}, {direction=}")
        if node == "ZZZ":
            return n_steps
        match direction:
            case "L":
                node = node_dict[node][0]
            case "R":
                node = node_dict[node][1]
    return n_steps


### Functions for part2


def get_n_steps_for_each_starting_node(
    starting_nodes: list[str], node_dict: dict[str, tuple[str, str]], directions: cycle
) -> dict[str, int]:
    steps_for_node: dict[str, int] = {}
    _nodes = starting_nodes.copy()
    for n_steps, direction in enumerate(directions):
        if len(steps_for_node) == len(_nodes):
            return steps_for_node

        for node in _nodes:
            if (node not in steps_for_node) and node.endswith("Z"):
                steps_for_node[node] = n_steps

        match direction:
            case "L":
                _nodes = [node_dict[node][0] for node in _nodes]
            case "R":
                _nodes = [node_dict[node][1] for node in _nodes]


def part2_lcm():
    directions = get_directions()
    node_dict = get_node_name_dict()
    nodes: list[str] = [node for node in node_dict if node.endswith("A")]
    n_steps_by_node = get_n_steps_for_each_starting_node(
        starting_nodes=nodes, node_dict=node_dict, directions=directions
    )
    print(n_steps_by_node)
    return reduce(lcm, n_steps_by_node.values())


if __name__ == "__main__":
    print("Part1:")
    n_steps_p1 = part1()
    print(f"Steps needed: {n_steps_p1:d}")

    print("Part2:")
    n_steps_p2 = part2_lcm()
    print(f"Steps needed: {n_steps_p2:d}")
