#!/usr/bin/env python3
"""
Author: Gadoskey

File: 0-simple_helper_function.py

Description: A Python function named index_range that takes
two integer arguments page and page_size. The function returns a tuple
of size two containing a start index and an end index corresponding to the
range of indexes to return in a list.
"""


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Function index_range that takes two integer arguments: page and page_size.

    Args:
        page (int): The current page number.
        page_size (int): The number of items per page.

    Returns:
        tuple[int, int]: A tuple containing the start index and end index.
    """
    start_page = (page - 1) * page_size
    end_page = start_page + page_size
    return (start_page, end_page)
