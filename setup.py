from setuptools import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup (
    name = "Langton-project",
    version = "0.3",
    description = "Study of cellular automata",
    long_description = read("README.md"),
    author = "CHALAMET Victor",
    author_email = "victorchalamet@gmail.com",
    packages = ["Langton_project", "Langton_project_interface"],
    license = "MIT",
    url = "https://github.com/victorchalamet/Langton_project",
    download_url = "https://github.com/victorchalamet/Langton_project/archive/refs/tags/v_0.3.tar.gz",
    keywords = ["emergence", "animation", "data"],
    install_requires = [
        "numpy",
        "datetime",
        ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10'
    ]
)