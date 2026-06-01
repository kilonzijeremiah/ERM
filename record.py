from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base
from datetime import datetime

class Record(Base):

    __tablename__ = "records"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    category = Column(String)
    filename = Column(String)
    owner = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
