import nox

@nox.session(tags=["style", "fix"])
def black(session):
    session.run("black", "PyPSA-GB")

@nox.session(tags=["style", "fix"])
def isort(session):
    session.run("isort", "PyPSA-GB")

@nox.session(tags=["style", "fix"])
def flake8(session):
    session.run("flake8", "PyPSA-GB")

@nox.session(tags=["style", "fix"])
def autopep8(session):
    session.run("autopep8", "PyPSA-GB", "--in-place", "-r")

