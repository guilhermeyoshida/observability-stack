from opentelemetry.sdk.resources import SERVICE_NAME, Resource

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

from opentelemetry import metrics
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader

# Service name is required for most backends
resource = Resource(attributes={
    SERVICE_NAME: "teste"
})

traceProvider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="http://0.0.0.0:50371"))
traceProvider.add_span_processor(processor)
trace.set_tracer_provider(traceProvider)

# reader = PeriodicExportingMetricReader(
#     OTLPMetricExporter(endpoint="localhost:5555")
# )
# meterProvider = MeterProvider(resource=resource, metric_readers=[reader])
# metrics.set_meter_provider(meterProvider)
