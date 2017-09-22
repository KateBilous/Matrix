from statsd import StatsClient
from datadog import dogstatsd


# ===================================================================================================
# Sends Metrics to test Grafana throw StatsD



# Sends metrics throw StatsD to test Grafana


connectionClient = StatsClient(host='172.25.1.18', port=8125)
f1 = 0
f2 = 1
while True:
    res = f1 + f2
    f1 = f2
    f2 = res
    connectionClient.incr('kkk')
    print("value is %d" % res)

# ====================================================================================================
# Sends metrics throw DogStatsD to test Grafana


connection = dogstatsd.DogStatsd(host='172.25.1.18',  # Host to test Grafana
                                 port=8125,  # StatsD port on test Grafana
                                 max_buffer_size=50,
                                 namespace=None,
                                 constant_tags=None,
                                 use_ms=False,
                                 use_default_route=False)
i = random.randint(0, 10)
while True:
    connection.increment('my.metric_name', 1, sample_rate=0.5)
