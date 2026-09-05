# Recursive Algorithms & Backtracking Problem Solving (Python)

A collection of pure recursive problem-solving algorithms in Python exploring state-space search, boolean toggle graphs, combinatorial subset sum partitioning, and recursive dictionary string evaluation under strict zero-loop / minimal-loop algorithmic constraints.

## Core Problem Modules

### 1. Toggle Switch Lightbulb Solver (`lightbulb_solver`)
- Models an array of toggles where flipping switch `i` inverts the state of bulb `i` and its immediate adjacent neighbors (`i-1`, `i+1`).
- `lightbulb_solver(lightbulb_array, target_array)`: Pure recursive decision tree exploring state transformations to assert reachability from an initial boolean array to a target array.
- `lightbulb_solver_with_steps(lightbulb_array, target_array)`: Backtracking search tracing and returning the optimal ascending sequence of switch indices used to attain the target state (or `[-1]` if unreachable).

### 2. Extended Pancake Target-Sum Partitioning (`divide_pancakes_extended`)
- Solves a combinatorial subset-sum bin-packing variant maximizing the count of disjoint pancake subsets that each sum to an exact target weight (`total_size`).
- Explores exponential combination trees to greedily maximize recipient partitions without element reuse.

### 3. Maximum-Score Word Synthesizer (`create_word`)
- Evaluates an available pool of character cards (`cards`) against a scored dictionary (`words`).
- Recursively matches card frequency constraints against lexical candidates to extract the highest-scoring valid word.

## Algorithmic Constraints & Code Design
- Zero-Loop Mandate: Implemented without `for`, `while`, list comprehensions, or sorting utilities (except where explicitly single-loop bounded).
- Wrapper Function Paradigm: Employs idiomatic wrapper functions passing explicit recursive states and defensive list clones without relying on default arguments.

## Requirements
- Python 3.8 or higher.

## Verification
Run tests or execution driver:
python hw4.py
