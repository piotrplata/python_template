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

####Jenkins
To run CI/CD you need machine with Jenkins.

To enable Jenkins automated runs webhooks must be set up. To set up webhooks on github go to project `Settings` on and select `Webhooks`.
Set up `Payload Url` to point to `github-webhook` endpoint on your machine with Jenkins.
   
    http://your.machine.with.jenkins:yourport/github-webhook/
    
To enable automated runs on pull requests 
under `Which events would you like to trigger this webhook` select 
`Let me select individual events` and pick `Pushes` and `Pull requests`

Now jenkins runs automated tests on every push and every pull request.

####Jenkinsfile
On push to master stage and production branch Jenkins will deploy to respective environment
Publish to gemfury is done when pushing do master
On every push and every pull request automated tests are run.

Jenkinsfile is using Jenkins `pipeline`. [About Pipeline syntax](https://jenkins.io/doc/book/pipeline/syntax/).
There is also an example of scripted suntax at the bottom of Jenkinsfile.
Recognition of branch is done with `when` step.
SSH is done with `sshagent` step from ssh agent plugin.
All credentials are stored in vault.


