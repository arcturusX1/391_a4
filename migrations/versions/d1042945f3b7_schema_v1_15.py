"""schema v1.15

Revision ID: d1042945f3b7
Revises: c6a47838d7da
Create Date: 2024-12-15 17:57:23.402534

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1042945f3b7'
down_revision = 'c6a47838d7da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mechanics', schema=None) as batch_op:
        batch_op.add_column(sa.Column('appt_number', sa.Integer(), nullable=False))
        batch_op.drop_column('apt_number')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mechanics', schema=None) as batch_op:
        batch_op.add_column(sa.Column('apt_number', sa.INTEGER(), nullable=False))
        batch_op.drop_column('appt_number')

    # ### end Alembic commands ###