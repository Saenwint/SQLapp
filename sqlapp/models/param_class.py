from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base

class ParamClass(Base):
    __tablename__ = "param_class"

    id = Column(Integer, primary_key=True)
    min_value = Column(Integer)
    max_value = Column(Integer)
    param_id = Column(Integer, ForeignKey('param.id'))
    prodclass_id = Column(Integer, ForeignKey('prod_class.id'))

    param = relationship("Param")
    prod_class = relationship("ProdClass")


    def __repr__(self):
        return f"ParamClass(id={self.id}, id_Параметра={self.param_id}, id_Класса={self.prodclass_id}, Мин. знач.={self.min_value}, Макс. знач.={self.max_value})"
