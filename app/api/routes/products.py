from typing import List, Optional, Literal
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import select, asc, desc
from sqlalchemy import or_
from app.db.session import get_db
from app.models.product import Product as ProductModel
from app.schemas.product import ProductOut, ProductCreate
from fastapi import UploadFile, File


router = APIRouter(prefix="/products", tags=["products"])


@router.get("", response_model=List[ProductOut])
def list_products(
    db: Session = Depends(get_db),
    q: Optional[str] = Query(None, description="Search text in name, tag, or weight"),
    tag: Optional[str] = Query(None, description="Filter by tag"),
    min_price: Optional[float] = Query(None),
    max_price: Optional[float] = Query(None),
    sort_by: Literal["id", "name", "price", "rating"] = Query("id"),
    order: Literal["asc", "desc"] = Query("asc"),
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
):
    stmt = select(ProductModel)

    if q:
        like = f"%{q}%"
        stmt = stmt.where(
            or_(
                ProductModel.name.ilike(like),
                ProductModel.tag.ilike(like),
                ProductModel.weight.ilike(like),
            )
        )

    if tag:
        stmt = stmt.where(ProductModel.tag == tag)

    if min_price is not None:
        stmt = stmt.where(ProductModel.price >= min_price)

    if max_price is not None:
        stmt = stmt.where(ProductModel.price <= max_price)

    sort_col = getattr(ProductModel, sort_by)
    stmt = stmt.order_by(asc(sort_col) if order == "asc" else desc(sort_col))

    stmt = stmt.limit(limit).offset(offset)

    rows = db.execute(stmt).scalars().all()
    return [ProductOut.model_validate(r) for r in rows]


@router.get("/{product_id}", response_model=ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.get(ProductModel, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return ProductOut.model_validate(product)


@router.post("", response_model=ProductOut, status_code=201)
def create_product(payload: ProductCreate, db: Session = Depends(get_db)):
    product = ProductModel(
        name=payload.name,
        image_url=payload.imageUrl,
        tag=payload.tag,
        weight=payload.weight,
        price=payload.price,
        rating=payload.rating,
        old_price=payload.oldPrice,
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return ProductOut.model_validate(product)

@router.put("/{product_id}/image", response_model=ProductOut)
def update_product_image(
    product_id: int,
    image_url: str,   # send new image URL as query or JSON
    db: Session = Depends(get_db)
):
    product = db.get(ProductModel, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product.image_url = image_url
    db.commit()
    db.refresh(product)
    return ProductOut.model_validate(product)
