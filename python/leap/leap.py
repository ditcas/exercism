def leap_year(year: int) -> bool:
    """
    Given a year, reports True if it is a leap year.
    ```text
    on every year that is evenly divisible by 4
    except every year that is evenly divisible by 100
    unless the year is also evenly divisible by 400
    ```
    """


    return ((year % 4 == 0) & (year % 100 != 0)) | (year % 400 == 0)
