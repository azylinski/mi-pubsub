from datetime import datetime
from time import sleep
from uuid import uuid4
from google.protobuf.timestamp_pb2 import Timestamp
from pubsub.rabbit import PubSub
from proto.order_pb2 import Order
from proto.user_pb2 import User


ps = PubSub()


now = Timestamp()
now.FromDatetime(datetime.utcnow())

u = User(first_name='Adam', last_name='West', email='adam.west@mail.com', created_at=now)

ps.publish('signup_completed', u)


now.FromDatetime(datetime.utcnow())
o = Order(id=str(uuid4()), customer=u, created_at=now)

ps.publish('order_placed', o)
