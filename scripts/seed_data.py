"""
Seed the database with sample products.
Run:  python -m scripts.seed_data
"""
from sqlalchemy.orm import Session
from app.db.session import SessionLocal, init_db
from app.models.product import Product

SAMPLE_PRODUCTS = [
    {
        "name": "Aashirvaad Atta",
        "image_url": "https://example.com/images/atta.jpg",
        "tag": "Best Sale",
        "weight": "5kg",
        "price": 289.0,
        "rating": 4.5,
        "old_price": 320.0,
    },
    {
        "name": "Amul Butter",
        "image_url": "https://example.com/images/amul-butter.jpg",
        "tag": "FROZEN",
        "weight": "500gm",
        "price": 265.0,
        "rating": 4.7,
        "old_price": None,
    },
    {
        "name": "Fortune Sunflower Oil",
        "image_url": "https://example.com/images/fortune-oil.jpg",
        "tag": "20% OFF",
        "weight": "1L",
        "price": 160.0,
        "rating": 4.2,
        "old_price": 200.0,
    },
    {
        "name": "Mother Dairy Milk",
        "image_url": "https://example.com/images/milk.jpg",
        "tag": "DAIRY",
        "weight": "1L",
        "price": 62.0,
        "rating": 4.1,
        "old_price": None,
    },
    {
        "name": "Bananas (Robusta)",
        "image_url": "https://example.com/images/banana.jpg",
        "tag": "FRESH",
        "weight": "6pc",
        "price": 48.0,
        "rating": 4.0,
        "old_price": 55.0,
    },
    {
        "name": "Tomatoes",
        "image_url": "https://example.com/images/tomato.jpg",
        "tag": "FRESH",
        "weight": "1kg",
        "price": 30.0,
        "rating": 4.3,
        "old_price": None,
    },
    {
        "name": "Parle-G Biscuits",
        "image_url": "https://example.com/images/parle-g.jpg",
        "tag": "SNACKS",
        "weight": "10pc",
        "price": 100.0,
        "rating": 4.6,
        "old_price": 120.0,
    },
    {
        "name": "Nestlé Maggi Noodles",
        "image_url": "https://example.com/images/maggi.jpg",
        "tag": "SNACKS",
        "weight": "12pc",
        "price": 168.0,
        "rating": 4.4,
        "old_price": None,
    },
    {
        "name": "Tata Salt",
        "image_url": "https://example.com/images/tata-salt.jpg",
        "tag": "ESSENTIAL",
        "weight": "1kg",
        "price": 22.0,
        "rating": 4.8,
        "old_price": 25.0,
    },
    {
        "name": "Amul Paneer",
        "image_url": "https://example.com/images/paneer.jpg",
        "tag": "FROZEN",
        "weight": "200gm",
        "price": 85.0,
        "rating": 4.5,
        "old_price": None,
    },
]


def seed():
    init_db()
    db: Session = SessionLocal()
    try:
        # Clear existing
        db.query(Product).delete()
        db.commit()

        for p in SAMPLE_PRODUCTS:
            db.add(Product(**p))
        db.commit()
        print(f"Inserted {len(SAMPLE_PRODUCTS)} products.")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
