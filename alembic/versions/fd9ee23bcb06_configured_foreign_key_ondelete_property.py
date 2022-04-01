"""configured foreign key ondelete property

Revision ID: fd9ee23bcb06
Revises: 9a915803927d
Create Date: 2022-04-01 15:28:04.035775

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fd9ee23bcb06'
down_revision = '9a915803927d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_comments_id', table_name='comments')
    op.drop_table('comments')
    op.drop_constraint('articles_ibfk_1', 'articles', type_='foreignkey')
    op.create_foreign_key(None, 'articles', 'users', ['author_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'articles', type_='foreignkey')
    op.create_foreign_key('articles_ibfk_1', 'articles', 'users', ['author_id'], ['id'])
    op.create_table('comments',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('body', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('created_at', sa.DATE(), nullable=True),
    sa.Column('author_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('article_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['article_id'], ['articles.id'], name='comments_ibfk_2'),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], name='comments_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_comments_id', 'comments', ['id'], unique=False)
    # ### end Alembic commands ###
