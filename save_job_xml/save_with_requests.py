import requests


job_name = 'build_helloworld'
response = requests.get('http://localhost:8080/job/{job}/config.xml'
                        .format(job=job_name))

if not response.status_code == requests.codes.ok:
    print 'Error reading job configuration: %s' % response.status_code
else:
    config = response.text

    with open('%s_config.xml' % job_name, 'w+') as config_file:
        config_file.write(config)
