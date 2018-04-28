#!/usr/bin/env python3

import experiments

def experiment_setup(experiment_name, n, w, **config):
    experiments.ensuredir(experiment_name)
    return "{}/{}_n={}_w={}_{}".format(
        experiments.experdir(experiment_name),
        experiment_name,
        n,
        w,
        "_".join(["{}={}".format(k, str(v)) for k, v in config.items()]))

def graphs_interactive_alt():
    # experiments.run_cmd("cargo build --release --bin graphs-interactive-alt")

    experiment_name = "graphs-interactive-alt"

    experiments.eprint("### {} ###".format(experiment_name))
    experiments.eprint(experiments.experdir(experiment_name))

    for w in reversed([1, 2, 4, 8, 16, 31]):
        for nodes in [10000000]:
            for edges in [32000000]:
                for rate in [2500 * x for x in [2, 4, 8]]:
                    for goal in [5]:
                        for queries in [0, 10, 100, 1000]:
                            for shared in ["no", "shared"]:
                                for bidijkstra in ["no", "bidijkstra"]:
                                    config = {
                                        "nodes": nodes,
                                        "edges": edges,
                                        "rate": rate,
                                        "goal": goal,
                                        "queries": queries,
                                        "shared": shared,
                                        "bidijkstra": bidijkstra,
                                    }

                                    n = 1

                                    filename = experiment_setup(experiment_name, n, w, **config)
                                    experiments.eprint("RUNNING {}".format(filename))
                                    commands = [
                                            "./target/release/graphs-interactive-alt {} -n {} -p {} -w {}".format(
                                                " ".join(str(x) for x in [nodes, edges, rate, goal, queries, shared, bidijkstra]),
                                                n,
                                                p,
                                                w) for p in range(0, n)]
                                    experiments.eprint("commands: {}".format(commands))
                                    processes = [experiments.run_cmd(command, filename, True) for command in commands]
                                    experiments.waitall(processes)

def graphs_interactive_neu():
    # experiments.run_cmd("cargo build --release --bin graphs-interactive-neu")

    experiment_name = "graphs-interactive-neu"

    experiments.eprint("### {} ###".format(experiment_name))
    experiments.eprint(experiments.experdir(experiment_name))

    for w in reversed([16, 31]):
        for nodes in [10000000]:
            for edges in [32000000]:
                for rate in [1000000]: # + x for x in [-250000, 0, 250000, 500000]]:
                    for goal in [60]:
                        for queries in [1, 10, 1000, 10000, 100000,]: # [0, 1000, 10000, 100000]:
                            for shared in ["no", "shared"]:
                                config = {
                                    "nodes": nodes,
                                    "edges": edges,
                                    "rate": rate,
                                    "goal": goal,
                                    "queries": queries,
                                    "shared": shared,
                                }

                                n = 1

                                filename = experiment_setup(experiment_name, n, w, **config)
                                experiments.eprint("RUNNING {}".format(filename))
                                commands = [
                                        "./target/release/graphs-interactive-neu {} -n {} -p {} -w {}".format(
                                            " ".join(str(x) for x in [nodes, edges, rate, goal, queries, shared]),
                                            n,
                                            p,
                                            w) for p in range(0, n)]
                                experiments.eprint("commands: {}".format(commands))
                                processes = [experiments.run_cmd(command, filename, True) for command in commands]
                                experiments.waitall(processes)
