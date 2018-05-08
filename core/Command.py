import subprocess
import re


class Command:
    def __init__(self, window):
        self.window = window
        self.project_root = window.extract_variables()['folder']

    def git_status_dict(self):
        files = []

        # array of staged files
        staged_files = self.git_staged_files().splitlines()
        git_status_output = self.git_status_output()

        # normalize git status output
        files_changed = git_status_output.splitlines()
        files_changed = list(map(lambda file: file.strip(), files_changed))
        for file in files_changed:
            modification_type, file = re.search(
                r"(.{0,2})\s+(.+)",
                file
            ).groups()
            # if file contains spaces the name will
            # be wraped with quotes, so we strip them
            file = file.strip("\"")
            # append space to modification type, looks prettier
            if len(modification_type) < 2:
                modification_type = ' {}'.format(modification_type)

            files.append({
                "file_name": file,
                "modification_type": modification_type,
                "is_staged": file in staged_files
            })

        return files

    def git_status_output(self):
        cmd = ['git status --porcelain']
        return self.run(cmd)

    def git_staged_files(self):
        cmd = ['git diff --name-only --cached']
        return self.run(cmd)

    def git_diff_file(self, file_name):
        file_name = self.escape_spaces(file_name)
        cmd = ['git diff --no-color HEAD {}'.format(file_name)]
        return self.run(cmd)

    def git_stage(self, file_name):
        file_name = self.escape_spaces(file_name)
        cmd = ['git add {}'.format(file_name)]
        return self.run(cmd)

    def git_unstage(self, file_name):
        file_name = self.escape_spaces(file_name)
        cmd = ['git reset HEAD {}'.format(file_name)]
        return self.run(cmd)

    def git_dismis_changes(self, file_name):
        file_name = self.escape_spaces(file_name)
        cmd = ['git checkout {}'.format(file_name)]
        return self.run(cmd)

    def escape_spaces(self, file_name):
        return file_name.replace(' ', '\ ')
    
    def run(self, cmd):
        p = subprocess.Popen(cmd,
                             bufsize=-1,
                             cwd=self.project_root,
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             shell=True)
        output, stderr = p.communicate()
        if (stderr):
            print('Error in Command.py:', stderr)
        return output.decode('utf-8')
