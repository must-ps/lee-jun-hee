import heapq

def solution(jobs):
    now, total_time = 0, 0
    DURATION, REQ_TIME = 0, 1
    jobs_heap = []
    sorted_jobs = sorted(list(map(lambda x: (x[1], x[0]), jobs)), key=lambda x: x[REQ_TIME], reverse=True)
    while True:
        while sorted_jobs and sorted_jobs[-1][REQ_TIME] <= now:
            runnable_job = sorted_jobs.pop()
            heapq.heappush(jobs_heap, runnable_job)
        if jobs_heap:
            job_to_run = heapq.heappop(jobs_heap)
            now += job_to_run[DURATION]
            total_time += now - job_to_run[REQ_TIME]
        elif not sorted_jobs:
            break
        else:
            now += 1
    return total_time // len(jobs)
