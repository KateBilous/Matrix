from datadog import statsd
# import boto3
import socket
import datadog


# client = boto3.client('redshift')
# redshift = boto3.resource('redshift')
# redshift


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

        # metics_path = MetricGenerator(_app_name="IDF",
        #
        #                               _claster_name="Clustar_Name",
        #                               _process_name="Process_Name",
        #                               _step_id=546745,
        #                               _process_id=5698,
        #                               _host_name="125.32.5.5")

# metric_path = MetricGenerator(app_name = "IDF",  host_name = "Clustar_Name", claster_name = "Process_Name",
#                               process_name = 546745, step_id = 5698, process_id= "125.32.5.5")

metric_path = MetricGenerator()

metric_path_ = metric_path.setMerticsAtributes(app_name = "kate")

print 'metics_path', metric_path
