import configparser
import boto3
from botocore.exceptions import ClientError
import time
import paramiko


class Ec2Instance:

    def __init__(self, config_file):
        self.config = configparser.ConfigParser(allow_no_value=True)
        self.config.read(config_file)

        ec2 = boto3.resource(
            'ec2',
            # Hard coded strings as credentials, not recommended.
            aws_access_key_id=self.config["aws"]["AWS_ACCESS_KEY_ID"],
            aws_secret_access_key=self.config["aws"]["AWS_SECRET_ACCESS_KEY"]
        )
        instance_id = self.config["aws"]["INSTANCE_ID"]
        self.instance = ec2.Instance(id=instance_id)  # instance id

    def start_instance(self):
        if self.instance.state["Name"] != "running":
            # DRY RUN to verify the permissions.
            try:
                self.instance.start(DryRun=True)
            except ClientError as e:
                if 'DryRunOperation' not in str(e):
                    raise

            # On DRY RUN success, initiate the instance
            print("Starting the instance.")
            self.instance.start(DryRun=False)
            self.instance.wait_until_running()
            self.instance.load()
            print("Waiting for status checks ..")
            time.sleep(45)

    def run_task(self, task_file):
        aws_key = paramiko.RSAKey.from_private_key_file(self.config["aws"]["KEY_PATH"])  # your private key for ssh
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print("Connecting to shell using ssh")
        ssh_client.connect(
            hostname=self.instance.public_dns_name,
            username=self.config["aws"]["USER"],
            pkey=aws_key
        )
        print("Executing commands on EC2 instance")
        task_file = open(task_file, "r")
        tasks = task_file.read()
        stdin, stdout, stderr = ssh_client.exec_command(tasks)
        for line in iter(lambda: stdout.readline(2048), ""):
            print(line)
        print("All tasks have been executed.")

    def stop_instance(self):
        print("Stopping the instance.")
        self.instance.stop()
