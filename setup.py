from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='templating',
    version='0.0.1',
    description='templating for speech output of voice applications',
    py_modules=['templating'],
    package_dir={'': 'src'},
    author="Leonard Fuechsel (ONSEI GmbH)",
    author_email="leo@onsei.de",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ONSEIGmbH/onsei-templating",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        "PyYAML",
        "Jinja2"
    ],
    extras_require = {
        "dev": [
            "pytest >= 3.7",
            "check-manifest",
            "twine",
        ],
    },
)