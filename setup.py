import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='teslafolkas',
    version='0.0.1',
    author='Laurynas Grusas',
    author_email='laurynas.grusas@gmail.com',
    description='Homework assignment for DS.2.1.3.',
    long_description=long_description,
    long_description_content_type='ext/markdown',
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
