"""Main script to execute email cleanup tasks."""

from loguru import logger
import database_connect as db
from database import get_tasks, CleanupTask
from email_cleanup import delete_old_emails


def main():
    """Main function to execute email cleanup tasks."""
    # Set up the database connection
    session = db.Session()

    # Get all cleanup tasks from the database
    tasks: list[CleanupTask] = get_tasks(session)  # type: ignore
    logger.info(f"Retrieved {len(tasks)} tasks from the database.")
    logger.debug(f"Tasks: {tasks}")

    # Iterate through tasks and perform email cleanup
    for task in tasks:
        # Perform email cleanup based on the task
        delete_old_emails(task)
    session.close()
    print("Email cleanup tasks completed.")
    logger.success("Email cleanup tasks completed.")


if __name__ == "__main__":
    db.Base.metadata.create_all(db.db)
    logger.info("Starting email cleanup tasks...")
    main()
