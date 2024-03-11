import setuptools

with open("README.md", 'r', encoding='utf-8') as f:
    long_desription = f.read()


__version__ = "0.0.0"

REPO_NAME = "Text-Summerizer-Project"
AUTHOR_USER_NAME = "sesna-tomy"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "sesnatomy1999@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description="A python package for NLP app",
    long_description=long_desription,
    long_description_content="text/markdown",
    url=f"https://github.com?{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={"Bug Tracker": f"https://github/{AUTHOR_USER_NAME}/{REPO_NAME}",
    },
    package_dir={"":"scr"},
    packages=setuptools.find_packages(where="scr")    
    )
