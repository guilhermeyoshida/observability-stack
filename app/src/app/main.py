from typing import Union
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry import trace
from fastapi import FastAPI
from . import tracing
app = FastAPI()

# FastAPIInstrumentor.instrument_app(app)
tracer = trace.get_tracer("test.tracer")

@app.get("/")
def read_root():
    with tracer.start_as_current_span("root") as root_span:
        obj = {"Hello": "World"}
        root_span.set_attribute("obj", "asdads")
        return obj


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
