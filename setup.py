from distutils.core import setup
import os

module_path = os.path.join(os.path.dirname(__file__), 'fabric_verbose.py')
version_line = [line for line in open(module_path)
                if line.startswith('__version_info__')][0]

__version__ = '.'.join(eval(version_line.split('__version_info__ = ')[-1]))

setup(
    name='fabric-verbose',
    py_modules=['fabric_verbose'],
    version=__version__,
    description='fabric-verbose',
    long_description=open('README.rst').read(),
    license='MIT',
    author='Suyeol Jeon',
    author_email='devxoul@gmail.com',
    url='https://github.com/devxoul/fabric-verbose',
    download_url='https://pypi.python.org/packages/source/f/fabric-verbose/'
                 'fabric-verbose-%s.tar.gz' % __version__,
    keywords=['Fabric', 'Verbose'],
    classifiers=[]
)
