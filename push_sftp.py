#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Kyle Fitzsimmons, 2015
'''
Login to SFTP server and push downloaded media to a folder
'''
from __future__ import print_function
import os
import sys
import time
import functools
import pysftp
from etaprogress.progress import ProgressBarWget
import config

class SFTP:
    '''Uploads files to config server and directory'''
    def __init__(self):
        self.config = config.Config()
        self.bar = None
        self.byes_written = 0
        self.last_file_size = 0

    @setupteardown
    def progress(self, bytes, file_size):
        '''Display and update progress bar in place for upload progress'''
        self.bar.numerator = bytes
        print(self.bar, end='\r')
        sys.stdout.flush()
        self.byes_written = bytes
        self.last_file_size = file_size
        
    def upload(self, content, display=True):
        '''Upload content file and handle stdout display'''
        with pysftp.Connection(**self.config.SFTP) as conn:
            with conn.cd(self.config.file_directory):
                if display:
                    callback = self.progress
                    start = time.time()
                    print('Uploading: {}'.format(content))
                else:
                    callback = None
                conn.put(content, preserve_mtime=True, callback=callback)
        if callback:
            end = time.time()
            duration = end - start
            print()
            print('Upload finished in {t:.2f}s, {d} transferred'.format(
                t=duration, 
                d=human_readable(self.last_file_size)
            ))

# helper functions
def human_readable(num, suffix='B'):
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            size = {'num': num, 'u': unit, 's': suffix}
            return '{num:.1f}{u}{s}'.format(**size)
        num /= 1024.0
    size = {'num': num, 'u': 'Y', 's': suffix}
    return '{num:.1f}{u}{s}'.format(**size)

def setupteardown(func):
    def _decorator(self, bytes, file_size):
        # setup
        if not self.byes_written:
            self.bar = ProgressBarWget(file_size)
        # execute
        func(self, bytes, file_size)
        sys.stdout.flush()
        # teardown
        if self.byes_written == file_size:
            self.byes_written = 0
            self.bar = None
    return _decorator

if __name__ == '__main__':
    S = SFTP()
    S.upload('testfile.dat', display=True)

