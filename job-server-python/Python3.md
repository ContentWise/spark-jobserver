# Spark Job Server - Submit Python 3 job

## How to create python 3 egg file for spark job server

Clone Spark Job Server repository from [here](https://github.com/ContentWise/spark-jobserver) then edit the file *job-server-python/src/python/build.sh* changing the python command to the one version you require (for instance python3 to create python 3.x egg file version)

From repository folder execute:

* sbt
* buildPython

and you can find the egg file under folder *job-server-python/target/python* with the following name *spark_jobserver_python-<SJS_VERSION>-py<PYTHON_VERSION>.egg*.

Once the file has been create you need to change Spark Job Server *application.conf* file editing the python section

```
python {
      paths = [
        "/opt/devel/spark/python",
        "/opt/devel/temp/spark_jobserver_python-<SJS_VERSION>-py<PYTHON_VERSION>.egg"
      ]

      # The default value in application.conf is "python"
      executable = "/usr/local/bin/python<PYTHON_VERSION>"
   }
```

Spark Job Server can now manage python3 jobs.

## Spark configuration

Spark installation must be configured to support python3 jobs.

## How to submit sjs-python-example file

1. Create a python context factory using curl command

   ```
   curl -X POST "localhost:8090/contexts/py-context?context-factory=park.jobserver.python.PythonSessionContextFactory"
   ```

2. Whereas Java and Scala jobs are packaged as Jar files, Python jobs need to be packaged as `Egg` files we could push this to the server as a job binary

   ```
   curl --data-binary @/opt/devel/temp/sjs_python_examples-<SJS-VERSION>-py<PYTHON_VERSION>.egg -H 'Content-Type: application/python-archive' localhost:8090/binaries/my_py_job
   ```

3. Finally running a Python job is similar to running other job types

   ```
   1. curl -d 'input.strings = ["a", "b", "a", "b" ]' \
      "localhost:8090/jobs?appName=my_py_job&classPath=example_jobs.word_count.WordCountSparkJob&context=py-context"
   ```

   ​