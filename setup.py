from setuptools import setup

setup(
    name="wow_ls",
    version="0.0",
    packages=['wow_ls'],
    description="An LSP implementation targetting WoW AddOn developers",
    author="plusmouse",
    author_email="plusmouse@protonmail.com",
    install_requires=[
        "luaparser",
        "python-jsonrpc-server",
        'ujson'
    ]
)
