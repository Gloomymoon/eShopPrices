# coding=utf-8
from datetime import datetime

from app import db


class eShopPrice(db.Model):
    __tablename__ = "eshop_prices"
    datetime = db.Column(db.DateTime(), default=datetime.now, primary_key=True)
    content = db.Column(db.Text)
