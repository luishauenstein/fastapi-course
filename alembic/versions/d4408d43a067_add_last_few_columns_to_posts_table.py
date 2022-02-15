"""add last few columns to posts table

Revision ID: d4408d43a067
Revises: 8c9c1c926fdd
Create Date: 2022-02-14 23:50:04.686899

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4408d43a067'
down_revision = '8c9c1c926fdd'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean,
                  nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(
        timezone=True), nullable=False,  server_default=sa.text("NOW()")))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass