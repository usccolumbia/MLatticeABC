import setuptools

with open("README.md", "r",encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="mlatticeabc",
    version="0.0.1",
    long_description=long_description,
    url="https://github.com/mlatticeabc",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
    ],
)
