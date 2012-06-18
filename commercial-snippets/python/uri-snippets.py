'''
Created on 24 Mar 2011
Last Updated on 28 Mar 2011
PARTIAL CODE REMOVAL 18th June 2012 - removed commercial-sensitive code to put in dlewis-portfolio

@author: Daniel Lewis <daniel@vanirsystems.com>
'''
from urlparse import urlparse
from urlparse import urldefrag
from urlparse import urlsplit
from datetime import datetime
import socket
import urllib2
''' CODE REMOVED '''
import logging, re
class Uri():
    
    def __init__(self, links, plinks):
        self.links = links
        self.plinks = plinks
    
    # function: check valid
    def validate(self, uri):
        response = Client(uri)
        response.head()
        return (response.geturl(), response.info().gettype(), response.info().getsubtype())
    
    # function: check if uri is in the database
    def is_present(self, uri):
        ''' CODE REMOVED '''
        
    # function: grabs the longuri from the database based on a shorturi
    def db_longifier(self, shorturi):
        ''' CODE REMOVED '''
    
    # function: grabs a longuri from the internet by sending a get head request
    def net_longifier(self, shorturi):
        response = Client(shorturi)
        response.head()
        return urldefrag(response.geturl())[0]
    
    # function: returns true if the longuri is in the collection
    def longuri_ispresent(self, longuri):
        ''' CODE REMOVED '''
        
        
    # function: save a uri with an upsert
    def save(self, data = {}):
        ''' CODE REMOVED '''  
    
    # function: appends a shorturi to a longuri link
    def append_shorturi(self, link, shorturi):
        ''' CODE REMOVED '''

    # function: fetches a uri, first checking the database, and if not found then checking the net (uses aspects for probing)
    def fetch_uri(self, link):
        ''' CODE REMOVED '''
    
    ''' CODE REMOVED '''
        
    def filter(self, data, content):
        ''' CODE REMOVED '''
    
    def get(self, link, force = False):
        ''' CODE REMOVED '''
    
class HeadRequest(urllib2.Request):
    """
    HEAD request wrapper, usage:
    
    response = urllib2.urlopen(HeadRequest(link))
    """
    def get_method(self):
        return "HEAD"

class InvalidUrlError(Exception):
    """
    Invalid url exception
    """
