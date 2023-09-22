import unittest
from cache_decorator import cache

class TestCacheDecorator(unittest.TestCase):

    def test_cached_results(self):
        # Create an instance of CacheDecorator
        cache_decorator = cache()

        # Define a simple function to be decorated
        @cache_decorator.cache
        def add(a, b):
            return a + b

        # Test the cache with some function calls
        result1 = add(2, 3)
        result2 = add(2, 3)  # This should use the cached result
        result3 = add(4, 5)  # This should not use the cache

        # Check if the results are as expected
        self.assertEqual(result1, 5)
        self.assertEqual(result2, 5)
        self.assertEqual(result3, 9)

    def test_cache_clear(self):
        # Create an instance of CacheDecorator
        cache_decorator = cache()

        # Define a simple function to be decorated
        @cache_decorator.cache
        def multiply(a, b):
            return a * b

        # Test the cache with some function calls
        result1 = multiply(2, 3)
        result2 = multiply(4, 5)

        # Clear the cache
        cache_decorator.clear_cache()

        # Call the function again
        result3 = multiply(2, 3)  # This should not use the cache

        # Check if the results are as expected
        self.assertEqual(result1, 6)
        self.assertEqual(result2, 20)
        self.assertEqual(result3, 6)  # Cache should be cleared, so result3 should not be cached

if __name__ == '__main__':
    unittest.main()
