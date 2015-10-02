import re
from imhotep.tools import Tool


class Eslint(Tool):
    regexp = re.compile('^(?P<filename>.*?): line (?P<line>\d+), col \d+, (?P<message>.*)$')

    def process_line(self, dirname, line):
        match = self.regexp.search(line)
        if match is None:
            return None
        line = match.group('line')
        message = match.group('message')
        # replace '/private' due to mac quirk. workaround this problem:
        # https://github.com/justinabrahms/imhotep/issues/78
        return match.group('filename').replace('/private', ''), line, message

    def get_file_extensions(self):
        return ['.js', 'jsx']

    def get_command(self, dirname, linter_configs=set()):
        return 'eslint --no-ignore --format compact'

