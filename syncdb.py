#!/usr/bin/env python
import os
from models import db


os.environ['PYTHONINSPECT'] = 'True'
db.create_all()
exit()
