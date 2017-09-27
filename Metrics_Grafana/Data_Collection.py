from  Metric_Generator import MetricGenerator
import Metric_Generator


def setMetricPath():
    _metric_path = MetricGenerator()
    _metric_path.host_name = "Grafana"
    _metric_path.step_id = 125
    _metric_path.process_name = 'Some name'
    _metric_path.app_name = 'Some app name'
    _metric_path.claster_name = 'Claster name'
    _metric_path.process_id = 456

    return _metric_path.process_id, _metric_path.claster_name, _metric_path.app_name, _metric_path.process_name, _metric_path.step_id,
    _metric_path.host_name


# jj = MetricGenerator("IDF", "Redshift", "Claster1", "Process1", 65, 85)

# def objectRedefinition():
#     metric_path = str(_metric_path)
#     return metric_path


print setMetricPath()

print hasattr("_metric_path", "_metric_path.host_name")
