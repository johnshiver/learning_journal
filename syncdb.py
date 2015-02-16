#!/usr/bin/env python
import os
import readline
from pprint import pprint
from flask import *
from models import db


os.environ['PYTHONINSPECT'] = 'True'
db.create_all()
exit()
