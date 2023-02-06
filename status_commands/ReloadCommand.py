from GitDiffView.core.Event import Event
from GitDiffView.status_commands.GitTextCommand import GitTextCommand


class GitDiffViewReloadCommand(GitTextCommand):
    def run(self):
        Event.fire('git_status.update_diff_view', self.current_line)
