"""Seed initial data

Revision ID: 5c4077aa9ca8
Revises: 3a0ad4758705
Create Date: 2025-05-23 08:00:11.235202

"""
from typing import Sequence, Union
from datetime import datetime
from uuid import uuid4

from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.sql import table, column
from app.models.user import UserRole

# revision identifiers, used by Alembic.
revision: str = '5c4077aa9ca8'
down_revision: Union[str, None] = '3a0ad4758705'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Define table structure for bulk insert
    users = table('users',
        column('uid', sa.Uuid),
        column('email', sa.String),
        column('name', sa.String),
        column('role', sa.Enum(UserRole)),
        column('password', sa.String),
        column('created', sa.DateTime),
        column('updated', sa.DateTime),
    )

    # Insert seed data
    # All passwords are "P@ssw0rd!"
    password_hash = '$2b$12$MUjFO0aqKG669iMeDMwoB.CCSl62Wyn92jNJZhE7t0abKVgkLczWa'

    op.bulk_insert(users, [
        {
            'uid': uuid4(),
            'email': 'w.smithers@snrub-corp.io',
            'name': 'Waylon Smithers',
            'role': UserRole.SUPER_ADMIN,
            'password': password_hash,
            'created': datetime.utcnow(),
            'updated': datetime.utcnow()
        },
        {
            'uid': uuid4(),
            'email': 'c.carlson@snrub-corp.io',
            'name': 'Carl Carlson',
            'role': UserRole.ADMIN,
            'password': password_hash,
            'created': datetime.utcnow(),
            'updated': datetime.utcnow()
        },
        {
            'uid': uuid4(),
            'email': 'c.charlie@snrub-corp.io',
            'name': 'Charlie',
            'role': UserRole.ADMIN,
            'password': password_hash,
            'created': datetime.utcnow(),
            'updated': datetime.utcnow()
        },
        {
            'uid': uuid4(),
            'email': 'l.leonard@snrub-corp.io',
            'name': 'Lenny Leonard',
            'role': UserRole.CREATOR,
            'password': password_hash,
            'created': datetime.utcnow(),
            'updated': datetime.utcnow()
        },
        {
            'uid': uuid4(),
            'email': 'f.grimes@snrub-corp.io',
            'name': 'Frank Grimes',
            'role': UserRole.CREATOR,
            'password': password_hash,
            'created': datetime.utcnow(),
            'updated': datetime.utcnow()
        },
        {
            'uid': uuid4(),
            'email': 'canary.m.burns@snrub-corp.io',
            'name': 'Canary M. Burns',
            'role': UserRole.CREATOR,
            'password': password_hash,
            'created': datetime.utcnow(),
            'updated': datetime.utcnow()
        },
        {
            'uid': uuid4(),
            'email': 'angel.of.death@snrub-corp.io',
            'name': 'Angel of Death',
            'role': UserRole.CREATOR,
            'password': password_hash,
            'created': datetime.utcnow(),
            'updated': datetime.utcnow()
        },
        {
            'uid': uuid4(),
            'email': 't.jankovsky@snrub-corp.io',
            'name': 'Tibor Jankovsky',
            'role': UserRole.VIEWER,
            'password': password_hash,
            'created': datetime.utcnow(),
            'updated': datetime.utcnow()
        },
        {
            'uid': uuid4(),
            'email': 'h.simpson@snrub-corp.io',
            'name': 'Homer Simpson',
            'role': UserRole.VIEWER,
            'password': password_hash,
            'created': datetime.utcnow(),
            'updated': datetime.utcnow()
        },
        {
            'uid': uuid4(),
            'email': 'b.bernie@snrub-corp.io',
            'name': 'Bernie',
            'role': UserRole.VIEWER,
            'password': password_hash,
            'created': datetime.utcnow(),
            'updated': datetime.utcnow()
        }
    ])


def downgrade() -> None:
    # Remove the seed data in downgrade
    op.execute("""
        DELETE FROM users WHERE email IN (
            'w.smithers@snrub-corp.io',
            'c.carlson@snrub-corp.io',
            'c.charlie@snrub-corp.io',
            'l.leonard@snrub-corp.io',
            'f.grimes@snrub-corp.io',
            'canary.m.burns@snrub-corp.io',
            'angel.of.death@snrub-corp.io',
            't.jankovsky@snrub-corp.io',
            'h.simpson@snrub-corp.io',
            'b.bernie@snrub-corp.io'
        )
    """)
