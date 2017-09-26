from statsd import StatsClient
# from datadog import dogstatsd as statsd
from datadog import statsd
import Connection
import random
import time
import statsd
import datetime
import pytz
from datadog import api
# ===================================================================================================
# Sends Metrics to test Grafana throw StatsD



# Sends metrics throw StatsD to test Grafana

def StstsDmetricstiming():
    connectionClient = Connection.GrfanaConnectionStatsD()
    # connectionClient = StatsClient(host='172.25.1.18', port=8125)

    i = random.randint(0, 500)

    while True:
        statsd.DogStatsd.timing('lalala.metric.value', i, )

        time.sleep(0.5)
        i = random.randint(0, 500)


# ====================================================================================================
# Sends metrics throw DogStatsD to test Grafana

def DogStatsdincrement():
    ConnectionClient = Connection.GrafanaConnectionDogStatsD()
    i = random.randint(0, 10)
    while True:
        ConnectionClient.increment('my.metric_name', 1, tags="dogincrement", sample_rate=0.5)


def DogStatsDtiming():
    ConnectionClient = Connection.GrafanaConnectionDogStatsD()

    # @ConnectionClient.timed('user.query.time', sample_rate=0.5)
    # def get_user(user_id):
    #     time.sleep(5)
    #     # Do what you need to ...

    # Is equivalent to ...
    with ConnectionClient.timed('user.query.time', sample_rate=0.5):
        # Do what you need to ...
        pass

    # Is equivalent to ...
    start = time.time()
    time.sleep(5)
    ConnectionClient.timing('user.query.time', time.time() - start)


def DogSatasDhistograms():
    ConnectionClient = Connection.GrafanaConnectionDogStatsD()

    start_time = time.time()
    #page = render_page()
    duration = time.time() - start_time
    ConnectionClient.histogram('mywebsite.page_render.time',
                               duration)


def DatadogStatsDgauge():


    ConnectionClient = Connection.GrafanaConnectionDogStatsD()

    ConnectionClient.gauge('mywebsite.users.active', random.randint(50, 78))
# ======================================================================================================


def DatadofEventStatsd():
    ConnectionClient = Connection.GrafanaConnectionDogStatsD()
    #ConnectionClient  =  Connection.DatadogConnection()
    ConnectionClient.event("event.mymetric", "Satrrt IDF", alert_type='error',  source_type_name= 'nme of database or smth else',
                           date_happened= time.clock(), hostname= '172.25.1.18')


def DatadogEventStatsD():
    ConnectionClient = Connection.GrafanaConnectionDogStatsD()
    title = "test with Markdown"
    text = """This **section** will not have any formatting applied.
    %%%
    Here **the markdown** will work
    %%%"""
    tags = ['test:markdown']
    ConnectionClient.event(title=title, text=text, tags=tags)


def main():
    ConnectionClient = Connection.GrafanaConnectionDogStatsD()

    title = input("Enter the title: ")
    text = input("Enter the text: ")
    tags = input("Enter the tags: ")
    time = input("Enter the local time (YYYY-MM-DD HH:MM:SS): ")

    naive = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
    my_tz = pytz.timezone("Australia/Sydney")
    local_dt = my_tz.localize(naive, is_dst=None)
    utc_dt = local_dt.astimezone(pytz.utc)
    time = utc_dt.strftime('%Y-%m-%dT%H:%M:%SZ')

    json_body = [
        {
            "measurement": "stag",
            "tags": {
            },
            "fields": {
                "title": title,
                "text": text,
                "tags": tags
            },
            "time": time
        }
    ]

    api.Event.create(json_body);

    print("Wrote the following point:")
    print(json_body)


if __name__ == '__main__':
    while True:
        main()
        #DatadofEventStatsd()
        #DatadofEventStatsd()
        #DatadogStatsDgauge()
        #DogSatasDhistograms()
        # DogStatsDtiming()
        # StstsDmetricstiming()
        # DogStatsdincrement()
