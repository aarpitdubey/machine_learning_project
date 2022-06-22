from setuptools import setup, find_packages
from typing import List

# Declaring variables for setup function
PROJECT_NAME="housing-predictor"
VERSION="0.0.3"
AUTHOR="Arpit Dubey"
DESCRIPTION="This is the first ML Project for FSDS Nov 2021 batch"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"


def get_requirements_list()->List[str]:
    """
    ["numpy", "pandas"] -> List[str]

    Description: This function is going to return list of requirement
    mention in requirements.txt file

    return: This function is going to return a list which contain name 
    of libraries mentioned in reuirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup (
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(), #PACKAGES
    install_requires=get_requirements_list()

)

# if __name__=="__main__":
#     prit(get_requirements_list())