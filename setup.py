from setuptools import setup, find_packages



setup(
    name="blessedtext-py",
    version="1.0.0",
    description="A python wrapper for sms.blessedtexts.com API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Njeru Mtwaiti",
    author_email="newerbandit@proton.me",
    url="https://github.com/njeru-codes/BlessedTextsPy", 
    license="MIT",
    packages=find_packages(), 
    install_requires=[
        # add libibraries here
    ],
    python_requires=">=3.7",
    classifiers=[
    ]
)