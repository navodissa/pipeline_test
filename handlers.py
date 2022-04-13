import logging.config
import logging
from flask import jsonify
import yaml

# Read the logger configurations from config.yaml file
with open('config/config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)


# Get the logger specified in the file
logger = logging.getLogger('sampleLogger')


# Default Error messages as a list
ERROR_MSGS = [{'ERROR': 'Content-Type not supported!'}, 
            {'ERROR' : 'Only positive values are allowed'},
            {'ERROR' : 'Integer values are required'},
            {'ERROR' : 'TimeOut-maximum recursion depth exceeded in comparison'},
            {'ERROR' : 'TimeOut-Too many digits in integer'}]


def batsman_Handler(request):

    # Get the content Type and host ip address from the request
    content_type = request.headers.get('Content-Type')
    ip = request.headers.get('Host')

    # If content type is not JSON return an error message
    if (content_type == 'application/json'):
        jsonData = request.get_json()
        arg = jsonData['value']
    
    # Check if passed value is an integer and greater than 0 or else return error messages
        if isinstance(arg, int) == False:
            logger.error(ERROR_MSGS[2])
            return jsonify(ERROR_MSGS[2])
        elif arg < 0:
            logger.error(ERROR_MSGS[1])
            return jsonify(ERROR_MSGS[1])  

        logger.info("Input value for batsman: {value} received from ip : {ip}".format(value=arg, ip=ip))

        result = "Sanath Jayasuriya"

    # Create the dictionary with the returend response
        response = { 'arg': arg, 'Batsman output': result }
        logger.info("Response sent: {response}".format(response=response))
    
    # Return the jsonfied response back
        return jsonify(response)
    else:
        logger.error("{error}. Received: {errorType} from ip : {ip}".format(error=ERROR_MSGS[0], errorType=content_type, ip=ip))
        return jsonify(ERROR_MSGS[0]), 400


def bowler_Handler(request):
    # Get the content Type and host ip address from the request
    content_type = request.headers.get('Content-Type')
    ip = request.headers.get('Host')

    # If content type is not JSON return an error message
    if (content_type == 'application/json'):
        jsonData = request.get_json()            
        arg1 = jsonData['value1']
        arg2 = jsonData['value2']

    # Check if passed values are an integer and greater than 0 or else return error messages
        if isinstance(arg1, int) & isinstance(arg2, int) == False:
            logger.error(ERROR_MSGS[2])
            return jsonify(ERROR_MSGS[2])
        elif arg1 | arg2 < 0:
            logger.error(ERROR_MSGS[2])
            return jsonify(ERROR_MSGS[1]) 
        logger.info("Input values for Bowler (arg1: {arg1}, arg2: {arg2}) received from ip : {ip}".format(arg1=arg1, arg2=arg2, ip=ip))

        try:
            result = "Muralidaran broke {arg1} wicket/s from {arg2} ball/s".format(arg1=arg1, arg2=arg2)
        except RecursionError:
            logger.error(ERROR_MSGS[3])
            return jsonify(ERROR_MSGS[3])
        except OverflowError:
            logger.error(ERROR_MSGS[4])
            return jsonify(ERROR_MSGS[4]) 

    # Create the dictionary with the returend response
        response = { 'arg_1': arg1, 'arg_2' : arg2, 'bowler output': result }
        logger.info("Response sent: {response}".format(response=response))

    # Return the jsonfied response back
        return jsonify(response)
    else:
        logger.error("{error}. Received: {errorType} from ip : {ip}".format(error=ERROR_MSGS[0], errorType=content_type, ip=ip))
        return jsonify(ERROR_MSGS[0]), 400


def keeper_Handler(request):
    # Get the content Type and host ip address from the request
    content_type = request.headers.get('Content-Type')
    ip = request.headers.get('Host')

    # If content type is not JSON return an error message
    if (content_type == 'application/json'):
        jsonData = request.get_json() 
        arg = jsonData['value']

    # Check if passed value is an integer and greater than 0 or else return error messages    
        if isinstance(arg, int) == False:
            logger.error(ERROR_MSGS[2])
            return jsonify(ERROR_MSGS[2])
        elif arg < 0:
            logger.error(ERROR_MSGS[1])
            return jsonify(ERROR_MSGS[1]) 

        logger.info("Input value for Keeper: {value} received from ip : {ip}".format(value=arg, ip=ip))

    # Call the Keeper 
        result = "Romesh Kaluwitharana"
        response = { 'arg': arg, 'Keeper Output': result }
        logger.info("Response sent: {response}".format(response=response))
    
    # Return the jsonfied response back
        return jsonify(response)
    else:
        logger.error("{error}. Received: {errorType} from ip : {ip}".format(error=ERROR_MSGS[0], errorType=content_type, ip=ip))
        return jsonify(ERROR_MSGS[0]), 400