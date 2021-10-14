from setuptools import find_packages, setup

setup(
    name='notifierbot',
    packages=find_packages(include=['notifierbot']),
    version='0.1.0',
    description='Python Library for different Notification Bots',
    author='Sakshay Mahna',
    license='MIT',
    install_requires=['requests'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'requests'],
    test_suite='tests',
)