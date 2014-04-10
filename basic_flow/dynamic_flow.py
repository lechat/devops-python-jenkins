import logging

from jenkinsapi import jenkins

from jenkinsflow.flow import serial


def main(api):

    my_jobs = ['fast_test_helloworld', 'slow_test_helloworld']
    with serial(api, timeout=200, report_interval=3) as ctrl1:
        ctrl1.invoke('compile_helloworld')

        with ctrl1.parallel(timeout=200, report_interval=3) as ctrl2:
            for job_name in my_jobs:
                ctrl2.invoke(job_name)

        ctrl1.invoke('package_helloworld')

if __name__ == '__main__':
    jenkins = jenkins.Jenkins("http://localhost:8080")
    main(jenkins)
