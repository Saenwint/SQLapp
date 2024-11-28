from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.base import Base
from models.product import Product
from models.unit import Unit
from models.enumclassifier import EnumClassifier
from models.enumposition import EnumPosition
from models.param import Param
from models.param_class import ParamClass
from models.param_product import ParamProduct
from models.prodclass import ProdClass
from config import settings

engine = create_engine(
        settings.DATABASE_URL,
        echo=True,
)

session_maker = sessionmaker(bind=engine, expire_on_commit=False)

def create_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)