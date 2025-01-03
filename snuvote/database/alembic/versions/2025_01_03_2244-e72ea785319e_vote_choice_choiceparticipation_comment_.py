"""Vote, Choice, ChoiceParticipation, Comment 추가

Revision ID: e72ea785319e
Revises: 69e6f0a92334
Create Date: 2025-01-03 22:44:08.580754

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'e72ea785319e'
down_revision: Union[str, None] = '69e6f0a92334'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'id',
            existing_type=mysql.INTEGER(),
            type_=sa.BigInteger(),
            existing_nullable=False,
            autoincrement=True)
    op.create_table('vote',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('writer_id', sa.BigInteger(), nullable=False),
    sa.Column('create_datetime', sa.DateTime(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('end_datetime', sa.DateTime(), nullable=False),
    sa.Column('participation_code_required', sa.Boolean(), nullable=False),
    sa.Column('participation_code', sa.String(length=20), nullable=True),
    sa.Column('realtime_result', sa.Boolean(), nullable=False),
    sa.Column('multiple_choice', sa.Boolean(), nullable=False),
    sa.Column('annonymous_choice', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['writer_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('choice',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('vote_id', sa.BigInteger(), nullable=False),
    sa.Column('choice_content', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['vote_id'], ['vote.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('vote_id', sa.BigInteger(), nullable=False),
    sa.Column('writer_id', sa.BigInteger(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_datetime', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['vote_id'], ['vote.id'], ),
    sa.ForeignKeyConstraint(['writer_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('choice_participation',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.Column('choice_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['choice_id'], ['choice.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('choice_participation')
    op.drop_table('comment')
    op.drop_table('choice')
    op.drop_table('vote')
    op.alter_column('user', 'id',
               existing_type=sa.BigInteger(),
               type_=mysql.INTEGER(),
               existing_nullable=False,
               autoincrement=True)
    # ### end Alembic commands ###
