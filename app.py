#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 
Course work: 
@author: raja
Source:
    
'''

# Import necessary modules
import falcon

class City(object):

    def on_get(self, request, response):

        result = {
            'name' : 'Toronto',
            'timezone' : 'EST'
        }

        response.media = result

    
api = falcon.API()
api.add_route('/', City())


'''
    how to run?

    gunicorn -b 0.0.0.0:8000 app:api

    or

    gunicorn -b localhost:8000 app:api
'''