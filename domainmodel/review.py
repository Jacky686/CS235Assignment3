from datetime import datetime

from domainmodel.movie import Movie


class Review:

    def __init__(self, movie: Movie, review_text: str, rating: int):
        if type(movie) == Movie:
            self.__movie = movie
        else:
            self.__movie = None

        if review_text == "" or type(review_text) is not str:
            self.__review_text = None
        else:
            self.__review_text = review_text

        if 1 <= rating <= 10 and type(rating) == int:
            self.__rating = rating
        else:
            self.__rating = None

        self.__timestamp = datetime.now()

    @property
    def movie(self) -> Movie:
        return self.__movie

    @property
    def review_text(self) -> str:
        return self.__review_text

    @property
    def rating (self) -> str:
        return self.__rating

    @property
    def timestamp(self) -> datetime:
        return self.__timestamp

    def __repr__(self):
        return f"<Review {self.__movie}, {self.__review_text}, {self.__rating}>"

    def __eq__(self, other):
        if self.__movie == other.movie and \
                self.__review_text == other.review_text and \
                self.__rating == other.rating and \
                self.__timestamp == other.__timestamp:
            return True

        return False


class TestReview:

    def test_init(self):
        pass
        # movie = Movie("Moana", 2016)
        # review_text = "This movie was very enjoyable."
        # rating = 8
        # review = Review(movie, review_text, rating)
        #
        # review1 = Review(movie, review_text, rating)
        #
        # print(review == review1)
        # print(review)
        # print(review.movie)
        # print("Review: {}".format(review.review_text))
        # print("Rating: {}".format(review.rating))
