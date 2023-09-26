# from setuptools import find_packages, setup
# from typing import List
# # shows all the requirements
# HYPEN_E_DOT ='-e .'

# def get_requirements(file_path:str)->List[str]: #has all the required packages
#     '''
#     this function will return the list of requirements 
#     '''
#     requirements = []
#     with open(file_path) as file_obj: # open the file who's path is given and save it as a temporary variable
#         requirements = file_obj.readlines()#read the lines in the given fil, but also reads the "\n" after every  line so we need to remove that manually
#         requirements=[req.replace("\n"," ") for req in requirements]
#         if HYPEN_E_DOT in requirements:
#             requirements.remove(HYPEN_E_DOT)
#     return requirements

from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup( #all the parameters that are required
name = 'ml_project',
version = '0.0.1',
author = 'rajat',
author_email = 'rajatgoswami7333@gmail.com',
packages = find_packages(),
# install_requires = get_requirements('requirements.txt')
install_requires = get_requirements('requirements.txt')
)
