#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Kyle Fitzsimmons, 2015
'''
Config file for PushSFTP
'''

class Config:
    '''SFTP upload server parameters '''
    SFTP = {
        'host': 'sftpserver.com',
        'username': 'user',
        'password': 'pass',
        'port': 22
    }
    file_directory = 'folder/relative/path/'


