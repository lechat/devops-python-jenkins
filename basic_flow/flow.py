import logging

from jenkinsapi import jenkins

from jenkinsflow.flow import serial


def main(api):
    logging.basicConfig()
    logging.getLogger("").setLevel(logging.WARNING)

    with serial(api, timeout=70, report_interval=3) as ctrl1:
        ctrl1.invoke('compile_helloworld')

        with ctrl1.parallel(timeout=70, report_interval=3) as ctrl2:
            ctrl2.invoke('fast_test_helloworld')
            ctrl2.invoke('slow_test_helloworld')

        ctrl1.invoke('package_helloworld')

if __name__ == '__main__':
    jenkins = jenkins.Jenkins("http://localhost:8080")
    main(jenkins)
