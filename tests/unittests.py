import unittest
from app.auth import login

class Project2tests(unittest.TestCase):

    def LoginEmail(self):
        data = user@test.edu
        result = login(data)
        self.assertTrue(result, True)

    def LoginPassword(self):

    def RegisterEmail(self):

    def RegisterPasswordConfirm(self):

    def RegisterBadPassword(self):

    def alreadyRegister(self):

    def successfulLogin(self):

    def successfulRegister(self):

    def denyAccess(self):

    def allowAccess(self):



if __name__ == '__main__':
    unittest.main()