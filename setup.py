import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mlatticeabc",
    version="0.0.1",
    long_description=long_description,
    # long_description_content_type="text/markdown",
    url="https://github.com/mlatticeabc",
    # packages=['mlatticeabc'],
    # package_dir={'roost': 'roost'},
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
    ],
)