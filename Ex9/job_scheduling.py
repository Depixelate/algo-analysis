class DSUNode:
    def __init__(self, val: int):
        self.rep = self
        self.rank = 0
        self.first_empty = val
        self.val = val


def get_rep(elem):
    if elem != elem.rep:
        elem.rep = get_rep(elem.rep)
    return elem.rep


def union(elem1, elem2):
    rep1, rep2 = get_rep(elem1), get_rep(elem2)
    if rep1.rank > rep2.rank:
        rep2.rep = rep1
    else:
        rep1.rep = rep2
        if rep1.rank == rep2.rank:
            rep2.rank += 1
    rep1.rep.first_empty = min(rep1.first_empty, rep2.first_empty)
    return rep1.rep


def same_set(elem1, elem2):
    return get_rep(elem1) == get_rep(elem2)


def get_and_dec(rep):
    rep.first_empty -= 1
    return rep.first_empty


class Job:
    def __init__(self, name, profit, deadline):
        self.name = name
        self.profit = profit
        self.deadline = deadline

    def __str__(self):
        return f"Job{self.name:02}"


def get_job_index(schedule, deadline):
    rep = get_rep(deadline)
    while True:
        index = get_and_dec(rep)
        if index < 0:
            return index
        if schedule[index] is None:
            return index
        other = schedule[index].deadline
        rep = union(other, rep)

def compress(schedule):
    compressed_schedule = []
    for job in schedule:
        if job is None:
            continue
        compressed_schedule.append(job)
    return compressed_schedule


def job_scheduler(jobs: list[Job]):
    last_deadline = max(jobs, key=lambda job: job.deadline.val).deadline.val
    schedule = [None for i in range(last_deadline)]
    jobs.sort(key=lambda job: job.profit, reverse=True)
    for job in jobs:
        index = get_job_index(schedule, job.deadline)
        if index < 0:
            continue
        schedule[index] = job

    return compress(schedule)


if __name__ == "__main__":
    num_jobs = int(input("Enter how many jobs you want to schedule: "))
    jobs = []
    for i in range(num_jobs):
        profit = float(input(f"Enter the profit for job {i+1}: "))
        deadline = DSUNode(int(input(f"Enter the deadline for job {i + 1}: ")))
        name = i + 1
        jobs.append(Job(name, profit, deadline))

    schedule = job_scheduler(jobs)
    print()
    for i in range(len(schedule)):
        print(f"{i:02}-{i+1:02}", end="  ")
    print()
    for job in schedule:
        if job is None:
            print("Empty", end= "  ")
            continue
        print(job, end="  ")
    print()
