from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns the list of requirements
    """
    with open(file_path) as file_object:
        requirements = [req.strip() for req in file_object.readlines()]  # strip newline chars

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='mlopsproject',
    version='0.0.1',
    author='mdabbad',
    author_email='hr591230nc.gamil.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
