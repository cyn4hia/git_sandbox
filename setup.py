from setuptools import find_packages, setup

def get_requirements(path: str):
    return [l.strip() for l in open(path)]

setup(
    name='copilot-package-name',
    version='1.0',
    author='Your Name',
    author_email='your-email@example.com',
    description='A short description of your package',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
