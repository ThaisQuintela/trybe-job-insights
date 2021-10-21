from src.jobs import read


def get_unique(key, path):
    """Get a list of unique values from a list of dicts"""
    list = read(path)
    return set(item[key]
               for item in list
               if item[key] != "" and item[key] != "invalid")


def filter_by_category(key, category, jobs):
    """Get a list of all entries from a specific category"""
    return [job for job in jobs if job[key] == category]


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them"""
    return get_unique("job_type", path)


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type"""
    return filter_by_category("job_type", job_type, jobs)


def get_unique_industries(path):
    """Checks all different industries and returns a list of them"""
    return get_unique("industry", path)


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry"""
    return filter_by_category("industry", industry, jobs)


def get_max_salary(path):
    """Get the maximum salary of all jobs"""
    salary_list = get_unique("max_salary", path)
    return max([int(salary) for salary in salary_list])


def get_min_salary(path):
    """Get the minimum salary of all jobs"""
    salary_list = get_unique("min_salary", path)
    return min([int(salary) for salary in salary_list])


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job"""
    if (type(salary) != int
            or "min_salary" not in job
            or "max_salary" not in job
            or type(job["min_salary"]) != int
            or type(job["max_salary"]) != int
            or job["min_salary"] > job["max_salary"]):
        raise ValueError("Value Error")
    return (job["min_salary"] <= salary <= job["max_salary"])


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range"""
    return [job for job in jobs
            if type(salary) == int
            and job["min_salary"] < job["max_salary"]
            and matches_salary_range(job, salary) is True]
