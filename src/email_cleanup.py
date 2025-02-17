"""Cleanup Emails"""

import subprocess
from datetime import datetime, timedelta
from loguru import logger
from database import CleanupTask


def delete_old_emails(task: CleanupTask):
    """Delete emails older than a specified number of days for each user."""

    query_by = task.query_by
    query_data = task.query_data
    days_to_keep = int(task.days_to_keep)
    user_email = task.user_email

    if query_by == "subject":
        search_criteria = f"SUBJECT {query_data}"
    elif query_by == "sender":
        search_criteria = f"FROM {query_data}"
    else:
        raise ValueError(f"Invalid query_by value: {query_by}")

    # Execute the doveadm expunge command
    purge = subprocess.run(
        [
            "doveadm",
            "expunge",
            "-u",
            user_email,
            "mailbox",
            task.mailbox,
            search_criteria,
            "SENTBEFORE",
            f"{task.days_to_keep}d",
        ],
        check=False,
        capture_output=True,
    )

    if purge.returncode != 0:
        logger.error(f"Failed to delete emails for {user_email}: {purge.stderr.decode().strip()}")
    else:
        logger.success(purge.stdout.decode().strip())

    logger.success(f"Deleted emails older than {days_to_keep} days for {user_email}.")
    logger.debug(f"Search criteria: {search_criteria}")
    logger.debug(f"Days to keep: {days_to_keep}")
    logger.debug(f"User email: {user_email}")
    logger.debug(f"Query by: {query_by}")
    logger.debug(f"Query data: {query_data}")
