from fastapi import FastAPI
from scalar_fastapi import add_scalar_reference, Theme

app = FastAPI(
    title="My FastAPI App", 
    description="This is a sample FastAPI application with Scalar reference.", 
    version="1.0.0"
)

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

add_scalar_reference(
    app,
    route="/scalar",
    theme=Theme.BLUE_PLANET, 
    dark_mode=True,
)
