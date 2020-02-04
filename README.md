Template project in python
======================
> Template project in python with simple logger,
> app configuration solution, gitignore, CI/CD Jenkinsfile, 
> command line entry point, versioning, packaging with setuptools,
> contenerization with docker, test with pytest, and package publishing script to gemfury.

### Structure
    .
    ├── config.json                             #configuration file for the app folder above virtual env
    ├── Dockerfile                              #Dockerfile running the app on start
    ├── Dockerfile_python                       #Dockerfile with python and tmpuser for Jenkins
    ├── Jenkinsfile                             #Jenkinsfile for CI/CD setup
    ├── MANIFEST.in                             #Additional files for packaging with setuptools
    ├── python_template                         #Package main directory
    │   ├── config.json                         #default configruation file
    │   ├── config.py                           #configuration parser
    │   ├── data                                #folder for data (should be configured with config.json)
    │   │   └── __init__.py
    │   ├── entry_points.py                     #Application entry points for setuptools to run app by single cmd command
    │   ├── __init__.py
    │   ├── logging_manager.py                  #Logging solution
    │   ├── logs                                #Folder with log (should be cofigured with config.json)
    │   │   ├── __init__.py
    │   │   └── steam_explorer_model.log        #log file (non versioned)
    │   ├── python_template_source.py           #example source file
    │   ├── tests                               #folder with tests
    │   │   ├── __init__.py
    │   │   └── test_python_template.py         #example test testing python_template_source.py
    │   └── VERSION                             #version number
    ├── README.md                               #this file
    ├── requirements.txt                        #necessary python packages to run the project
    ├── scripts                                 
    │   └── publish_to_gemfury.sh
    └── setup.py                                #setuptools setup.py file

### Proposed git wokrflow with CI/CD
#### Git workflow
Variation on GitLab Flow with 3 branches reflecting 3 environments.

master as development branch (On push Jenkins deploys to production environment and publish the artifact)
stage as testing/staging/preproduction (On push Jenkins deploys to staging environment)
production as production env (On push Jenkins deploys to production environment)

#### Jenkins
To run CI/CD you need machine with Jenkins.

To enable Jenkins automated runs webhooks must be set up. To set up webhooks on github go to project `Settings` on and select `Webhooks`.
Set up `Payload Url` to point to `github-webhook` endpoint on your machine with Jenkins.
   
    http://your.machine.with.jenkins:yourport/github-webhook/
    
To enable automated runs on pull requests 
under `Which events would you like to trigger this webhook` select 
`Let me select individual events` and pick `Pushes` and `Pull requests`

Now jenkins runs automated tests on every push and every pull request.

#### Jenkinsfile
The agent for Jenkins is running docker container created from Dockerfile_python. It's default python image with additional temporary user.
On push to master stage and production branch Jenkins will deploy to respective environment
Publish to gemfury is done when pushing do master
On every push and every pull request automated tests are run.

Jenkinsfile is using Jenkins `pipeline`. [About Pipeline syntax](https://jenkins.io/doc/book/pipeline/syntax/).
There is also an example of scripted syntax at the bottom of Jenkinsfile.
Recognition of branch is done with `when` step.
SSH is done with `sshagent` step from ssh agent plugin.
All credentials are stored in vault.

### Contenrization with dockerfiles
There are two dockerfiles `Dockerfile_python` and `Dockerfile`. `Dockerfile_python` is a clean python docker image with added temporary user. It is used in Jenkins Pipeline as a base image. `Dockerfile` is a file to contenerize the application.
To create docker image enter main directory and execute `docker build -t image_name .`.
To run image use `docker run image_name`. To enter bash terminal inside container use `docker run -it image_name bash`

### Logging
Logging is implemented with standard `loggin` module.  In current configuration file logger is set to `WARNING` level logging and console logger is set to `INFO` level logging

### Automated tests
Automated tests are located inside `tests` folder. Every file with `test_*` or `*_test` pattern is considered a test file by PyTest package.
More about python test discovery you can find [here](https://docs.pytest.org/en/latest/goodpractices.html#test-discovery).

### Packaging
Packaging is implemented with setuptools package. Setup.py is packaging script. To add to package files that are not python files you can use `MANIFEST.in` file. To install files from `MANIFEST.in` during package installation `include_package_data` parameter of setup function must be set to `True`
To install package execute `python setup.py install`. To install in develop mode execute `python setup.py develop`. This mode causes that all changes in package source code are instantly reflected during runtime (There is no need to reinstall the package). Another way to install in develop editable mode is to use pip.
Execute `pip install -e .`
To build publishable distribution packages use `python setup.py sdist bdist_wheel`

### App configuration
In current configuration package is looking for configuration in parent directory of `sys.prefix`. For virtualenv it means a parent directory of virtualenv directory. If no `config.json` file is present the default `config.json` inside package will be used.
`config.json` is parsed by `config.py` and is accessible through `python_template.config` module.

### Setting up virtualenv with requirements.txt
It's a good practice to set up virtual environment for every project and install packages into that environment.
You can create virtualenv with `virtualenv name_of_venv` command. To activate virtualenv in terminal use `source namve_of_venv/bin/activate`
To install packages required for the project use `pip install -r requirements.txt`



