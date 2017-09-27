from datadog import statsd
# import boto3
import socket
import datadog


# client = boto3.client('redshift')
# redshift = boto3.resource('redshift')
# redshift
#app_name, host_name, claster_name, process_name, step_id, process_id

class MetricGenerator():
    def __init__(self):
        self.app_name = ()
        self.claster_name = ()
        self.process_name = ()
        self.step_id = ()
        self.process_id = ()
        self.host_name = ()

    def setMerticsAtributes(self, app_name, claster_name, process_name, step_id, process_id, host_name):
        self._app_name = app_name
        self._claster_name = claster_name
        self._process_name = process_name
        self._step_id = step_id
        self._process_id = process_id
        self._host_name = host_name

    def getMetricsValue(self):
        return self._app_name, self._claster_name, self._process_name, self._step_id, self._process_id, self._process_id,
        self._host_name
        print MetricGenerator.getMetricsValue()



print hasattr('_metric_path1', 'app_name')

# metric_path = {'app_name': None, 'host_name': None, 'claster_name': None, 'process_name': None, 'step_id': None,
#                'process_id': None}
#
# #print metric_path

