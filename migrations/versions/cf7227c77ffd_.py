"""empty message

Revision ID: cf7227c77ffd
Revises: e4a7234c2bfe
Create Date: 2023-06-30 18:37:45.523333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf7227c77ffd'
down_revision = 'e4a7234c2bfe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('home_post', schema=None) as batch_op:
        batch_op.alter_column('latitude',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)
        batch_op.alter_column('longitude',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('home_post', schema=None) as batch_op:
        batch_op.alter_column('longitude',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)
        batch_op.alter_column('latitude',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)

    # ### end Alembic commands ###