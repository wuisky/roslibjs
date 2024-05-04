#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler, test
import sys
import os

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # self.root_directory = kwargs.pop('root_directory', os.getcwd())
        # self.root_directory = os.path.join(os.getcwd(), 'ur_description')
        self.root_directory = '/opt/ros/humble/share'
        super().__init__(*args, directory=self.root_directory, **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

if __name__ == '__main__':
    # root_dir = sys.argv[2] if len(sys.argv) > 2 else os.getcwd()
    root_dir = os.getcwd()
    test(CORSRequestHandler, HTTPServer, port=int(sys.argv[1]) if len(sys.argv) > 1 else 8000)
