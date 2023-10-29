"""init

Revision ID: 0e008629e844
Revises: 
Create Date: 2023-06-28 19:40:02.240970

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e008629e844'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hardware',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cpu', sa.String(), nullable=False),
    sa.Column('capacity_of_ram', sa.String(), nullable=False),
    sa.Column('capacity_of_disk', sa.String(), nullable=False),
    sa.Column('status', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpu')
    )
    op.create_table('server',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hardware_id', sa.Integer(), nullable=True),
    sa.Column('ip_address', sa.String(), nullable=False),
    sa.Column('operating_system', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['hardware_id'], ['hardware.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('ip_address')
    )
    op.create_table('tariff',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('price', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('server_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['server_id'], ['server.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('description'),
    sa.UniqueConstraint('price')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('tariff_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('hashed_password', sa.String(length=1024), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['tariff_id'], ['tariff.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name')
    )
    op.create_table('payment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('tariff_id', sa.Integer(), nullable=True),
    sa.Column('price', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['tariff_id'], ['tariff.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('payment')
    op.drop_table('user')
    op.drop_table('tariff')
    op.drop_table('server')
    op.drop_table('hardware')
    # ### end Alembic commands ###
