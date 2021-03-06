from sparkjobserver.api import SparkJob, build_problems


class WordCountSparkJob(SparkJob):

    def validate(self, context, runtime, config):
        if config.get('input.strings', None):
            return config.get('input.strings')
        else:
            return build_problems(['config input.strings not found'])

    def run_job(self, context, runtime, data):
        return context.parallelize(data).countByValue()


class FailingSparkJob(SparkJob):
    """
    Simple example of a SparkContext job that fails
    with an exception for use in tests
    """

    def validate(self, context, runtime, config):
        if config.get('input.strings', None):
            return config.get('input.strings')
        else:
            return build_problems(['config input.strings not found'])

    def run_job(self, context, runtime, data):
        raise ValueError('Deliberate failure')


class WordCountSparkSessionJob(SparkJob):

    def validate(self, context, runtime, config):
        if config.get('input.strings', None):
            return config.get('input.strings')
        else:
            return build_problems(['config input.strings not found'])

    def run_job(self, context, runtime, data):
        return context.sparkContext.parallelize(data).countByValue()

class WordCountSparkSessionJobPython3(SparkJob):

    def validate(self, context, runtime, config):
        if config.get('input.strings', None):
            return config.get('input.strings')
        else:
            return build_problems(['config input.strings not found'])

    def run_job(self, context, runtime, data):
        return context.sparkContext.parallelize(['strings are now utf-8 \u03BCnico\u0394é!']).countByValue()