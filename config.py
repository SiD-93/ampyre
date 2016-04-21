import json
from pythonzenity import *
config = { }

def confWrite():
    minimum = Entry(title='Ampyre Config', text='Enter the minimum threshold: ')
    maximum = Entry(title='Ampyre Config', text='Enter the maximum threshold: ')
    if (minimum == '' or maximum == ''):
        Warning(title='Ampyre Config', text='Threshold(s) not set. Please set to continue.')
        confWrite()
    else:
        config = {'minThreshold': minimum, 'maxThreshold': maximum}
        with open('conf.json', 'w') as f:
            json.dump(config, f)
            f.close()
        Message(title='Ampyre Config', text='Thresholds set.')

def confRead(confValue):
    with open('conf.json', 'r') as f:
        config = json.load(f)
        return config[confValue]
        f.close()
