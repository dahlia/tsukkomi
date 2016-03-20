import ast
from setuptools import find_packages, setup


def readme():
    try:
        with open('README.rst') as f:
            return f.read()
    except (IOError, OSError):
        return


def get_version():
    filename = 'tsukkomi/__init__.py'
    version = None
    with open(filename, 'r') as f:
        tree = ast.parse(f.read(), filename)
        for node in tree.body:
            if (isinstance(node, ast.Assign) and
                    node.targets[0].id == '__version__'):
                version = ast.literal_eval(node.value)
        if isinstance(version, tuple):
            version = '.'.join([str(x) for x in version])
        return version


install_requires = [
    'setuptools',
]
tests_require = [
    'pytest >= 2.9.0',
]
extras_require = [
    'import-order',
    'flake8'
]


setup(
    name='tsukkomi',
    version=get_version(),
    description='make tsukkomi for python types',
    long_description=readme(),
    url='',
    author='Kang Hyojun',
    author_email='iam.kanghyojun' '@' 'gmail.com',
    license='Public Domain',
    packages=find_packages(exclude=['tests']),
    install_requires=install_requires,
    extras_require={
        'tests': tests_require,
        'extras': extras_require
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
