import os

DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Change the test IP as you prefer
TEST_IP = "8.8.8.8"

###############################################################################
# DB
###############################################################################

# enable configuring your database uri from system environment
SQLALCHEMY_DATABASE_URI = os.environ.get('MYWEATHERAPP_SQLALCHEMY_DATABASE_URI', 'sqlite:////tmp/test.db' )