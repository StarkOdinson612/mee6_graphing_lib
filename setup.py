from distutils.core import setup

setup(
    name="mee6_graphing_lib",  # How you named your package folder (MyLib)
    packages=["mee6_graphing_lib"],  # Cshosse the same as "name"
    version="0.5",  # Start with a small number and increase it with every change you make
    license="MIT",  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description="A library that tracks user progress in the MEE6 discord bot",  # Give a short description about your library
    author="Stark Odinson",  # Type in your name
    author_email="darkknightishaan@gmail.com",  #  # Type in your E-Mail
    url="https://github.com/StarkOdinson612/mee6_graphing_lib",  # Provide either the link to your github or to your website
    download_url="https://github.com/StarkOdinson612/mee6_graphing_lib/archive/refs/tags/v0.5.tar.gz",  # I explain this later on
    keywords=[
        "MEE6",
        "Graphing",
        "Discord",
        "Levelling",
    ],  # Keywords that define your package best
    install_requires=[
        "mee6-py-api",
        "matplotlib",
        "numpy",
    ],  # I get to this in a second
    classifiers=[
        "Development Status :: 4 - Beta",  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",  # Again, pick a license
        "Programming Language :: Python :: 3.9",
    ],
)
