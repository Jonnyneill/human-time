from setuptools import setup, find_packages


def readme():
    with open("README.md") as readmeFile:
        return readmeFile.read()


setup(
    name="human-time",
    version="0.1.1",
    author="Jonathan Neill",
    author_email="jonnyneill@hotmail.com",
    description="Converts digit based time formats to the english language equivalent",
    keywords="talking clock human time",
    license='MIT',
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Jonnyneill/human-time",
    packages=find_packages(),
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    entry_points={
        "console_scripts": [
            "humantime=src.cli_client:main",
            "humantime-server=src.app:start"
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "Operating System :: OS Independent",
    ],
)
