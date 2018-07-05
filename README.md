ec2_task
=================

Enabling easy start, running of tasks and stopping of EC2 instances in AWS.

Requirements
------------

* Python3 (>=3.4)


### Usage

    $ pip install ec2-task

Add your AWS credentials and details of your EC2 instance in config file e.g. aws_config.ini.
The aws_config file should have the following:

    [aws]
    AWS_ACCESS_KEY_ID=
    AWS_SECRET_ACCESS_KEY
    INSTANCE_ID=
    REGION=
    KEY_PATH=<path to aws key file for ssh>
    USER=<user e.g. ubuntu>

List of tasks should be added as a separate file (containing mainly shell commands) e.g. task.sh.

    >>> from ec2_task import connect_ec2
    >>> ec2_instance = connect_ec2.Ec2Instance(config_file="aws_config.ini") # include the path of your aws config file
    >>> ec2_instance.start_instance()
    >>> ec2_instance.run_task(task_file="task.sh") # include the path of your task file
    >>> ec2_instance.stop_instance()
    
Check example in the Github repository.
