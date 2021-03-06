import orm
from models import User, Blog, Comment
import asyncio, os, json, time

loop = asyncio.get_event_loop()

@asyncio.coroutine
def test():
    yield from orm.create_pool(loop, user='www-data', password='www-data', database='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()

#for x in test():
#    pass

loop.run_until_complete(test())
