"""empty message

Revision ID: 860a95a2a667
Revises: 7eb156117f18
Create Date: 2022-05-11 19:53:53.649866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '860a95a2a667'
down_revision = '7eb156117f18'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    #op.drop_column('clientes', 'data_atendimento')
    # ### end Alembic commands ###
    pass

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('clientes', sa.Column('data_atendimento', sa.DATE(), nullable=False))
    # ### end Alembic commands ###