"""assign groups to all users

Revision ID: 7ddaf5286202
Revises: cbdb6fc2f1ee
Create Date: 2023-03-13 23:54:03.948178

"""
from alembic import op
import sqlalchemy as sa
from pathlib import Path

# revision identifiers, used by Alembic.
revision = '7ddaf5286202'
down_revision = 'cbdb6fc2f1ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('item_market_source_id_fkey', 'item', type_='foreignkey')
    op.create_foreign_key(None, 'item', 'market_source', ['market_source_id'], ['id'])
    op.drop_column('item', 'item_size')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item',
                  sa.Column('item_size', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'item', type_='foreignkey')
    op.create_foreign_key('item_market_source_id_fkey', 'item', 'brand', ['market_source_id'], ['id'])
    # ### end Alembic commands ###
