#!/usr/bin/env python3#!/usr/bin/env python3
from .db import db
from sqlalchemy.sql import func

class Visitor(db.Model):

    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    at = db.Column(db.TIMESTAMP, nullable=False, server_default=func.now())
    user_agent = db.Column(db.String(1024), nullable=True)

