from setuptools import setup

def readme():
    with open('README.rst', encoding="utf8") as readme_file:
        return readme_file.read()

setup(
  name = 'crudatalab',
  packages = ['crudatalab'],
  version = '1.3.1',
  description = "Official Python package for CRU DataLab's API",
  long_description=readme(),
  author = 'CRU International Limited',
  author_email = 'alex.kulikov@crugroup.com',
  license='MIT',
  url = 'https://github.com/crugroup/cru-datalab',
  keywords = ['API', 'crudatalab'],
  classifiers = ['Development Status :: 5 - Production/Stable', 'Programming Language :: Python :: 3 :: Only'],
  install_requires=['pandas>=2.0.0', 'pytest-shutil==1.7.0']
)