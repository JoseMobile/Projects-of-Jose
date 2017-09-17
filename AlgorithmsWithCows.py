

from ps1_partition import get_partitions
import time



def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cow_select = []
    sorted_cows = (sorted(cows, key = cows.get, reverse = True))

    sorted_cows1 = sorted_cows.copy()
    
    while True:
        ship = []# new ship
        
        if sorted_cows1 == [] or cows[sorted_cows1[-1]] > limit:
            return cow_select
        else:
            weight = 0
            for cow in sorted_cows:
                
                if weight + cows[sorted_cows[-1]] > limit:
                    break     
                elif ship == [] or cows[cow] + weight <= limit:
                    ship.append(cow)
                    weight += cows[cow]
                    sorted_cows1.remove(cow)
                   
                     
            if ship != []:
                
                cow_select.append(ship)
           
            sorted_cows = sorted_cows1[:]


def ship_weight(cows, ship):
    weight = 0
    for cow in ship:
        weight += cows[cow]
    return weight

def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    a = cows.keys()
    cow_list = list(a)
    combo_list = []
    feasible = []
    for combo in (get_partitions(cow_list)):
        combo_list.append(combo)
    for combo in combo_list:
        valid_combo = True
        for ship in combo: 
            if ship_weight(cows,ship) > limit:
                valid_combo = False
                break
            else:
                pass
        if valid_combo:
            feasible.append((len(combo), combo))
    sorted_list = sorted(feasible, key = lambda tup: tup[0])
    return sorted_list[0][1]


        

def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    start = time.time()
    greedy_cow_transport(cows, 50)
    end = time.time()
    print(end - start, 'greedy algorithm time')
    start = time.time()
    brute_force_cow_transport(cows, 50)
    end = time.time()
    print(end - start, 'brute_force algorithm time')


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=100
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))
print(compare_cow_transport_algorithms())

