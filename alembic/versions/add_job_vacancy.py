"""Add vacancy to jobs

Revision ID: add_job_vacancy
Revises: add_company_is_active
Create Date: 2026-04-28

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = 'add_job_vacancy'
down_revision = 'add_company_is_active'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('jobs', sa.Column('vacancy', sa.Integer(), nullable=False, server_default='1'))


def downgrade() -> None:
    op.drop_column('jobs', 'vacancy')