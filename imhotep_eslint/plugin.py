from imhotep.tools import Tool
import re


class Eslint(Tool):
    regexp = re.compile('^(?P<filename>.*?): line (?P<line>\d+), col \d+, (?P<message>.*)$')

    def process_line(self, dirname, line):
        match = self.regexp.search(line)
        if match is None:
            return None
        filename = "{0}/{1}".format(dirname, match.group('filename'))
        line = match.group('line')
        message = match.group('message')
        return filename, line, message

    def get_file_extensions(self):
        return ['.js']

    def get_command(self, dirname, linter_configs=set()):
        return 'xargs eslint --format compact'

