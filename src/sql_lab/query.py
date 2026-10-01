"""Query the 'mock' table in the MySQL database uploaded by process.py."""

import logging
import os

import mysql.connector

# Log timestamps and levels so each step's status is easy to follow
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

# Database connection settings come from environment variables
DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")


def get_connection():
    """Open and return a connection to the MySQL database."""
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
    )


def get_data_by_group(value):
    """Return all rows from 'mock' where the `group` column equals value.

    Filter column: `group` (backticked because GROUP is reserved in MySQL).
    """
    logger.info("Fetching rows where group = %s", value)
    rows = []
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        # Parameterized query: the value is passed separately, never
        # concatenated into the SQL string
        cursor.execute("SELECT * FROM mock WHERE `group` = %s", (value,))
        rows = cursor.fetchall()
        cursor.close()
        logger.info("Found %d rows for group = %s", len(rows), value)
    except mysql.connector.Error:
        logger.exception("Query by group failed")
    finally:
        # Always close the connection, even after an error
        if conn is not None and conn.is_connected():
            conn.close()
    return rows


def plot_counts(groupby):
    """Count rows per distinct value of the column named groupby.

    Returns a list of (value, count) tuples, largest count first.
    """
    logger.info("Counting rows grouped by %s", groupby)
    counts = []
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        # Column names can't be passed as %s parameters, so check that the
        # name is a real column in this table before using it in the SQL
        cursor.execute(
            "SELECT column_name FROM information_schema.columns "
            "WHERE table_schema = %s AND table_name = 'mock'",
            (DB_NAME,),
        )
        valid_columns = [row[0] for row in cursor.fetchall()]
        if groupby not in valid_columns:
            logger.error("'%s' is not a column in mock: %s", groupby, valid_columns)
            return counts
        # Safe to insert now: groupby matched a real column name exactly
        cursor.execute(
            f"SELECT `{groupby}`, COUNT(*) AS n FROM mock "
            f"GROUP BY `{groupby}` ORDER BY n DESC"
        )
        counts = cursor.fetchall()
        cursor.close()
        logger.info("Found %d distinct values in %s", len(counts), groupby)
    except mysql.connector.Error:
        logger.exception("Count query failed")
    finally:
        # Always close the connection, even after an error
        if conn is not None and conn.is_connected():
            conn.close()
    return counts


def main():
    """Demonstrate both query functions and print the results."""
    # Count rows per group and show the result
    counts = plot_counts("group")
    print("Rows per group:")
    for value, n in counts:
        print(f"  {value}: {n}")

    # Use the most common group value to demonstrate the filtered query
    if counts:
        top_group = counts[0][0]
        rows = get_data_by_group(top_group)
        print(f"\nFirst 5 rows where group = {top_group}:")
        for row in rows[:5]:
            print(row)


if __name__ == "__main__":
    main()
