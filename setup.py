from setuptools import setup
import setuptools

setup(name = 'serialDevUtil',
      version = '0.9.1',
      author = 'OpenZSD',
      author_email = 'open@z-softdevelopment.com',
      description = 'A simple util to find known devices for serial communication',
      url = 'https://github.com/OpenZSD/serialUtil',
      package_dir = { 'serialDevUtil': 'serialDevUtil' },
      packages = setuptools.find_packages(),
      package_data = {
        'serialDevUtil':['device.json']
      },
      install_requires=['pyserial'])

