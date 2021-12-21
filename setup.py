from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize('src/functional_extensions.py'),
      package_dir={'src': 'src'},
      name='Functional Extensions',
      version='0.0.1',
      author='Jonas Reinhardt',
      author_email='jonas@reinhardt.ai',
      description='Functional extensions for Python objects',
      long_description='file: README.md',
      url='https://github.com/ReinhardtJ/Functional-Extensions',
      classifiers=['Programming Language :: Python :: 3',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent'])