from sqlalchemy import inspect

from models import Base, Product
from database import engine

inspector = inspect(engine)

columns = inspector.get_columns("products")

for column in columns:
    print(
        f"Название: {column['name']} | "
        f"Тип: {column['type']} | "
        f"Nullable: {column['nullable']}"
    )