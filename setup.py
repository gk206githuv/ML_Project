from setuptools import setup,find_packages
from typing import List
HYPNENATE = '-e .'
def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]
        if HYPNENATE in requirements:
            requirements.remove(HYPNENATE)
    return requirements





setup(
    name="ML Project",
    version="0.0.1",    
    author="Gaurav",
    author_email="gauravkasaudhan@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)