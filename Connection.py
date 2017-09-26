from statsd import StatsClient
import datadog

#==============================Connection to Grafana===================================================

def GrfanaConnectionStatsD():
    connection = StatsClient(host='172.25.1.18',
                             port=8125)
    return connection


def GrafanaConnectionDogStatsD():
    connection = datadog.DogStatsd(host='172.25.1.18',  # Host to test Grafana
                                     port=8125,  # StatsD port on test Grafana
                                     max_buffer_size=50,
                                     namespace=None,
                                     constant_tags=None,
                                     use_ms=False,
                                     use_default_route=False)
    return connection



#=============================Connection to Datadog====================================================

def DatadogConnection():
    connection = datadog.DogStatsd( host = 'https://app.datadoghq.com',
                                      port = 8125,
                                      namespace=None,
                                      constant_tags=None,
                                      use_ms=False,
                                      use_default_route=False
                                      )
    return connection