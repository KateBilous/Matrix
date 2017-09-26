import Connection
from datadog import dogstatsd

Connection.GrafanaConnectionDogStatsD()
dogstatsd.DogStatsd