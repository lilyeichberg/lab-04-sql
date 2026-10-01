"""Read MOCK_DATA.csv, clean it, and upload it to a MySQL database."""

import logging
import os

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# Log timestamps and levels so each step's status is easy to follow
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

# Database connection settings come from environment variables
DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")


def read_data(filename):
    """Load a CSV file into a pandas DataFrame and return it."""
    logger.info("Reading %s", filename)
    data = pd.read_csv(filename)
    logger.info("Read %d rows and %d columns", *data.shape)
    return data


def clean_data(data):
    """Remove rows with missing values and return the cleaned DataFrame."""
    logger.info("Cleaning data")
    before = len(data)
    # Drop any row that has at least one missing value
    cleaned = data.dropna()
    logger.info("Dropped %d rows with missing values", before - len(cleaned))
    return cleaned


def load_data(data, table):
    """Write the DataFrame to the given MySQL table, creating it if needed."""
    logger.info("Uploading %d rows to table '%s'", len(data), table)
    engine = None
    try:
        # URL.create handles special characters in the password safely
        url = URL.create(
            "mysql+mysqlconnector",
            username=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            database=DB_NAME,
        )
        engine = create_engine(url)
        # to_sql creates the table if it doesn't exist, then appends the rows
        data.to_sql(table, engine, if_exists="append", index=False)
        logger.info("Upload to '%s' succeeded", table)
    except Exception:
        logger.exception("Upload to '%s' failed", table)
    finally:
        # Always release the connection pool, even after an error
        if engine is not None:
            engine.dispose()


def main():
    """Run the full pipeline: read, clean, then load into the 'mock' table."""
    data = read_data("MOCK_DATA.csv")
    data = clean_data(data)
    load_data(data, "mock")


if __name__ == "__main__":
    main()
