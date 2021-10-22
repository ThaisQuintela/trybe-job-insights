from src.sorting import sort_by


criteria_list = [
        {
            "min_salary": "0",
            "max_salary": "2000",
            "date_posted": "2021-10-21"
        },
        {
            "min_salary": "2000",
            "max_salary": "4000",
            "date_posted": "2021-10-20"
        },
        {
            "min_salary": "4000",
            "max_salary": "6000",
            "date_posted": "2021-10-19"
        },
        {
            "min_salary": "6000",
            "max_salary": "8000",
            "date_posted": "2021-10-18"
        },
        {
            "min_salary": "500",
            "max_salary": "1500",
            "date_posted": "2021-10-22"
        }
    ]


def test_sort_by_criteria():
    """ Test the 'min_salary' criterion """
    sort_by(criteria_list, "min_salary")
    assert criteria_list == [
        {
            "min_salary": "0",
            "max_salary": "2000",
            "date_posted": "2021-10-21"
        },
        {
            "min_salary": "500",
            "max_salary": "1500",
            "date_posted": "2021-10-22"
        },
        {
            "min_salary": "2000",
            "max_salary": "4000",
            "date_posted": "2021-10-20"
        },
        {
            "min_salary": "4000",
            "max_salary": "6000",
            "date_posted": "2021-10-19"
        },
        {
            "min_salary": "6000",
            "max_salary": "8000",
            "date_posted": "2021-10-18"
        }
    ]

    """ Test the 'max_salary' criterion """
    sort_by(criteria_list, "max_salary")
    assert criteria_list == [
        {
            "min_salary": "6000",
            "max_salary": "8000",
            "date_posted": "2021-10-18"
        },
        {
            "min_salary": "4000",
            "max_salary": "6000",
            "date_posted": "2021-10-19"
        },
        {
            "min_salary": "2000",
            "max_salary": "4000",
            "date_posted": "2021-10-20"
        },
        {
            "min_salary": "0",
            "max_salary": "2000",
            "date_posted": "2021-10-21"
        },
        {
            "min_salary": "500",
            "max_salary": "1500",
            "date_posted": "2021-10-22"
        }
    ]

    """ Test the 'date_posted' criterion """
    sort_by(criteria_list, "date_posted")
    assert criteria_list == [
        {
            "min_salary": "500",
            "max_salary": "1500",
            "date_posted": "2021-10-22"
        },
        {
            "min_salary": "0",
            "max_salary": "2000",
            "date_posted": "2021-10-21"
        },
        {
            "min_salary": "2000",
            "max_salary": "4000",
            "date_posted": "2021-10-20"
        },
        {
            "min_salary": "4000",
            "max_salary": "6000",
            "date_posted": "2021-10-19"
        },
        {
            "min_salary": "6000",
            "max_salary": "8000",
            "date_posted": "2021-10-18"
        }
    ]
