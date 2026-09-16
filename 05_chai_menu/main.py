from fastapi import FastAPI, HTTPException, Query
from models import MenuItem, MenuResponse
from data import menu_items

app = FastAPI(
    title="Chai Menu API",
    description="This is a menu for chai ",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)


@app.get("/")
def root():
    return {"message": "Welcome to Chai Menu API"}


@app.get("/menu", response_model=MenuResponse)
def get_menu(
    category: str | None = Query(
        None, description="Filter by chai,shakes,snacks,sides,dessert"
    )
):
    if category:
        filtered_menu = [
            item for item in menu_items if item["category"] == category.lower()
        ]
        if not filtered_menu:
            raise HTTPException(status_code=404, detail="Menu item not found")
        return MenuResponse(count=len(filtered_menu), menu_items=filtered_menu)
    return MenuResponse(count=len(menu_items), menu_items=menu_items)
