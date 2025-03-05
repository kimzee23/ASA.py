import unittest
from  movieRating import *

class textMoiveRating(unittest.TestCase):
    def test_add_movie(self):
        result = get_add_movie()
        self.assertEqual(result, 'Inception')

    def test_rating_moive(self):
        result = get_rating_movie()
        self.assertEqual(result, 2.0)
        

"""
    def test_add_movie_is_invalid(self):
        movie = {}
        result = get_add_movie("12--121")
        self.assertEqual(result, "Invalid input. Please enter a valid movie name.")
        self.assertEqual(len(movie),0)
    """
    
    

if __name__== "__main__":
    unittest.main()
