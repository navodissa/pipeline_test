from flask import Flask, request
import logging
import logging.config
import handlers
import yaml

# Read the logger configurations from config.yaml file
with open('config/config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

# Get the logger specified in the file
logger = logging.getLogger('sampleLogger')

application = app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/batsman/', methods = ['POST'])
def show_Batsman():
    return handlers.batsman_Handler(request)


@app.route('/bowler/', methods = ['POST'])
def show_Bowler():
    return handlers.bowler_Handler(request)


@app.route('/keeper/', methods = ['POST'])
def show_Keeper():
    return handlers.keeper_Handler(request)

    

if __name__ == "__main__":
    app.run()