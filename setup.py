from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

# This call to setup() does all the work
setup(
    name="workflowy-assistant",
    version="0.0.2",
    description="Helps you automate your WorkFlowy.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guidoknoop/workflowy-assistant",
    author="Guido Knoop",
    author_email="guidojurgenknoop@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    py_modules=["workflowy_assistant"],
    install_requires=["selenium", "webdriver_manager"],
    package_dir={'':'src'},
)