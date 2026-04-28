"""Add is_active to companies

Revision ID: add_company_is_active
Revises: 762e095bdba4
Create Date: 2026-04-28

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = 'add_company_is_active'
down_revision = '762e095bdba4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('companies', sa.Column('is_active', sa.Boolean(), nullable=False, server_default='true'))


def downgrade() -> None:
    op.drop_column('companies', 'is_active')