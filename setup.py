from setuptools import setup

setup(
    name='wikionterm',
    version='0.1.1',
    py_modules=['wikionterm'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        wikionterm=wikionterm:search
    ''',
)
