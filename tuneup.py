#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "SmileySlays"

import cProfile
import pstats
import timeit
from functools import wraps


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    # You need to understand how decorators are constructed and used.
    # Be sure to review the lesson material on decorators, they are used
    # extensively in Django and Flask.
    @wraps(func)
    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        value = func(*args, **kwargs)
        pr.disable()
        ps = pstats.Stats(pr).strip_dirs().sort_stats('cumulative')
        ps.print_stats(1)
        return value
    return inner


def read_movies(src):
    """Returns a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """returns True if title is within movies list"""
    for movie in movies:
        if movie.lower() == title.lower():
            return True
    return False


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    movies_dict = {}
    duplicates = []
    for movie in movies:
        if movie in movies_dict:
            movies_dict[movie] += 1
        else:
            movies_dict[movie] = 1
        if movies_dict[movie] > 1:
            duplicates.append(movie)
    return duplicates


def timeit_helper(func):
    """Part A:  Obtain some profiling measurements using timeit"""
    # YOUR CODE GOES HERE
    # timeit.timeit(func()), number=10000)
    t = timeit.Timer(str(func), globals=globals())

    result = t.repeat(repeat=7, number=5)
    print("Best time across 7 repeats"
          "of 5 runs per repeat: " + str(min(result)) + " secs")
    return result


def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))
    # print(find_duplicate_movies("movies.txt"))


if __name__ == '__main__':
    main()
