"""add_visits_count_to_urls

Revision ID: e91a14ba751c
Revises: d3ef123f75ce
Create Date: 2025-11-20 07:00:05.966360

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e91a14ba751c'
down_revision: Union[str, None] = 'd3ef123f75ce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('urls', sa.Column('visits_count', sa.Integer(), nullable=False, server_default='0'))


def downgrade() -> None:
    op.drop_column('urls', 'visits_count')


