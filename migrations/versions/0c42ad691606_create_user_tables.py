"""create account tables

Revision ID: 0c42ad691606
Revises:
Create Date: 2023-10-18 07:01:33.536063

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "0c42ad691606"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """

    CREATE TABLE "user" (
        id SERIAL PRIMARY KEY,
        email VARCHAR(120) UNIQUE NOT NULL,
        name VARCHAR(80),
        password VARCHAR(255) NOT NULL
    );

    CREATE TABLE auction (
        id SERIAL PRIMARY KEY,
        auid INTEGER NOT NULL,
        zip_code VARCHAR(10),
        market_price FLOAT,
        price FLOAT,
        state VARCHAR(50) NOT NULL,
        photo VARCHAR(255),
        description VARCHAR(255) NOT NULL,
        sqft FLOAT,
        fetch_page BOOLEAN,
        date_start TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        date_end TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        city VARCHAR(255) NOT NULL
    );

    CREATE TABLE user_req (
        id SERIAL PRIMARY KEY,
        user_id INTEGER NOT NULL,
        zip_code VARCHAR(10) NOT NULL,
        sqft_price FLOAT NOT NULL,
        min_sqft FLOAT NOT NULL
    );


    """
    )