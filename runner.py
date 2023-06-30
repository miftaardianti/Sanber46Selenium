import unittest
from unittest.suite import TestSuite
import cart, saucedemo, folderbaru.test

if __name__ == "__main__":

    #inisiasi test suit
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    #add tests
    suite.addTests(loader.loadTestsFromModule(cart))
    suite.addTests(loader.loadTestsFromModule(saucedemo))
    suite.addTests(loader.loadTestsFromModule(folderbaru.test))

    #create runner
    runner = unittest.TextTestRunner()
    runner.run(suite)

