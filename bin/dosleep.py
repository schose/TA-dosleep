from __future__ import absolute_import, division, print_function, unicode_literals

import os
import sys
import time

from splunklib.searchcommands import dispatch, StreamingCommand, Configuration, Option, validators

from splunklib import six

@Configuration()
class SleepCommand(StreamingCommand):
    time = Option(
        doc='''
        **Syntax:** **dnstimeout=***<dnstimeout>*
        **Description:** time to sleep in seconds''',
        require=True, validate=validators.Integer())
    

    def stream(self, records):
        
        self.logging_level = "INFO"
        sleeptime = self.time 
        # if dnsserver is not set use default form configfile one
        if self.time is None:
            sleeptime = 1

        time.sleep(sleeptime)

        for record in records:
            
            yield record



dispatch(SleepCommand, sys.argv, sys.stdin, sys.stdout, __name__)
