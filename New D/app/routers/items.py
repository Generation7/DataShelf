from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import crud, schemas, models
from ..deps import get_db
from ..database import engine, Base


# Ensure tables exist on import
Base.metadata.create_all(bind=engine)


router = APIRouter()


@router.post("/", response_model=schemas.ItemOut, status_code=status.HTTP_201_CREATED)
def create_item(item_in: schemas.ItemCreate, db: Session = Depends(get_db)):
    existing = crud.get_item_by_name(db, item_in.name)
    if existing:
        raise HTTPException(status_code=400, detail="Item with this name already exists")
    return crud.create_item(db, item_in)


@router.get("/{item_id}", response_model=schemas.ItemOut)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = crud.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.get("/", response_model=list[schemas.ItemOut])
def list_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.list_items(db, skip=skip, limit=limit)


@router.put("/{item_id}", response_model=schemas.ItemOut)
def update_item(item_id: int, item_in: schemas.ItemUpdate, db: Session = Depends(get_db)):
    item = crud.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return crud.update_item(db, item, item_in)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = crud.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    crud.delete_item(db, item)
    return None


