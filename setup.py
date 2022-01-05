from pathlib import Path
from setuptools import setup

from celery_chunkificator import __version__


current_directory = Path(__file__).parent
long_description = (current_directory / "README.md").read_text()


packages = ['celery_chunkificator']


setup(
    name='celery-chunkify-task',
    version=__version__,
    description="Efficient celery tasks chunkification",
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='python, celery,',
    author='Oleg Churkin',
    url='http://github.com/ReznikovRoman/celery-chunkify-task',
    license='BSD',
    packages=packages,
    zip_safe=False,
    install_requires=[
        'celery>=4.2.0',
        'structlog>=20.1.0',
    ],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: Web Environment",
    ],
    test_suite='tests',
)
