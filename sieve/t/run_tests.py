import unittest

if __name__ == '__main__':

    suite = unittest.defaultTestLoader.loadTestsFromNames(
            (
                'sieve.t.test_evaluation',
                'sieve.t.test_parser',
                'sieve.t.test_validators',
            ),
        )
    unittest.TextTestRunner().run(suite)
