"""lcmap-rachel is real-time acquisition change evaluation - a research and development project to
map continuous change detections beyond the end dates of stable pyccd models.
"""

from setuptools import setup


def readme():
    with open('README.rst', 'r') as f:
        return f.read()


def version():
    with open('version.txt', 'r') as v:
        return v.read().strip()


setup(
    name='lcmap-rachel',

    version=version(),

    description=__doc__,

    long_description=readme(),

    url='https://github.com/danzelenak-usgs/lcmap-rachel',

    author='USGS EROS LCMAP',

    author_email='dzelenak@contractor.usgs.gov',

    license='Unlicense',

    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: Unlicense',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='usgs eros lcmap pyccd ard',

    packages=['rachel'],

    install_requires=[],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[test]
    extras_require={
        'test': ['pytest',
                 'vcrpy'
                 ],

        'dev': ['']
    },

    # setup_requires='',

    # tests_require='',

    # entry_points='',

    include_package_data=True,

    zip_safe=False

)
