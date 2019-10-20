pip install --upgrade pip   
python3 -m pip install --user --upgrade setuptools wheel
python3 setup.py sdist bdist_wheel
python3 -m pip install --user --upgrade twine
python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
pip install --index-url https://test.pypi.org/project/42ai-pkg-qbragard/1.0.0/ --no-deps 42ai-qbragard  