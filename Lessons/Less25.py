from sqlalchemy import create_engine, Column,Integer,String,Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base= declarative_base()

class User(Base):
    __tablename__="user"
    id = Column(Integer,Sequence("user_id_seq"),primary_key=True)
    name= Column (String(50))
    age = Column(Integer)

engine = create_engine("sqlite:///:memory:", echo=True)
Base.metadata.create_all(bind=engine)
Session= sessionmaker(bind=engine)
session=Session()

person1=User (name="Python,", age=50)
person2 = User (name="Java", age =60)
person3= User (name="Ivan", age=44)
person4=User(name="Kate", age=25)

session.add_all({person1,person2,person3,person4})
session.commit()

persons= session.query(User).all()
for person in persons:
    print(f"персонаж: {person.id}, по имени {person.name}, возрастом {person.age}")