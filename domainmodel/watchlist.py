from domainmodel.movie import Movie
from typing import List


class WatchList:

    def __init__(self):
        self.__watch_list: List[Movie] = list()

    @property
    def watch_list(self) -> List[Movie]:
        return self.__watch_list

    def add_movie(self, movie):
        if isinstance(movie, Movie) and movie not in self.__watch_list:
            self.__watch_list.append(movie)

    def remove_movie(self, movie):
        if isinstance(movie, Movie) and movie in self.__watch_list:
            self.__watch_list.remove(movie)

    def select_movie_to_watch(self, index):
        if 0 <= index < len(self.__watch_list):
            return self.__watch_list[index]
        else:
            return None

    def size(self):
        return len(self.__watch_list)

    def first_movie_in_watchlist(self):
        if self.__watch_list:
            return self.__watch_list[0]
        else:
            return None

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < self.size():
            temp_i = self.i
            self.i += 1
            return self.__watch_list[temp_i]
        else:
            raise StopIteration
