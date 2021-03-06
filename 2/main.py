import client
import numpy as np
import random
import sys
import json
import math

POPULATION_SIZE = 10
GENERATIONS = 8
MIN = -10.0
MAX = 10.0
MUTATION_PROB = 0.5
MAX_MUTATE = 1000
MIN_MUTATE = 100
ORIGINAL_FITNESS = 381807315968.0
MATING_POOL_SIZE = 2
BEST_PARENTS = 4
TRAIN_FACTOR = 1.0
TEST_FACTOR = 1.0
POWER_FACTOR = 3


def mutate(vector, num=1, prob=MUTATION_PROB):
    for _ in range(num):
        for i in range(len(vector)):
            if random.random() <= prob:
                val = random.uniform(0.9, 1.1)
                val *= vector[i]
                val = max(val, -10.0)
                val = min(val, 10.0)
                vector[i] = val
    return vector


def single_point_crossover(a, b):
    if len(a) != len(b) or len(a) < 2:
        return a, b
    p = random.randint(0, len(a)-1)
    return a[:p]+b[p:], b[:p]+a[p:]


def binary_crossover(a, b, nc=POWER_FACTOR):
    if len(a) != len(b):
        return a, b
    p = random.random()
    if p <= 0.5:
        b = (p * 2)**(1.0 / (nc + 1))
    else:
        b = (1.0 / ((1.0 - p) * 2))**(1.0 / (nc + 1))
    na = np.array(a, dtype='float_')
    nb = np.array(b, dtype='float_')
    nchild1 = (na * (1 + b) + nb * (1 - b)) * 0.5
    nchild2 = (na * (1 - b) + nb * (1 + b)) * 0.5
    return list(nchild1), list(nchild2)


def fitness_value(errors):
    return 1.0 / ((errors[0] * TRAIN_FACTOR) + (errors[1] * TEST_FACTOR))


def vector_errors(vector):
    team_id = 'w6zmexNbwRHCKVKxAjTMN7kU4SOsMsoXL5cEAZKoHfvi0F0tvY'
    errors = client.get_errors(team_id, vector)
    return errors


def get_fitness_list(population):
    return [fitness_value(vector_errors(vector)) for vector in population]


def get_error_tuples(population):
    return [vector_errors(vector).copy() for vector in population]


def select_new_population(old_population, fitness_list, k=POPULATION_SIZE):
    weights = [(100.0 - ((x / sum(fitness_list)) * 100)) for x in fitness_list]
    return random.choices(population=old_population, weights=weights, k=k)


def select_pair(population, fitness_list):
    return select_new_population(population, fitness_list, k=2)


def sort_population(population, fitness_list, error_tuples):
    def fitness_weight(e):
        return fitness_list[e]
    pos = list(range(len(population)))
    pos.sort(key=fitness_weight, reverse=True)
    final_population = population.copy()
    final_fitness = fitness_list
    final_errors = error_tuples
    for i in range(len(population)):
        final_population[i] = population[pos[i]].copy()
        final_fitness[i] = fitness_list[pos[i]]
        final_errors[i] = error_tuples[pos[i]].copy()
    return final_population, final_fitness, final_errors


def populate(size=POPULATION_SIZE):
    try:
        coefficients = json.load(open("population.txt", 'r'))
        population = []
        best_vector = []
        error_tuples = []
        min_error = 1.0e+18
        flag = False
        for vector_str, errors in coefficients.items():
            vector = [float(x) for x in vector_str.strip('][').split(', ')]
            if errors[0] + errors[1] < min_error:
                min_error = errors[0] + errors[1]
                best_vector = vector.copy()
            population.append(vector)
            if len(errors) == 2:
                error_tuples.append(errors)
            else:
                error_tuples.append([1e41, 1e41])
            if len(population) >= size:
                break
        while len(population) < size:
            population.append(
                mutate(best_vector.copy(), num=random.randint(MIN_MUTATE, MAX_MUTATE), prob=1.0))
            error_tuples.append([1e41, 1e41])
            flag = True
        return population, error_tuples, flag
    except IOError:
        overfit_vector = [float(x) for x in open(r"overfit.txt",
                                                 "r").read().strip('[]\n').split(', ')]
        population = []
        error_tuples = [[1e41, 1e41] for _ in range(size)]
        population.append(overfit_vector)
        while len(population) < size:
            population.append(
                mutate(overfit_vector.copy(), num=random.randint(MIN_MUTATE, MAX_MUTATE), prob=1.0))
        return population, error_tuples, True


def get_coefficients(population, error_tuples):
    coefficients = {}
    for i in range(len(population)):
        coefficients[str(population[i])] = error_tuples[i]
    return coefficients


def get_next_gen(population, fitness_array, pool_size=MATING_POOL_SIZE, no_of_parents=BEST_PARENTS):
    parents = population[:no_of_parents]
    next_gen = parents.copy()
    for _ in range(math.ceil((POPULATION_SIZE - pool_size) / 2)):
        children = select_pair(
            population[:pool_size], fitness_array[:pool_size])
        children[0], children[1] = single_point_crossover(
            children[0], children[1])
        children[0] = mutate(children[0])
        children[1] = mutate(children[1])
        next_gen += children.copy()
    if len(next_gen) > POPULATION_SIZE:
        next_gen = next_gen[:POPULATION_SIZE]
    return next_gen


if __name__ == "__main__":
    population, error_tuples, flag = populate()
    for _ in range(GENERATIONS):
        if flag:
            GENERATIONS -= 1
            error_tuples = get_error_tuples(population)
        flag = True
        fitness_array = [fitness_value(error) for error in error_tuples]
        population, fitness_array, error_tuples = sort_population(
            population, fitness_array, error_tuples)
        print("Generation ", _, ":")
        for vector, error in get_coefficients(population, error_tuples).items():
            print(vector, " : ", error)
        print("Best = ", error_tuples[0][0]+error_tuples[0]
              [1], " => ", str(population[0]), error_tuples[0])
        print('')
        population = get_next_gen(population, fitness_array)
    error_tuples = get_error_tuples(population)
    fitness_array = [fitness_value(error) for error in error_tuples]
    population, fitness_array, error_tuples = sort_population(
        population, fitness_array, error_tuples)
    print("Generation ", GENERATIONS, ":")
    for vector, error in get_coefficients(population, error_tuples).items():
        print(vector, " : ", error)
    print("Final Best = ", error_tuples[0][0]+error_tuples[0]
          [1], " => ", str(population[0]), error_tuples[0])
    json.dump(get_coefficients(population, error_tuples),
              open("population.txt", 'w'))
