import random


class Chromosome(object):
    """
    Based on
    M. D. Pierro, Annotated Algorithms in Python with Applications in Physics, Biology, and Finance,
    ISBN 978-89-6540-105-6.
    """
    alphabet = 'ATGC'
    size = 32
    mutations = 2

    # methods
    def __init__(self, father=None, mother=None):
        if not father or not mother:
            self.dna = [random.choice(self.alphabet) for i in range(self.size)]
        else:
            father_half = father.dna[0:(self.size // 2)]
            mother_half = mother.dna[(self.size // 2):]
            self.dna = father_half + mother_half
            for mutation in range(self.mutations):
                self.dna[random.randint(0, self.size - 1)] = random.choice(self.alphabet)

    def fitness(self, target):
        ones_list = [1 for i, c in enumerate(self.dna) if c == target.dna[i]]
        result = sum(ones_list)
        return result

    def __lt__(self, other):
        return self.dna.__lt__(other.dna)


def top(population, target, n=10):
    table = [(chromo.fitness(target), chromo) for chromo in population]
    table.sort(reverse=True)
    return [row[1] for row in table][:n]


def oneof(population):
    return population[random.randint(0, len(population) - 1)]


def main():
    GENERATIONS = 10000
    OFFSPRING = 20
    SEEDS = 20
    TARGET = Chromosome()

    population = [Chromosome() for i in range(SEEDS)]
    for i in range(GENERATIONS):
        print('\n\nGENERATION:', i)
        print(0, TARGET.dna)
        fittest = top(population, TARGET)

        for chromosome in fittest:
            print(i, chromosome.dna)

        if max(chromo.fitness(TARGET) for chromo in fittest) == Chromosome.size:
            print('SOLUTION FOUND')
            break

        population = [Chromosome(father=oneof(fittest),
                                 mother=oneof(fittest))
                      for i in range(OFFSPRING)]


if __name__ == '__main__':
    main()
