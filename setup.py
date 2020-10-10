from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="GummyFN",
    version="1.0.1",
    description="A Python package to get GummyFN coding for bos",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/ilovekids2/GummyFN",
    author="ilovekids2",
    author_email="gummyloo2018@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["Gummy-FN"],
    include_package_data=True,
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "GummyFN=Gummy-FN:main",
        ]
    },
)