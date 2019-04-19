from setuptools import setup

setup(
    name='todoapp',
    packages=['todoapp'],
    include_package_data=True,
    install_requires=[
        'Flask>=1.0.2',
        'Flask-SQLAlchemy>=2.3.2',
        'requests>=2.21'
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
