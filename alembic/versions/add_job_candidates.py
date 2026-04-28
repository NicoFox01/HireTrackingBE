"""Add total_candidates and filled to jobs

Revision ID: add_job_candidates
Revises: add_job_vacancy
Create Date: 2026-04-28

"""
from alembic import op
import sqlalchemy as sa

revision = 'add_job_candidates'
down_revision = 'add_job_vacancy'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('jobs', sa.Column('total_candidates', sa.Integer(), nullable=True))
    op.add_column('jobs', sa.Column('filled', sa.Boolean(), nullable=True, server_default='false'))


def downgrade() -> None:
    op.drop_column('jobs', 'filled')
    op.drop_column('jobs', 'total_candidates')