"""adding fk game_id to Position

Revision ID: 1a502a700d4d
Revises: 79ddfa9b7420
Create Date: 2022-04-28 15:06:01.689947

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a502a700d4d'
down_revision = '79ddfa9b7420'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('positions', sa.Column('game_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'positions', 'games', ['game_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'positions', type_='foreignkey')
    op.drop_column('positions', 'game_id')
    # ### end Alembic commands ###
