"""Database module for managing email cleanup tasks."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from database_connect import Base


class CleanupTask(Base):  # type: ignore
    """
    Represents a cleanup task for managing email retention.

    Attributes:
        id (int): The primary key of the cleanup task.
        user_email (str): The email address of the user.
        days_to_keep (int): The number of days to keep emails.
        query_by (str): The field by which to query emails (e.g., 'subject', 'sender').
        query_data (str): The data to query by (e.g., specific subject or sender).
    """

    __tablename__ = "cleanup_tasks"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_email = Column(String(255), nullable=False)
    days_to_keep = Column(Integer, nullable=False)
    mailbox = Column(String(255), nullable=False, default="INBOX")
    query_by = Column(String(255), nullable=False)
    query_data = Column(String(255), nullable=False)


def get_tasks(session: Session) -> list[CleanupTask]:
    """Get all cleanup tasks from the database."""

    results = session.query(CleanupTask).all()
    session.close()
    return results
