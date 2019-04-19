from setuptools import setup

setup(
    name='todoapp',
    packages=['todoapp'],
    include_package_data=True,
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy',
        'psycopg2'
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
