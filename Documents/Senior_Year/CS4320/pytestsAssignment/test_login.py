import pytest
import login

def test_login():

	userName = login.getUserName()
	password = login.getPassword()
	assert userName != "" and  password != ""

def test_login_FAIL():
	userName = login.getUserNameFAIL()
	password = login.getPasswordFAIL()
	
	assert userName != '' and password != ''


# Test 2

def test_math():
	expectedResult = login.getExpectedResult()

	assert expectedResult == (9 * 2)

def test_math_FAIL():
	expectedResult = login.getExpectedResult()

	assert expectedResult == (9 * 3)

