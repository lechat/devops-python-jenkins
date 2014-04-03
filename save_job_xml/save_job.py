"""
An example of how to use JenkinsAPI to fetch the config XML of a job.
"""
from jenkinsapi.jenkins import Jenkins


J = Jenkins('http://localhost:8080')

job_name = 'build_helloworld'

config = J[job_name].get_config()

with open('%s_config.xml' % job_name, "w+") as config_file:
    config_file.write(config)
