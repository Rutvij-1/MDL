import client
import numpy as np
import random
import sys

POPULATION_SIZE = 8
GENERATIONS = 7
MIN = -10.0
MAX = 10.0
MUTATION_PROB = 0.4
MAX_MUTATE = 1000
MIN_MUTATE = 10
ORIGINAL_FITNESS = 381807315968.0
BEST_FITNESS = 343841643520.0
BEST_FITNESS_VECTOR = np.array([0.00000000e+00, -1.45799022e-12, -6.45215453e+00, -2.18641775e+00,
                                -1.75214813e-10, -1.83669770e-15,  8.52944060e-16,  2.29423303e-05,
                                -2.04721003e-06, -1.59792834e-08,  9.98214034e-10], dtype='float_')


def mutate(vector, num=1, prob=MUTATION_PROB):
    temp_vector = vector.copy()
    for _ in range(num):
        i = random.randint(0, temp_vector.shape[0]-1)
        if random.random() <= prob:
            temp_vector[i] = random.uniform(MIN, MAX)
    return temp_vector


def crossover(a, b):
    list_a = list(a)
    list_b = list(b)
    if len(list_a) != len(list_b) or len(list_a) < 2:
        return a, b
    p = random.randint(1, len(list_a)-1)
    return np.array(list_a[0:p]+list_b[p:], dtype='float_'), np.array(list_b[0:p]+list_a[p:], dtype='float_')


def fitness(vector):
    team_id = 'w6zmexNbwRHCKVKxAjTMN7kU4SOsMsoXL5cEAZKoHfvi0F0tvY'
    errors = client.get_errors(team_id, list(vector))
    return float(sys.maxsize - errors[0] - errors[1])


def get_fitness_list(population):
    return [fitness(vector) for vector in population]


def select_pair(population, fitness_list):
    return random.choices(population=population, weights=fitness_list, k=2)


def sort_population(population, fitness_list):
    def fitness_weight(e):
        return fitness_list[e]
    pos = list(range(len(population)))
    pos.sort(key=fitness_weight, reverse=True)
    final_population = population.copy()
    final_fitness = fitness_list
    for i in range(len(population)):
        final_population[i] = population[pos[i]].copy()
        final_fitness[i] = fitness_list[pos[i]]
    return final_population, final_fitness


def populate(vector, size=POPULATION_SIZE):
    return [vector] + [mutate(vector, num=random.randint(MIN_MUTATE, MAX_MUTATE)) for _ in range(size-1)]


def get_overfit_vector():
    overfit_vector_file = open(r"overfit.txt", "r")
    for line in overfit_vector_file:
        return np.array(line[1:-2].split(', '), dtype='float_')


if __name__ == "__main__":
    population = populate(get_overfit_vector())
    for _ in range(GENERATIONS):
        fitness_array = get_fitness_list(population)
        population, fitness_array = sort_population(population, fitness_array)
        print(population)

        next_gen = population[0:2]
        for __ in range(int(POPULATION_SIZE / 2) - 1):
            parents = select_pair(population, fitness_array)
            child_a, child_b = crossover(parents[0], parents[1])
            child_a = mutate(child_a, num=3)
            child_b = mutate(child_b, num=3)
            next_gen += [child_a, child_b]
        population = next_gen.copy()
    fitness_array = get_fitness_list(population)
    population, fitness_array = sort_population(population, fitness_array)
    print(population)
    print(sys.maxsize - fitness_array[0])
    if (sys.maxsize - fitness_array[0]) < BEST_FITNESS:
        BEST_FITNESS = sys.maxsize - fitness_array[0]
        BEST_FITNESS_VECTOR = population[0]
    print(ORIGINAL_FITNESS)
    print(BEST_FITNESS)
    first = True
    for ele in BEST_FITNESS_VECTOR:
        if first:
            print(f'[{ele}', end='')
            first = False
        else:
            print(f', {ele}', end='')
    print(']')
