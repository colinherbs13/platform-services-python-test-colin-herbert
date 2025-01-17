import json
import tornado.web

from pymongo import MongoClient
from tornado.gen import coroutine
from tornado.web import HTTPError

"""
Endpoint 3: 
    * Return the same rewards data as Endpoint 2 (CustomerRewardsDataHandler) but for all customers.
"""


class RewardsDataHandler(tornado.web.RequestHandler):
    # this endpoint returns the entire customers collection
    @coroutine
    def get(self):
        client = MongoClient("mongodb", 27017)
        db = client["Rewards"]
        customers = list(db.customers.find({}, {"_id": 0}))

        # write the customers collection and if an error occurs write the error code
        try:
            self.write(json.dumps(customers))
        except HTTPError as e:
            self.write_error(e.status_code)
