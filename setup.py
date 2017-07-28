from setuptools import setup, find_packages

setup(
    name='qtsass',
    version='0.1',
    description='Compile an SCSS/SASS stylesheet file to valid Qt CSS',

    packages=find_packages(),
    install_requires=['libsass', 'watchdog'],

    entry_points={
        'console_scripts': [
            'qtsass=qtsass:run',
        ]
    },
)
