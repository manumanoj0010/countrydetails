from setuptools import setup

# version of the software from Countrydetails/version.py
exec(compile(open('Countrydetails/version.py').read(), 'Countrydetails/version.py', 'exec'))

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


keywords = ['country', 'countrydetails', 'countryinfo', 'country information' ,'country data' ,'json']

setup(
    name="Countrydetails",
    version= __version__,
    description="A Python package to get weather reports for any location.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    contact_email = 'manumanoj0010@gmail.com',
    url="",
    author="Manoj Boddu",
    author_email="manumanoj0010@gmail.com",
    keywords = keywords,
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["Countrydetails"], #modules 
    include_package_data=True,
    install_requires=[""], #3rd party install requirements
    entry_points={
        "console_scripts": [
            "countrydetails=Countrydetails.cli:main",
        ]
    },
)