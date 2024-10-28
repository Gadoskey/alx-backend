#!/usr/bin/env python3
"""
Author: Gadoskey

File: 0-simple_helper_function.py

Description: A Python function named index_range that takes
two integer arguments page and page_size. The function returns a tuple
of size two containing a start index and an end index corresponding to the
range of indexes to return in a list for those particular pagination parameters.
"""


def index_range(page, page_size):
  """ function index_range that takes two integer arguments page and page_size
  Return: the start_page and page_size
  """
  start_page = (page - 1) * page_size
  return {start_page, page_size}
