"""Add reserves

Revision ID: b00542b97622
Revises: 
Create Date: 2019-07-19 22:30:02.431345

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b00542b97622'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('phoneNumber', sa.String(length=255), nullable=False),
    sa.Column('ssn', sa.String(length=100), nullable=True),
    sa.Column('role', sa.String(length=100), nullable=True),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('passwordHash', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phoneNumber'),
    sa.UniqueConstraint('ssn'),
    sa.UniqueConstraint('username')
    )
    op.create_table('business',
    sa.Column('businessID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('managerID', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['managerID'], ['user.id'], ),
    sa.PrimaryKeyConstraint('businessID')
    )
    op.create_table('service',
    sa.Column('serviceID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('employerID', sa.Integer(), nullable=False),
    sa.Column('businessID', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['businessID'], ['business.businessID'], ),
    sa.ForeignKeyConstraint(['employerID'], ['user.id'], ),
    sa.PrimaryKeyConstraint('serviceID')
    )
    op.create_table('timeTable',
    sa.Column('timeTableID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('serviceID', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['serviceID'], ['service.serviceID'], ),
    sa.PrimaryKeyConstraint('timeTableID')
    )
    op.create_table('time',
    sa.Column('timeID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('startTime', sa.String(length=40), nullable=False),
    sa.Column('endTime', sa.String(length=40), nullable=False),
    sa.Column('timeTableID', sa.Integer(), nullable=False),
    sa.Column('capacity', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['timeTableID'], ['timeTable.timeTableID'], ),
    sa.PrimaryKeyConstraint('timeID')
    )
    op.create_table('reserves',
    sa.Column('userID', sa.Integer(), nullable=False),
    sa.Column('timeID', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['timeID'], ['time.timeID'], ),
    sa.ForeignKeyConstraint(['userID'], ['user.id'], ),
    sa.PrimaryKeyConstraint('userID', 'timeID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reserves')
    op.drop_table('time')
    op.drop_table('timeTable')
    op.drop_table('service')
    op.drop_table('business')
    op.drop_table('user')
    # ### end Alembic commands ###
