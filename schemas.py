from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime


class SupplierBase(BaseModel):
    name: str
    email: str
    phone_number: str
    address: str


class SupplierCreate(SupplierBase):
    pass


class SupplierResponse(SupplierBase):
    id: int

    model_config = {
        "from_attributes": True
    }

# ----------------------------------------------------------------


class ProductBase(BaseModel):
    name: str
    description: str | None = None
    price: Decimal
    stock: int

    model_config = {
        "json_encoders": {
            Decimal: str
        }
    }


class ProductCreate(ProductBase):
    supplyed_by_id: int


class ProductResponse(ProductBase):
    id: int
    reveneue: Decimal = Decimal('0.00')
    created_at: datetime | None = None
    updated_at: datetime | None = None
    supplyed_by: SupplierResponse

    model_config = {
        "from_attributes": True,
        "json_encoders": {
            datetime: lambda v: v.isoformat() if v else None,
            Decimal: str
        }
    }
