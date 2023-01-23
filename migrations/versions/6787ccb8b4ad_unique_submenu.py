"""unique submenu

Revision ID: 6787ccb8b4ad
Revises: 56e02843d821
Create Date: 2023-01-17 23:40:13.968985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6787ccb8b4ad'
down_revision = '56e02843d821'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_submenus_title', table_name='submenus')
    op.create_index(op.f('ix_submenus_title'), 'submenus', ['title'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_submenus_title'), table_name='submenus')
    op.create_index('ix_submenus_title', 'submenus', ['title'], unique=False)
    # ### end Alembic commands ###