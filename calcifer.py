#!/usr/bin/python3

import os
import time
import yaml

def getConf(whichConfig):
    confFile = os.getcwd() + '/config/' + whichConfig + '.yaml'


def initConf():
    # todo: this bit to get conf files in the right place
    # check ~/.calcifer for conf files and create them if needed

def furnaceStatus(status):
    # start furnace
        # open flue damper # check safety
        # close thermostat switch
    # check heater coil temp
        # when @targetTemp is reached, return True


def heat(room):
    # turn off heat exchanger fan
    # close all duct dampers
        # or keep track of what's open
    # open room damper
    # turn on heat exchanger fan
    # return True


if __name__ == 'main':

    # First run, create conf files
    initConf()

    conf = getConf('main')

    while (True):
        # Check for heat commands from Daisy



