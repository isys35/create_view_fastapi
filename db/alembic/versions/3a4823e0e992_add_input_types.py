"""add input types

Revision ID: 3a4823e0e992
Revises: 8f189cb4a31b
Create Date: 2022-04-04 16:06:43.249192

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a4823e0e992'
down_revision = '8f189cb4a31b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('phone',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('value', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('text',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('value', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('input', sa.Column('phone_id', sa.Integer(), nullable=True))
    op.add_column('input', sa.Column('text_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'input', 'phone', ['phone_id'], ['id'])
    op.create_foreign_key(None, 'input', 'text', ['text_id'], ['id'])
    op.drop_column('input', 'phone')
    op.drop_column('input', 'text')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('input', sa.Column('text', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('input', sa.Column('phone', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    # TODO: Разобраться с  drop_constraint, нужно использовать нормальную IDE
    # op.drop_constraint('phone', 'input', type_='foreignkey')
    # op.drop_constraint('text', 'input', type_='foreignkey')
    op.drop_column('input', 'text_id')
    op.drop_column('input', 'phone_id')
    op.drop_table('text')
    op.drop_table('phone')
    # ### end Alembic commands ###
