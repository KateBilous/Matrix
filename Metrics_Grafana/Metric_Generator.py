from datadog import statsd
# import boto3
import socket
import datadog


# client = boto3.client('redshift')
# redshift = boto3.resource('redshift')
# redshift
import Data_Collection

class MetricGenerator():


    def __init__(self, app_name, host_name, claster_name, process_name, step_id, process_id):
        self._app_name = app_name
        self._claster_name = claster_name
        self._process_name = process_name
        self._step_id = step_id
        self._process_id = process_id
        self._host_name = host_name



    def setMerticsAtributes(self, app_name, claster_name, process_name, step_id, process_id,host_name   ):
        self._app_name = app_name
        self._claster_name = claster_name
        self._process_name = process_name
        self._step_id = step_id
        self._process_id = process_id
        self._host_name = host_name

    def getMetricsValue(self  ):
        return self._app_name, self._claster_name, self._process_name, self._step_id, self._process_id, self._process_id,
        self._host_name
        print MetricGenerator.getMetricsValue()


print 'metics_path', Data_Collection.metric_path

