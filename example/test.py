from ec2_task import connect_ec2

ec2_instance = connect_ec2.Ec2Instance(config_file="aws_config.ini")
ec2_instance.start_instance()
ec2_instance.run_task(task_file="task.sh")
ec2_instance.stop_instance()