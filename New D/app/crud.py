from typing import Sequence
from sqlalchemy.orm import Session
from sqlalchemy import select
from . import models, schemas


def create_item(db: Session, item_in: schemas.ItemCreate) -> models.Item:
    item = models.Item(name=item_in.name, description=item_in.description)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def get_item(db: Session, item_id: int) -> models.Item | None:
    return db.get(models.Item, item_id)


def get_item_by_name(db: Session, name: str) -> models.Item | None:
    stmt = select(models.Item).where(models.Item.name == name)
    return db.scalar(stmt)


def list_items(db: Session, skip: int = 0, limit: int = 100) -> Sequence[models.Item]:
    stmt = select(models.Item).offset(skip).limit(limit)
    return list(db.scalars(stmt))


def update_item(db: Session, item: models.Item, item_in: schemas.ItemUpdate) -> models.Item:
    if item_in.name is not None:
        item.name = item_in.name
    if item_in.description is not None:
        item.description = item_in.description
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def delete_item(db: Session, item: models.Item) -> None:
    db.delete(item)
    db.commit()


