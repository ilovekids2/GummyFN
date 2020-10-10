from setuptools import setup, find_packages

setup(
    name = 'GummyFN',
    version = '0.0.1',
    description = 'a lobby bot coding for GummyFN',
    url = '',
    author_email = 'gummyloo2018@gmail.com',
    packages = find_packages(),
    license='MIT',
    install_requires = ['aiohttp', 'bitstring']
)