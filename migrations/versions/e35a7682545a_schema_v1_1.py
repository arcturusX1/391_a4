"""schema v1.1

Revision ID: e35a7682545a
Revises: 940cae282cad
Create Date: 2024-12-15 01:10:41.261637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e35a7682545a'
down_revision = '940cae282cad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mechanics', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=100), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mechanics', schema=None) as batch_op:
        batch_op.drop_column('name')

    # ### end Alembic commands ###
