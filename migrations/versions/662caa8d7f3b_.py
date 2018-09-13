"""empty message

Revision ID: 662caa8d7f3b
Revises: 
Create Date: 2018-09-12 08:00:55.780666

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '662caa8d7f3b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('phone_number', sa.String(length=13), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###