from .Command import Command


class Formated:
    def __init__(self, window):
        self.window = window
        self.command = Command(window)

    def git_status(self, git_statuses):
        # holds dict with every file,
        # type of modification, and if the file is staged
        # will be rendered to git status view
        formated_output = []
        staged = '✔'
        unstaged = '☐'

        for status in git_statuses:
            staged_status = staged if status['is_staged'] else unstaged

            formated_output.append("{} {} {}".format(
                staged_status,
                status['modification_type'],
                status['file_name']
            ))

        help = [
            "-------------------------------",
            "[a] - stage/unstage a file",
            "[d] - dismiss changes to a file"
        ]
        for option in help:
            formated_output.append(option)

        return '\n'.join(formated_output)
