import unittest
import m
ut = unittest
class UsersTestCase(ut.TestCase):
	def setUp(self):
		self.user = m.Users()
	def tearDown(self):
		self.user.dispose()
		self.user = None
	def testGetPasswdByUserName(self):
		self.assertEqual(self.user.getpasswd_byname("test"), "testpwd")

def suite():
	suite = ut.TestSuite()
	suite.addTest(UsersTestCase("testGetPasswdByUserName"))
	return suite

def __init__(self):
	ut.TestSuite.__init__(self, map(UsersTestCase, ("testGetPasswdByUserName")))

if __name__ == "__main__":
	runner = ut.TextTestRunner()
	runner.run(suite())
