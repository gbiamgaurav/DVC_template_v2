from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "DVC_template_v2" # github repo name
AUTHOR_USER_NAME = "gbiamgaurav" # update as per your need
SRC_REPO = "DVC_template_v2" # example sklearn etc
LIST_OF_REQUIREMENTS = [] # core dependencies


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="gaurav.bhattacharya10@gmail.com",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)