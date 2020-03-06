"""empty message

Revision ID: 1e38d94001d1
Revises: 
Create Date: 2019-12-04 21:59:48.074302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e38d94001d1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clientes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=True),
    sa.Column('cpfcnpj', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('produtos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nome')
    )
    op.create_table('contatos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=True),
    sa.Column('telefone', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('principal', sa.Boolean(), nullable=True),
    sa.Column('cliente_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cliente_id'], ['clientes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('enderecos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rua', sa.String(), nullable=True),
    sa.Column('bairro', sa.String(), nullable=True),
    sa.Column('cidade', sa.String(), nullable=True),
    sa.Column('numero', sa.String(), nullable=True),
    sa.Column('complemento', sa.String(), nullable=True),
    sa.Column('estado', sa.String(), nullable=True),
    sa.Column('cliente_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cliente_id'], ['clientes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orcamentos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data_atual', sa.DateTime(), nullable=False),
    sa.Column('data_agendamento', sa.DateTime(), nullable=False),
    sa.Column('data_conclusao', sa.DateTime(), nullable=False),
    sa.Column('data_cancelamento', sa.DateTime(), nullable=True),
    sa.Column('descricao', sa.String(length=200), nullable=False),
    sa.Column('cliente_id', sa.Integer(), nullable=False),
    sa.Column('observacao', sa.String(length=4000), nullable=False),
    sa.ForeignKeyConstraint(['cliente_id'], ['clientes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orcamentos')
    op.drop_table('enderecos')
    op.drop_table('contatos')
    op.drop_table('produtos')
    op.drop_table('clientes')
    # ### end Alembic commands ###
