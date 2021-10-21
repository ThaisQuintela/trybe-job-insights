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
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


def get_max_salary(path):
    """Get the maximum salary of all jobs"""
    salary_list = get_unique("max_salary", path)
    return max([int(salary) for salary in salary_list])


def get_min_salary(path):
    """Get the minimum salary of all jobs"""
    salary_list = get_unique("min_salary", path)
    return min([int(salary) for salary in salary_list])


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
