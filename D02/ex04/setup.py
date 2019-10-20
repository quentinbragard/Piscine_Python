import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="42ai-pkg-qbragard",
    version="1.0.0",
    author="qbragrd",
    author_email="",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    path=["/Users/qbragard/Piscine_Python/D02/ex04/loading.py","/Users/qbragard/Piscine_Python/D02/ex04/logger.py"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)