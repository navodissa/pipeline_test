import unittest
import requests


class ApiTest(unittest.TestCase):
    ''' With this APITest class, we will be performing unit tests for all the API calls'''  

# Constants related to unittests
    API_URL = "http://localhost:5000"
    BATSMAN_URL = "{}/batsman/".format(API_URL)
    BOWLER_URL = "{}/bowler/".format(API_URL)
    KEEPER_URL = "{}/keeper/".format(API_URL)

# Unit tests for batsman related API calls 

    def test_1__post_batsman(self):
        arg = '{"value": 10}'
        output = {"arg": 10, "Batsman output": "Sanath Jayasuriya"} 
        resp = requests.post(ApiTest.BATSMAN_URL, data=arg, headers={'Content-Type': 'application/json'})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(),output)

    def test_2__post_batsman_validation(self):
        arg1 = '{"value": "10"}'
        output1 = {"ERROR" : "Integer values are required"} 
        resp = requests.post(ApiTest.BATSMAN_URL, data=arg1, headers={'Content-Type': 'application/json'})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(),output1)

        arg2 = '{"value": -1}'
        output2 = {'ERROR' : 'Only positive values are allowed'}
        resp = requests.post(ApiTest.BATSMAN_URL, data=arg2, headers={'Content-Type': 'application/json'})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(),output2)

        arg3 = '{"value": 10}'
        output3 = {'ERROR': 'Content-Type not supported!'}
        resp = requests.post(ApiTest.BATSMAN_URL, data=arg3, headers={'Content-Type': 'text/plain'})
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(resp.json(),output3)

    
# Unit Test for bowler related API calls

    def test_3__post_bowler(self):
        arg = '{"value1": 2, "value2": 6}'
        output = {"bowler output": "Muralidaran broke 2 wicket/s from 6 ball/s", "arg_1": 2, "arg_2": 6} 
        resp = requests.post(ApiTest.BOWLER_URL, data=arg, headers={'Content-Type': 'application/json'})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(),output)

    def test_4__post_bowler_validation(self):
        arg1 = '{"value1": "2", "value2": 0}'
        output1 = {"ERROR" : "Integer values are required"} 
        resp = requests.post(ApiTest.BOWLER_URL, data=arg1, headers={'Content-Type': 'application/json'})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(),output1)

        arg2 = '{"value1": -2, "value2": 0}'
        output2 = {'ERROR' : 'Only positive values are allowed'}
        resp = requests.post(ApiTest.BOWLER_URL, data=arg2, headers={'Content-Type': 'application/json'})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(),output2)

        arg3 = '{"value1": 2, "value2": 0}'
        output3 = {'ERROR': 'Content-Type not supported!'}
        resp = requests.post(ApiTest.BOWLER_URL, data=arg3, headers={'Content-Type': 'text/plain'})
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(resp.json(),output3)


# Unit Tests for keeper related API calls

    def test_5__post_keeper(self):
        arg = '{"value": 5}'
        output = {"Keeper Output": "Romesh Kaluwitharana", "arg": 5 } 
        resp = requests.post(ApiTest.KEEPER_URL, data=arg, headers={'Content-Type': 'application/json'})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(),output)

    def test_6__post_keeper_validation(self):
        arg1 = '{"value": "10"}'
        output1 = {"ERROR" : "Integer values are required"} 
        resp = requests.post(ApiTest.KEEPER_URL, data=arg1, headers={'Content-Type': 'application/json'})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(),output1)

        arg2 = '{"value": -1}'
        output2 = {'ERROR' : 'Only positive values are allowed'}
        resp = requests.post(ApiTest.KEEPER_URL, data=arg2, headers={'Content-Type': 'application/json'})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(),output2)

        arg3 = '{"value": 10}'
        output3 = {'ERROR': 'Content-Type not supported!'}
        resp = requests.post(ApiTest.BATSMAN_URL, data=arg3, headers={'Content-Type': 'text/plain'})
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(resp.json(),output3)

