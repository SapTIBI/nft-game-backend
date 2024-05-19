from abc import ABC, abstractmethod

class AbstractRepository(ABC):
    @abstractmethod
    def create_one():
        raise NotImplementedError
    
    @abstractmethod
    def get_one_by_id():
        raise NotImplementedError
    
    @abstractmethod
    def get_all():
        raise NotImplementedError

    @abstractmethod
    def update_one():
        raise NotImplementedError
    
    @abstractmethod
    def delete_one():
        raise NotImplementedError
#
# class SQLAlchemyRepository(AbstractRepository):
#     # model = None

#     # def create_one(self, data: dict) -> int:
#     #     with get_db() as session:
#     #         db_object = self.model(**data)
#     #         session.add(db_object)
#     #         session.commit()
#     #         session.refresh(db_object)
#     #         return db_object.id
#     #         # stmt = insert(self.model).values(**data)
#     #         # res = session.execute(stmt)
#     #         # session.commit()
#     #         # return res.lastrowid  
            
#     # def get_one_by_id(self, id: int):
#     #     with get_db() as session:
#     #         db_object = session.query(self.model).filter_by(id=id).first()
#     #         return db_object
            
#     # def get_all(self, pagination):
#     #     with get_db() as session:
#     #         db_object = session.query(self.model).limit(pagination.limit).offset(pagination.offset)
#     #         return db_object
    
#     # def update_one(self, data: dict) -> int:
#     #     with get_db() as session:
#     #         stmt = insert(self.model).values(**data)
#     #         res = session.execute(stmt)
#     #         session.commit()
#     #         return res.rowcount
    
#     # def delete_one(self):
#     #     with get_db() as session:
#     #         stmt = select(self.model)
#     #         res = session.execute(stmt)
#     #         res = [row[0].to_read_model() for row in res.all()]
#     #         return res.rowcount
    
