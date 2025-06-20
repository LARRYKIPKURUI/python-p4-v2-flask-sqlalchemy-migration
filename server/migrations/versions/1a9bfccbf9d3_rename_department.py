"""rename department

Revision ID: 1a9bfccbf9d3
Revises: 5b0a28bec7c3
Create Date: 2025-06-13 22:19:02.230420

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a9bfccbf9d3'
down_revision = '5b0a28bec7c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address',  new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location',  new_column_name='address')
