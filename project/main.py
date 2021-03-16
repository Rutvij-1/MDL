import client
import random
import json
import numpy as np

POPULATION_SIZE = 10
GENERATIONS = 9
MIN = -10.0
MAX = 10.0
MUTATION_PROB = 0.7
MAX_MUTATE = 1000
MIN_MUTATE = 100
ORIGINAL_ERROR = 381807315968.0
MATING_POOL_SIZE = 10
BEST_PARENTS = 3
TRAIN_FACTOR = 0.95
TEST_FACTOR = 1.0
DIFF_FACTOR = 1.0
VAR_PERCENTAGE = 25
POWER_FACTOR = 3


# For each weight of the vector, it is changed with given probability.
# In case the weight is 0, it is assigned a random value in given range.
def mutate(vector, num=1, prob=MUTATION_PROB, perc=VAR_PERCENTAGE):
    vector = vector.copy()
    for _ in range(num):
        for i in range(len(vector)):
            if random.random() <= prob:
                if vector[i] == 0.0:
                    vector[i] = random.uniform(MIN, MAX)
                else:
                    val = random.uniform(
                        1.0 - (perc / 100), 1.0 + (perc / 100))
                    val *= vector[i]
                    val = max(val, -10.0)
                    val = min(val, 10.0)
                    vector[i] = val
    return vector


# With a power factor, randomised weight factors are calculated.
# By adding parents multiplied by these weight factors, 2 child vectors are calculated from the parent vectors
def binary_crossover(a, b, nc=POWER_FACTOR):
    if len(a) != len(b):
        return a, b
    p = random.random()
    if p <= 0.5:
        b = (p * 2) ** (1.0 / (nc + 1))
    else:
        b = (1.0 / ((1.0 - p) * 2)) ** (1.0 / (nc + 1))
    na = np.array(a, dtype="float_")
    nb = np.array(b, dtype="float_")
    nchild1 = (na * (1 + b) + nb * (1 - b)) * 0.5
    nchild2 = (na * (1 - b) + nb * (1 + b)) * 0.5
    return list(nchild1), list(nchild2)


# Randomly choose a position and swap all weights after that position
def single_point_crossover(a, b):
    if len(a) != len(b) or len(a) < 2:
        return a, b
    p = random.randint(0, len(a) - 1)
    return a[:p] + b[p:], b[:p] + a[p:]


# For all weights, swap them with given probability
def uniform_crossover(a, b, prob=0.5):
    if len(a) != len(b):
        return a, b
    a = a.copy()
    b = b.copy()
    for i in range(len(a)):
        if random.random() <= prob:
            a[i], b[i] = b[i], a[i]
    return a, b


# In a population of vectors with decreasing fitness, for position, select the element with given weights.
def selection_crossover(population, weights):
    vector = []
    for i in range(len(population[0])):
        pos = random.choices(list(range(len(population))),
                             weights=weights, k=1)[0]
        vector.append(population[pos][i])
    return vector.copy()


# Get fitness value from training set and testing set MSEs
def fitness_value(errors):
    return 1.0 / abs(
        (errors[0] * TRAIN_FACTOR)
        + (errors[1] * TEST_FACTOR)
        + (abs(errors[0] - errors[1]) * DIFF_FACTOR)
    )


# Get error tuple for a vector from server
def vector_errors(vector):
    team_id = "w6zmexNbwRHCKVKxAjTMN7kU4SOsMsoXL5cEAZKoHfvi0F0tvY"
    errors = client.get_errors(team_id, vector)
    return errors


# Get list of error tuples, given the population
def get_error_tuples(population):
    return [vector_errors(vector).copy() for vector in population]


# Select a population of given size, with gievn weights with repitition
def select_new_population(old_population, fitness_list, k=POPULATION_SIZE):
    weights = [(100.0 - ((x / sum(fitness_list)) * 100)) for x in fitness_list]
    return random.choices(population=old_population, weights=weights, k=k)


# Select a population of given size, with gievn weights without repitition
def select_unique_population(old_population, fitness_list, k=POPULATION_SIZE):
    weights = [(100.0 - ((x / sum(fitness_list)) * 100)) for x in fitness_list]
    population = old_population.copy()
    ans = []
    for _ in range(k):
        p = random.choices(
            population=list(range(len(population))), weights=weights, k=1
        )[0]
        ans.append(population[p])
        population.pop(p)
        weights.pop(p)
    return ans


# Select a pair from population with gievn weights with repitition
def select_pair(population, fitness_list):
    return select_new_population(population, fitness_list, k=2)


# Sort the population, fitness array and the error tuple array in decreasing order of fitness
def sort_population(population, fitness_list, error_tuples):
    def fitness_weight(e):
        return fitness_list[e]

    pos = list(range(len(population)))
    pos.sort(key=fitness_weight, reverse=True)
    final_population = population.copy()
    final_fitness = fitness_list.copy()
    final_errors = error_tuples.copy()
    for i in range(len(population)):
        final_population[i] = population[pos[i]].copy()
        final_fitness[i] = fitness_list[pos[i]]
        final_errors[i] = error_tuples[pos[i]].copy()
    return final_population, final_fitness, final_errors


