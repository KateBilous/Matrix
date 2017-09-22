from statsd import StatsClient
from datadog import dogstatsd


def connectionStatsD():
    connection = StatsClient(host='172.25.1.18',
                             port=8125)
    return connection


def connectionDogStatsD():
    connection = dogstatsd.DogStatsd(host='172.25.1.18',  # Host to test Grafana
                                     port=8125,  # StatsD port on test Grafana
                                     max_buffer_size=50,
                                     namespace=None,
                                     constant_tags=None,
                                     use_ms=False,
                                     use_default_route=False)
    return connection
         