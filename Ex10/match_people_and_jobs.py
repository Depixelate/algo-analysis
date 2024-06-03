import math
def partial_lb(cost, jobs_used, person):
    plb = 0
    n = len(cost)
    for i in range(person, n):
        min_cost = math.inf
        for j in range(n):
            if jobs_used[j]:
                continue
            if cost[i][j] < min_cost:
                min_cost = cost[i][j]
        plb += min_cost
    return plb

min_cost = math.inf
min_match = None
def min_match_helper(cost, person, match, jobs_used, cur_cost):
    global min_cost
    global min_match
    n = len(cost)
    for job in range(n):
        if jobs_used[job]:
            continue
        jobs_used[job] = True
        match[person] = job
        new_cost = cur_cost + cost[person][job]
        new_lb = new_cost + partial_lb(cost, jobs_used, person + 1)
        if new_lb < min_cost:
            if person >= n - 2:
                min_cost = new_lb
                match[n-1] = jobs_used.index(False)
                min_match = list(match)
            else:
                min_match_helper(cost, person + 1, match, jobs_used, new_cost)
        jobs_used[job] = False
    
def min_match(cost):
    n = len(cost)
    min_match_helper(cost, 0, [0 for i in range(n)], [False for i in range(n)], 0)
    return min_cost, min_match

if __name__ == "__main__":
    n = int(input("Enter number of people and jobs: "))
    cost = [eval(input(f"Enter the costs for jobs 1 to {n} for person {i + 1}: ")) for i in range(n)]
    tot_cost, person_to_job = min_match(cost)
    print(f"Total Cost: {tot_cost}")
    print("Matches: ")
    for p, j in enumerate(person_to_job):
        print(f"Person {p+1}: Job {j+1}")


    