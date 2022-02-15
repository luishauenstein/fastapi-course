"""add user table

Revision ID: 780401e05163
Revises: d265e1646a71
Create Date: 2022-02-14 23:01:51.726325

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '780401e05163'
down_revision = 'd265e1646a71'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('passsword', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
