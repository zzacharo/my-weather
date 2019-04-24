from setuptools import setup

setup(
    name='myweatherapp',
    include_package_data=True,
    packages=['myweatherapp'],
    entry_points={
        'flask.commands': [
            'weather = myweatherapp.cli:cli'
        ]
    },
    install_requires=[
        'Flask>=1.0.2',
        'Flask-SQLAlchemy>=2.3.2',
        'requests>=2.21',
        'simplekv>=0.12.0',
        'redis>=3.2.1'
    ],
    setup_requires=[
        'pytest-runner',

    ],
    tests_require=[
        'pytest',
    ],
)
