"""add content column to post table

Revision ID: d265e1646a71
Revises: ef31fbdfd1cc
Create Date: 2022-02-14 22:57:49.048062

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd265e1646a71'
down_revision = 'ef31fbdfd1cc'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
