import setuptools
from distutils.core import setup, Extension
from Cython.Build import cythonize

with open('README.md', 'r') as f:
      long_description = f.read()

setup(name='Functional Extensions',
      version='0.0.31',
      author='Jonas Reinhardt',
      author_email='jonas@reinhardt.ai',
      description='Functional extensions for Python objects',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/ReinhardtJ/Functional-Extensions',
      project_urls={
            "Bug Tracker": "https://github.com/ReinhardtJ/Functional-Extensions/issues",
      },
      classifiers=['Programming Language :: Python :: 3',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent'],
      package_dir={'': 'src'},
      packages=setuptools.find_packages(where="src"),
      python_requires=">=3.7"
)