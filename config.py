import configparser
import os
from configparser import ConfigParser


class config(object):
    global property_map
    def properties(self, abspath):
        property_map={}
        #path = os.path.abspath("properties")
        cf = configparser.ConfigParser()
        print(abspath)
        cf.read(abspath)
        for item in cf.sections():
            temp={}
            for option in cf.options(item):
                temp[option] = cf[item][option]
            property_map[item] = temp
        return property_map


#print(config().properties())
