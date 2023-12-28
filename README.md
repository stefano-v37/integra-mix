# integra-mix
Python calculator to identify the best set of a commercial list of commercial integrators to satisfy selected micronutrients

### installation

The development is being done using pyenv + venv as python manager on WSL running Ubuntu 22.04 on Windows 11.

 - pyenv to select the python version and eventually a specific environment

        pyenv install 3.11.6
        pyenv virtualenv 3.11.6 3.11.6\integra_mix
 
 - venv to generate the environment for testing and CI

        make create-venv

A `.tool-versions` is added for `asdf` support.

 - Install the requirements on your chosen environment
        
        make install-requirements

  - Install the package in editable mode

        pip install -e .
