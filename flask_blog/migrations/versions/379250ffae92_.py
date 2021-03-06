"""empty message

Revision ID: 379250ffae92
Revises: a44a0558978
Create Date: 2015-11-12 14:16:10.542763

"""

# revision identifiers, used by Alembic.
revision = '379250ffae92'
down_revision = 'a44a0558978'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('blog_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('slug', sa.String(length=256), nullable=True),
    sa.Column('publish_date', sa.DateTime(), nullable=True),
    sa.Column('live', sa.Boolean(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['blog_id'], ['blog.id'], ),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    op.alter_column(u'user', 'is_author',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    op.alter_column(u'user', 'password',
               existing_type=mysql.VARCHAR(length=80),
               type_=sa.String(length=60),
               existing_nullable=True)
    op.alter_column(u'user', 'username',
               existing_type=mysql.VARCHAR(length=80),
               type_=sa.String(length=25),
               existing_nullable=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(u'user', 'username',
               existing_type=sa.String(length=25),
               type_=mysql.VARCHAR(length=80),
               existing_nullable=True)
    op.alter_column(u'user', 'password',
               existing_type=sa.String(length=60),
               type_=mysql.VARCHAR(length=80),
               existing_nullable=True)
    op.alter_column(u'user', 'is_author',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.drop_table('post')
    op.drop_table('category')
    ### end Alembic commands ###
