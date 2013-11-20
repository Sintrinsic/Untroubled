'''
Created on Nov 19, 2013

@author: bdupree
'''

class GenericEvent(object):

    def __init__(self, identifier, metaDataDict):
        self.identifier = identifier
        self.meta = metaDataDict #dictionary of passed data
        self.cancelled = False
        