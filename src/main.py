from pydantic import BaseModel

from fastapi import FastAPI, Depends

from sqlalchemy.orm import Session

from database.database import SessionLocal, engine, Base
from database import models

Base.metadata.create_all(bind=engine)

app = FastAPI()

class OrderCreate(BaseModel):
    user_name: str
    user_email: str
    description: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/pedidos")
def order(db: Session = Depends(get_db)):
    db_order = db.query(models.Order).all()

    orders = [{"id": order.id, "username": order.user_name, "email": order.user_email, "description": order.description} for order in db_order]
    
    return {"pedidos": orders}

@app.post("/pedidos")
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    
    new_order = models.Order(user_name=order.user_name, user_email= order.user_email, description=order.description)

    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return {"message": "Order created successfully", "order": new_order}

@app.put("/pedidos/{order_id}")
def update_order(order_id: int, order_update: OrderCreate, db: Session = Depends(get_db)):

    order = db.query(models.Order).filter(models.Order.id == order_id).first()

    order.user_name = order_update.user_name
    order.user_email = order_update.user_email
    order.description = order_update.description
    db.commit()
    db.refresh(order)

    return {"message": f"Order {order_id} updated successfully"}

@app.delete("/pedidos/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):

    order = db.query(models.Order).filter(models.Order.id == order_id).first()

    db.delete(order)
    db.commit()

    return {"message": f"Task {order_id} deleted successfully"}