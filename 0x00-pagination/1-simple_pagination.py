#!/usr/bin/env python3
"""
This defines a python class 'Server'
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    returns a tuple of size two containing a
    start index and an end index corresponding
    to the range of indexes to return in a list
    for those particular pagination parameters
    """
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        returns the specified pages
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        pages = index_range(page, page_size)
        pages = [x for x in range(pages[0], pages[1])]
        dataset = self.dataset()
        if page >= len(dataset):
            return []
        counter = 0
        pages_to_return = []
        for i in range(len(dataset)):
            if counter in pages:
                pages_to_return.append(dataset[i])
            counter += 1

        return pages_to_return
