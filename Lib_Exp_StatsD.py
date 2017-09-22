import statsd
# import socket
import time
from datadog import DogStatsd

HOST = '172.25.1.18'  # Symbolic name meaning the local host
PORT = 2003  # Arbitrary non-privileged port

#
# statsd_connection = statsd.StatsClient(
#      host='172.25.1.18',
#      port=8125
#
#  )
# my_t = statsd_connection.timer('uuu')

#
# c = statsd.StatsClient('172.25.1.180', 8125)
# # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # s.connect((HOST, PORTSD))
# # statsd_client = StatsClient(HOST, 8125)
# #
# # client_instance=StatsClient('172.25.1.18', PORTSD)  # s.connect((HOST,PORT))
# #
# #
# #
# #
# # #timertStatsD = client_instance.timer("timer")
# #
# while True:
#     my_t.start()
#
#     start = time.time()
#     time.sleep(3)
#     delay_time = ((time.time() - start) * 1000)
#     #statsd_connection.timing('katetimingtest', delay_time)
#     my_t.stop()
#
# # r = range(1, 100)
# # c = statsd.StatsClient('172.25.1.180', 8125)
# # for  i in r:
# #     c.decr('incrkate.metric.value')
# #     print i

# from statsd import StatsClient

# statsd = StatsClient('172.25.1.18', 8125)
# foo_timer = statsd.timer('foo')
# foo_timer.start()
# # Do something fun.
# foo_timer.stop()
# import statsd

# from datadog import statsd
# from statsd import StatsClient
#
# statsd = StatsClient(host='172.25.1.18',
#                      port=8125,
#                      prefix=None,
#                      maxudpsize=512,
#                      ipv6=False)

# foo_stats = StatsClient(prefix='foo')
# bar_stats = StatsClient(prefix='bar')
f1 = 0
f2 = 1
# while True:
#     res = f1 + f2
#     f1 = f2
#     f2 = res
#     statsd.incr('baz', 1)
#     statsd.incr('foo', res)

# Create a client for this application
# statsd_client = statsd.StatsClient(__name__, statsd_connection)


# class SomeClass(object):
#     def __init__(self):
#         # Create a client specific for this class
#         self.statsd_client = statsd_client.get_client(
#             self.__class__.__name__)
#
#     def do_something(self):
#         # Create a `timer` client
#         timer = self.statsd_client.get_client(class_=statsd.Timer)
#
#         # start the measurement
#         timer.start()
#
#         # do something
#         timer.intermediate('intermediate_value')
#
#         # do something else
#         timer.stop('total')

#====================================================================
# Track the run time of the database query.
# start_time = time.time()
# results = db.query()
# duration = time.time() - start_time
# statsd.histogram('database.query.time', duration)
#
#
#
#
# @statsd.timed('database.query.time')
# def get_data():
#     return db.query()

#===================================================================