import os

from setuptools import find_packages
from setuptools import setup

name = 'shupcast'
version = '0.1'

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()
except IOError:
    README = CHANGES = ''


setup(
    name=name,
    version=version,
    description="Addon for shupcast site",
    long_description='\n\n'.join([README, CHANGES]),
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Topic :: Documentation",
        "Topic :: Software Development :: Documentation",
    ],
    keywords='shupcast kotti podcast',
    author='Vanc Levstik',
    author_email='vanc.levstik@gmail.com',
    url='https://github.com/ferewuz/podcast-site',
    license='BSD',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "Kotti",
    ],
    entry_points={
        'fanstatic.libraries': [
            'shupcast = shupcast:library',
            ],
    },
)
