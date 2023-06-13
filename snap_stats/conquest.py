from aoc_utils import * # type: ignore

# State = (
# Number of Proving Grounds wins
# Number of first Silver wins
# Number of second Silver wins
# Number of first Gold wins
# Number of second Gold wins
# Number of third Gold wins
# Number of first Infinity wins
# Number of second Infinity wins
# Number of third Infinity wins
# Number of fourth Infinity wins
# Number of fifth Infinity wins
# Match Number
# )

TARGET=1550

def medals(state):
    p1, s1, s2, g1, g2, g3, i1, i2, i3, i4, i5, _ = state
    return 35*p1 + 40*s1 + 100*s2 + 80*g1 + 100*g2 + 250*g3 + 150*i1 + 175*i2 + 200*i3 + 250*i4 + 500*i5

def neighbours(state):
    game = state[-1]
    # Won the game
    yield state[:game] + (state[game]+1,) + state[game+1:-1] + ((game+1) % 11, )
    # Lost the game
    yield state[:-1] + (0,)

combos = set()

def visit(state):
    m = medals(state)
    cont = m < TARGET
    if not cont:
        combos.add((m, state[:-1]))
    return cont

# Find all combinations of conquest wins that give you at least 1550 medals
# Assumes you stop playing the game as soon as you cross the TARGET treshold
# Assumes you use all tickets that you earn even if you don't get any wins from that brakcet
if __name__ == '__main__':
    graph = UnweightedLazyGraph(neighbours)
    graph.bfs(
      (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
      visit
    )
    import csv
    with open('combos.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Medals', 'Proving Grounds', 'Silver 1', 'Silver 2', 'Gold 1', 'Gold 2', 'Gold 3', 'Infinity 1', 'Infinity 2', 'Infinity 3', 'Infinity 4', 'Infinity 5'])
        for m, state in sorted(combos, key=lambda ms: (ms[0], tuple(reversed(ms[1])))):
            p1, s1, s2, g1, g2, g3, i1, i2, i3, i4, i5 = state
            writer.writerow([m, p1, s1, s2, g1, g2, g3, i1, i2, i3, i4, i5])
