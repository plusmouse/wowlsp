from setuptools import setup

setup(
    name="wowlsp",
    version="0.0",
    packages=['wowlsp'],
    description="An LSP implementation targetting WoW AddOn developers",
    author="plusmouse",
    author_email="plusmouse@protonmail.com",
    install_requires=[
        "luaparser",
        "python-jsonrpc-server",
        'ujson'
    ]
)
