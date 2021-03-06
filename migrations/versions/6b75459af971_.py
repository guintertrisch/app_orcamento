"""empty message

Revision ID: 6b75459af971
Revises: e2296915ab8a
Create Date: 2019-12-04 22:27:30.053729

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b75459af971'
down_revision = 'e2296915ab8a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orcamento_detalhes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quantidade', sa.Integer(), nullable=False),
    sa.Column('valor', sa.Float(precision=5, asdecimal=2), nullable=False),
    sa.Column('acao', sa.String(length=60), nullable=False),
    sa.Column('produto_servico', sa.String(length=15), nullable=False),
    sa.Column('orcamento_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['orcamento_id'], ['orcamentos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orcamento_detalhes')
    # ### end Alembic commands ###
