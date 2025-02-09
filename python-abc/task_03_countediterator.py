#!/usr/bin/python3
from abc import ABC, abstractmethod


class CountedIterator(ABC):
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        return (self.counter)

    def __next__(self):
        try:
            item = next(self.iterator)
            self.counter += 1
            return (item)
        except StopIteration:
            raise StopIteration
