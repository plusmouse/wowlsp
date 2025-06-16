from setuptools import setup

setup(
    name="WoWLSP",
    version="0.0",
    description="An LSP implementation targetting WoW AddOn developers",
    author="plusmouse",
    author_email="plusmouse@protonmail.com",
    install_requires=[
        "luaparser",
        "python-jsonrpc-server",
    ]
)
