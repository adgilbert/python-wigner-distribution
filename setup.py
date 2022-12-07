import setuptools

with open("README.md", "r") as f:
    long_description = f.read()
with open('requirements.txt') as f:
    requirements = f.read().splitlines()
    
setuptools.setup(
     name='wigner',
     version='0.1',
     author="ag",
     long_description=long_description,
     url="https://github.com/adgilbert/python-wigner-distribution",
     packages=['wigner'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
         "Topic :: Scientific/Engineering :: Information Analysis",
         "Topic :: Scientific/Engineering :: Visualization",
         "Intended Audience :: Information Technology",
         "Intended Audience :: Science/Research",
     ],
     install_requires=requirements,
 )

