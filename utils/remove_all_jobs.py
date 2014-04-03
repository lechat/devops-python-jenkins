from jenkinsapi.jenkins import Jenkins


J = Jenkins('http://localhost:8080')

for job_name in J.jobs.keys():
    print 'Removing ', job_name
    del J.jobs[job_name]
