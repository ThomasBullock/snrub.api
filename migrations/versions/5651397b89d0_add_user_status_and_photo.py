"""Add user status and photo

Revision ID: 5651397b89d0
Revises: 5c4077aa9ca8
Create Date: 2026-01-31 05:40:52.810192

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '5651397b89d0'
down_revision: Union[str, None] = '5c4077aa9ca8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create the enum type first
    userstatus_enum = sa.Enum('ACTIVE', 'INACTIVE', 'DECEASED', 'SUSPENDED', name='userstatus')
    userstatus_enum.create(op.get_bind(), checkfirst=True)

    # Add status column with server default for existing rows
    op.add_column('users', sa.Column('status', userstatus_enum, nullable=False, server_default='ACTIVE'))
    op.add_column('users', sa.Column('photo', sa.LargeBinary(), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'photo')
    op.drop_column('users', 'status')

    # Drop the enum type
    sa.Enum(name='userstatus').drop(op.get_bind(), checkfirst=True)
