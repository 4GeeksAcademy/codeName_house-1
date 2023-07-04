"""empty message

<<<<<<<< HEAD:migrations/versions/42a63f28b4dd_.py
Revision ID: 42a63f28b4dd
Revises: 
Create Date: 2023-07-04 13:39:07.967002
========
Revision ID: acdc3ebc255c
Revises: 
Create Date: 2023-07-04 14:28:36.401191
>>>>>>>> main:migrations/versions/acdc3ebc255c_.py

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
<<<<<<<< HEAD:migrations/versions/42a63f28b4dd_.py
revision = '42a63f28b4dd'
========
revision = 'acdc3ebc255c'
>>>>>>>> main:migrations/versions/acdc3ebc255c_.py
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('skill',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('profile_pic', sa.String(), nullable=True),
    sa.Column('username', sa.String(length=120), nullable=False),
    sa.Column('surname1', sa.String(length=120), nullable=True),
    sa.Column('surname2', sa.String(length=120), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('cmr_profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('phone_number', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pro_profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('verified', sa.Boolean(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('dni', sa.String(length=255), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('address', sa.String(length=200), nullable=True),
    sa.Column('city', sa.String(length=200), nullable=True),
    sa.Column('postal_code', sa.String(), nullable=True),
    sa.Column('km_radius', sa.Numeric(), nullable=True),
    sa.Column('phone_number', sa.String(), nullable=True),
    sa.Column('hourly_rate', sa.Numeric(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('dni')
    )
    op.create_table('user_role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('home',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('address', sa.String(length=200), nullable=True),
    sa.Column('city', sa.String(length=200), nullable=True),
    sa.Column('postal_code', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('cmr_profile_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cmr_profile_id'], ['cmr_profile.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pro_profile_skill',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('skill_id', sa.Integer(), nullable=True),
    sa.Column('pro_profile_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pro_profile_id'], ['pro_profile.id'], ),
    sa.ForeignKeyConstraint(['skill_id'], ['skill.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contract',
    sa.Column('created', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('home_id', sa.Integer(), nullable=True),
    sa.Column('pro_profile_id', sa.Integer(), nullable=True),
    sa.Column('cmr_profile_id', sa.Integer(), nullable=True),
    sa.Column('job_status', sa.Enum('PENDING', 'ACTIVE', 'COMPLETED', 'CANCELED', name='jobstatus'), nullable=True),
    sa.Column('payment_status', sa.Enum('PENDING', 'PAYED', 'REFUNDED', name='paymentstatus'), nullable=True),
    sa.Column('comment', sa.String(length=255), nullable=True),
    sa.Column('starting_time', sa.DateTime(), nullable=False),
    sa.Column('finishing_time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['cmr_profile_id'], ['cmr_profile.id'], ),
    sa.ForeignKeyConstraint(['home_id'], ['home.id'], ),
    sa.ForeignKeyConstraint(['pro_profile_id'], ['pro_profile.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('home_post',
    sa.Column('created', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_visible', sa.Boolean(), nullable=False),
    sa.Column('home_id', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('latitude', sa.String(length=200), nullable=False),
    sa.Column('longitude', sa.String(length=200), nullable=False),
    sa.Column('starting_time', sa.DateTime(), nullable=True),
    sa.Column('finishing_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['home_id'], ['home.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('message',
    sa.Column('created', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=60), nullable=False),
    sa.Column('content', sa.String(length=255), nullable=False),
    sa.Column('message_status', sa.Enum('DRAFT', 'SENT', name='messagestatus'), nullable=True),
    sa.Column('home_id', sa.Integer(), nullable=True),
    sa.Column('sender_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['home_id'], ['home.id'], ),
    sa.ForeignKeyConstraint(['sender_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cmr_review',
    sa.Column('created', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('pro_sender_id', sa.Integer(), nullable=True),
    sa.Column('cmr_receiver_id', sa.Integer(), nullable=True),
    sa.Column('contract_id', sa.Integer(), nullable=True),
    sa.Column('comment', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['cmr_receiver_id'], ['cmr_profile.id'], ),
    sa.ForeignKeyConstraint(['contract_id'], ['contract.id'], ),
    sa.ForeignKeyConstraint(['pro_sender_id'], ['pro_profile.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('message_receiver',
    sa.Column('created', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message_id', sa.Integer(), nullable=True),
    sa.Column('receiver_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['message_id'], ['message.id'], ),
    sa.ForeignKeyConstraint(['receiver_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post_skills',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('skill_id', sa.Integer(), nullable=True),
    sa.Column('homepost_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['homepost_id'], ['home_post.id'], ),
    sa.ForeignKeyConstraint(['skill_id'], ['skill.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pro_review',
    sa.Column('created', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('pro_receiver_id', sa.Integer(), nullable=True),
    sa.Column('cmr_sender_id', sa.Integer(), nullable=True),
    sa.Column('contract_id', sa.Integer(), nullable=True),
    sa.Column('comment', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['cmr_sender_id'], ['cmr_profile.id'], ),
    sa.ForeignKeyConstraint(['contract_id'], ['contract.id'], ),
    sa.ForeignKeyConstraint(['pro_receiver_id'], ['pro_profile.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pro_review')
    op.drop_table('post_skills')
    op.drop_table('message_receiver')
    op.drop_table('cmr_review')
    op.drop_table('message')
    op.drop_table('home_post')
    op.drop_table('contract')
    op.drop_table('pro_profile_skill')
    op.drop_table('home')
    op.drop_table('user_role')
    op.drop_table('pro_profile')
    op.drop_table('cmr_profile')
    op.drop_table('user')
    op.drop_table('skill')
    op.drop_table('role')
    # ### end Alembic commands ###
