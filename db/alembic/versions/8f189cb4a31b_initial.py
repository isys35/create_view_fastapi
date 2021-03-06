"""Initial

Revision ID: 8f189cb4a31b
Revises: 
Create Date: 2022-03-21 16:53:39.780825

"""
from alembic import op
from fastapi import Depends
import sqlalchemy as sa

from app import get_db


# revision identifiers, used by Alembic.
revision = '8f189cb4a31b'
down_revision = None
branch_labels = None
depends_on = None


INPUT_TYPES = ['callback', 'location', 'text']


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bot',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('token', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('callback',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('input_types',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('value', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('location',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('longitude', sa.Numeric(), nullable=False),
    sa.Column('latitude', sa.Numeric(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('view',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('text', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('input',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('type_id', sa.Integer(), nullable=True),
    sa.Column('callback_id', sa.Integer(), nullable=True),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.Column('phone', sa.String(length=100), nullable=True),
    sa.Column('text', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['callback_id'], ['callback.id'], ),
    sa.ForeignKeyConstraint(['location_id'], ['location.id'], ),
    sa.ForeignKeyConstraint(['type_id'], ['input_types.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('telegram_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_bot', sa.Boolean(), nullable=True),
    sa.Column('first_name', sa.String(length=100), nullable=True),
    sa.Column('last_name', sa.String(length=100), nullable=True),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('language_code', sa.String(length=100), nullable=True),
    sa.Column('can_join_groups', sa.Boolean(), nullable=True),
    sa.Column('can_read_all_group_messages', sa.Boolean(), nullable=True),
    sa.Column('supports_inline_queries', sa.Boolean(), nullable=True),
    sa.Column('bot_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['bot_id'], ['bot.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('state',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('view_id', sa.Integer(), nullable=True),
    sa.Column('input_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['input_id'], ['input.id'], ),
    sa.ForeignKeyConstraint(['parent_id'], ['state.id'], ),
    sa.ForeignKeyConstraint(['view_id'], ['view.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    db = Depends(get_db)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('state')
    op.drop_table('telegram_user')
    op.drop_table('input')
    op.drop_table('view')
    op.drop_table('location')
    op.drop_table('input_types')
    op.drop_table('callback')
    op.drop_table('bot')
    # ### end Alembic commands ###