# Create a population from previous generation data, or the overfit vector.
# Note that if flag is True, then error tuples should be calculated to begin with.
def populate(size=POPULATION_SIZE):
    try:
        coefficients = json.load(open("population.txt", "r"))
        population = []
        best_vector = []
        error_tuples = []
        min_error = 1.0e18
        flag = False
        for vector_str, errors in coefficients.items():
            vector = [float(x) for x in vector_str.strip("][").split(", ")]
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
                mutate(
                    best_vector.copy(),
                    num=random.randint(MIN_MUTATE, MAX_MUTATE),
                    prob=1.0,
                )
            )
            error_tuples.append([1e41, 1e41])
            flag = True
        return population, error_tuples, flag
    except IOError:
        overfit_vector = [
            float(x) for x in open(r"overfit.txt", "r").read().strip("[]\n").split(", ")
        ]
        population = []
        error_tuples = [[1e41, 1e41] for _ in range(size)]
        population.append(overfit_vector)
        while len(population) < size:
            population.append(
                mutate(
                    overfit_vector.copy(),
                    num=random.randint(MIN_MUTATE, MAX_MUTATE),
                    prob=1.0,
                )
            )
        return population, error_tuples, True


# Get dictionary mapping of vector string to it's error tuple
def get_coefficients(population, error_tuples):
    coefficients = {}
    for i in range(len(population)):
        coefficients[str(population[i])] = error_tuples[i]
    return coefficients


# Get the next generation from the previous one.
# Here we first choose n with some weights.
# Then choose n vectors from population. And perform a selection cross over on it(Refer the function to know what it is).
# Mutate the resulting vector and add it to the next generation.
# Then add some of the best parents to it.
# This forms the new generation.
def get_next_gen(population, fitness_array, no_of_parents=BEST_PARENTS):
    next_gen = []
    weight_list = [
        [0.6, 0.4],
        [0.5, 0.3, 0.2],
        [0.45, 0.25, 0.15, 0.15],
    ]
    for _ in range(POPULATION_SIZE):
        n = random.choices(population=[2, 3, 4], weights=[
                           0.35, 0.45, 0.2], k=1)[0]
        posarr = select_unique_population(
            list(range(POPULATION_SIZE)), fitness_array, k=n
        )
        posarr.sort()
        pool = [population[x].copy() for x in posarr]
        next_gen.append(mutate(selection_crossover(
            pool, weight_list[n - 2])).copy())
    next_gen += population[:no_of_parents].copy()
    return next_gen.copy()


# Get population from file.
# Then in the genrations, get their errors, sort them, resize all, print them and then get new generation.
# Finally we store the generation data to file.
if __name__ == "__main__":
    population, error_tuples, flag = populate()
    # # ------------------Testing Code-------------------
    # fitness_array = [fitness_value(error) for error in error_tuples]
    # population, fitness_array, error_tuples = sort_population(
    #     population, fitness_array, error_tuples)
    # population = population[:POPULATION_SIZE]
    # fitness_array = fitness_array[:POPULATION_SIZE]
    # error_tuples = error_tuples[:POPULATION_SIZE]
    # for vector, error in get_coefficients(population, error_tuples).items():
    #     print(vector, " : ", error)
    # print("Best = ", error_tuples[0][0]+error_tuples[0]
    #       [1], " => ", str(population[0]), error_tuples[0])
    # print('')
    # population = get_next_gen(population, fitness_array)
    # error_tuples = [[1e7, 1e7]
    #                 for _ in range(POPULATION_SIZE)] + error_tuples[:BEST_PARENTS]
    # fitness_array = [fitness_value(error) for error in error_tuples]
    # population, fitness_array, error_tuples = sort_population(
    #     population, fitness_array, error_tuples)
    # population = population[:POPULATION_SIZE]
    # fitness_array = fitness_array[:POPULATION_SIZE]
    # error_tuples = error_tuples[:POPULATION_SIZE]
    # for vector, error in get_coefficients(population, error_tuples).items():
    #     print(vector, " : ", error)
    # print("Best = ", error_tuples[0][0]+error_tuples[0]
    #       [1], " => ", str(population[0]), error_tuples[0])
    # print('')
    # # -------------Testing Code Ends-----------------
    first = True
    if flag:
        GENERATIONS -= 1
    for _ in range(GENERATIONS):
        if flag:
            if first:
                error_tuples = get_error_tuples(population)
            else:
                error_tuples = (
                    get_error_tuples(population[:POPULATION_SIZE]).copy()
                    + error_tuples[:BEST_PARENTS]
                )
        flag = True
        first = False
        fitness_array = [fitness_value(error) for error in error_tuples]
        population, fitness_array, error_tuples = sort_population(
            population, fitness_array, error_tuples
        )
        population = population[:POPULATION_SIZE]
        fitness_array = fitness_array[:POPULATION_SIZE]
        error_tuples = error_tuples[:POPULATION_SIZE]
        print("Generation ", _, ":")
        for vector, error in get_coefficients(population, error_tuples).items():
            print(vector, " : ", error)
        print(
            "Best = ",
            error_tuples[0][0] + error_tuples[0][1],
            " => ",
            str(population[0]),
            error_tuples[0],
        )
        print("")
        population = get_next_gen(population, fitness_array)
    error_tuples = (
        get_error_tuples(population[:POPULATION_SIZE]).copy()
        + error_tuples[:BEST_PARENTS]
    )
    fitness_array = [fitness_value(error) for error in error_tuples]
    population, fitness_array, error_tuples = sort_population(
        population, fitness_array, error_tuples
    )
    population = population[:POPULATION_SIZE]
    print("Generation ", GENERATIONS, ":")
    for vector, error in get_coefficients(population, error_tuples).items():
        print(vector, " : ", error)
    print(
        "Final Best = ",
        error_tuples[0][0] + error_tuples[0][1],
        " => ",
        str(population[0]),
        error_tuples[0],
    )
    json.dump(get_coefficients(population, error_tuples),
              open("population.txt", "w"))
