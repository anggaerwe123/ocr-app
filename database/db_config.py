from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

DATABASE_URL = "postgresql://postgres:achmad1312@localhost:5432/convertdata"
engine = create_engine(
    DATABASE_URL,
    connect_args={"options": "-c timezone=Asia/Jakarta"}
)
Base = declarative_base()

class ProductTable(Base):
    __tablename__ = 'invoice'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_number = Column(String(50))
    description = Column(String(255))
    quantity = Column(Integer)
    unit_price = Column(Float)
    line_total = Column(Float)
    discount = Column(Float)
    createddate = Column(DateTime, default=datetime.now) 

    @classmethod
    def get_all(cls):
        return session.query(cls).all()
    @classmethod
    def delete(cls, id):
        product = session.query(cls).get(id)
        if product:
            session.delete(product)
            session.commit()
            return True
        return False

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()