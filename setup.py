from setuptools import find_packages, setup

setup(
    name='coral_client',
    version='1.0.0',
    packages=find_packages(),
    url='https://bitbucket.org/gokhankaraboga/project1_coral_client',
    license='GPL',
    author='Gokhan Karaboga',
    author_email='gokhan.karaboga@metglobal.com',
    description='Hotelspro api client',
    install_requires=['requests', 'base64'],
    classifiers=(
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
)
