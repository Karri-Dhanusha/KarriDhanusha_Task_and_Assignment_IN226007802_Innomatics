from fastapi import FastAPI

app = FastAPI()

# Initial products
products = [
    {"id": 1, "name": "Notebook", "price": 50, "category": "Stationery", "in_stock": True},
    {"id": 2, "name": "Pen", "price": 10, "category": "Stationery", "in_stock": True},
    {"id": 3, "name": "Monitor", "price": 7000, "category": "Electronics", "in_stock": True},
    {"id": 4, "name": "Mouse", "price": 500, "category": "Electronics", "in_stock": False},

    # Q1 - Added products
    {"id": 5, "name": "Laptop Stand", "price": 1299, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1899, "category": "Electronics", "in_stock": False},
]


# Root API
@app.get("/")
def home():
    return {"message": "FastAPI Store API Running"}


# Show all products
@app.get("/products")
def get_products():
    return {
        "products": products,
        "total": len(products)
    }


# Q2 - Filter by category
@app.get("/products/category/{category_name}")
def get_by_category(category_name: str):
    result = [p for p in products if p["category"] == category_name]

    if not result:
        return {"error": "No products found in this category"}

    return {
        "category": category_name,
        "products": result,
        "total": len(result)
    }


# Q3 - Show only in-stock products
@app.get("/products/instock")
def get_instock():
    available = [p for p in products if p["in_stock"] == True]

    return {
        "in_stock_products": available,
        "count": len(available)
    }


# Q4 - Store summary
@app.get("/store/summary")
def store_summary():

    total_products = len(products)
    in_stock = len([p for p in products if p["in_stock"]])
    out_stock = total_products - in_stock

    categories = list(set([p["category"] for p in products]))

    return {
        "total_products": total_products,
        "in_stock_products": in_stock,
        "out_of_stock_products": out_stock,
        "categories": categories
    }