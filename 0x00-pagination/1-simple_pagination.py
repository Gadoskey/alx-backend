#!/usr/bin/env python3
"""
Author: Gadoskey

File: 1-simple_pagination.py

Description: A Python method named get_page that takes
two integer arguments page with default value 1
and page_size with default value 10.
"""

import csv
import math
from typing import List, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a page of dataset."""
        # Assert both arguments are integers greater than 0
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        # If the range is out of bounds, return an empty list
        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]
