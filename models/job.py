from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from backend.db.database import Base

class StoryJob(Base):
    __tablename__ = "story_jobs"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(String, index=True, unique =true)
    session_id = Column(String, index=True)
    theme = Column(String)
    status = Column(String)
    story_id = Column(Integer, index=True)
    error = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    complete_job = Column(DateTime(timezone=True), nullable=True)
    