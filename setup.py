# setup.py is used in ML projects to define dependencies, package metadata, 
# and installation instructions for easy distribution and reproducibility.
from setuptools import find_packages,setup

HYPHEN_E_DON='-e .'  ##Ensures dependencies specified in setup.py are installed.
def get_requirement(filename:str)->list[str]:

    '''this function will return list of requiremnts'''
    
    filename=r"requirements.txt"
    with open(filename) as file_obj:
        requirements=file_obj.readlines()  ## when excute line by line it appened \n end of the line
        requirements=[req.replace('\n','') for req in requirements]

        if HYPHEN_E_DON in requirements:
            requirements.remove(HYPHEN_E_DON)
            
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Satendra Dwivedi',
    author_email='satendradwivedi161@gamil.com',
    packages=find_packages(), ##Ensures that Python recognizes src as a package.
    install_requires=get_requirement("requirements.txt")
    
)
