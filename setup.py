from setuptools import find_packages,setup
from typing import List

Hypen_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file:
        requirements=file.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if Hypen_E_DOT in requirements:
            requirements.remove(Hypen_E_DOT)
            

setup(
    name='mlproject',
    version='0.0.1',
    author='SriHari',
    author_email='stud.srihari13@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)