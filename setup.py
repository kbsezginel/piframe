"""
Raspberry PI Frame.
"""
from setuptools import setup, find_packages


setup(
    name="piframe",
    version="0.1.0",
    description="Raspberry PI Frame",
    author="Kutay B. Sezginel",
    author_email="kutaybs@gmail.com",
    url='https://github.com/kbsezginel/piframe',
    include_package_data=True,
    packages=find_packages(),
    install_requires=['pygame', 'imageio'],
    entry_points={
        'console_scripts': ['piframe=piframe.main']
    }
)
