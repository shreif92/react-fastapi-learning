from fastapi import FastAPI, HTTPException, status
from tortoise.contrib.fastapi import register_tortoise
from tortoise.exceptions import DoesNotExist

from models import Product, Supplier
from schemas import SupplierCreate, SupplierResponse, ProductCreate, ProductResponse


app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello, World!"}

# -----------------------------------------------------------------------------


@app.post("/supplier", response_model=SupplierResponse)
async def create_supplier(supplier_data: SupplierCreate):
    supplier = await Supplier.create(**supplier_data.dict())
    return supplier


@app.get("/supplier/{supplier_id}", response_model=SupplierResponse)
async def get_supplier(supplier_id: int):
    supplier = await Supplier.get(id=supplier_id)
    return supplier


@app.get("/suppliers", response_model=list[SupplierResponse])
async def get_suppliers():
    suppliers = await Supplier.all()
    return suppliers


@app.put("/update_supplier/{supplier_id}", response_model=SupplierResponse)
async def update_supplier(supplier_id: int, supplier_data: SupplierCreate):
    try:
        supplier = await Supplier.get(id=supplier_id)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="supplier not found")

    supplier.name = supplier_data.name
    supplier.email = supplier_data.email
    supplier.phone_number = supplier_data.phone_number
    supplier.address = supplier_data.address
    await supplier.save()
    return supplier


@app.delete("/delete_supplier/{supplier_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_supplier(supplier_id: int):
    try:
        supplier = await Supplier.get(id=supplier_id)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="supplier not found")

    await supplier.delete()
    return None

# ------------------------------------------------------------------------------------


@app.post("/product", response_model=ProductResponse)
async def create_product(product_data: ProductCreate):
    try:
        # First check if supplier exists
        supplier = await Supplier.get(id=product_data.supplyed_by_id)
        # Create product if supplier exists
        product = await Product.create(**product_data.dict())
        return await Product.get(id=product.id).prefetch_related('supplyed_by')
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail=f"Supplier with id {product_data.supplyed_by_id} not found"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.get("/products", response_model=list[ProductResponse])
async def all_products():
    try:
        products = await Product.all().prefetch_related('supplyed_by')
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/product/{product_id}", response_model=ProductResponse)
async def get_product(product_id: int):
    try:
        product = await Product.get(id=product_id).prefetch_related('supplyed_by')
        return product
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="product not found")


@app.delete("/delete_product/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: int):
    try:
        product = await Product.get(id=product_id)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="product not found")

    await product.delete()
    return None


@app.put("/update_product/{product_id}", response_model=ProductResponse)
async def update_product(product_id: int, product_data: ProductCreate):
    try:
        product = await Product.get(id=product_id)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="product not found")

    product.name = product_data.name
    product.description = product_data.description
    product.stock = product_data.stock
    product.price = product_data.price
    product.supplyed_by_id = product_data.supplyed_by_id
    await product.save()
    return await Product.get(id=product.id).prefetch_related('supplyed_by')
# ----------------------------------------------------------------------------------
register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
