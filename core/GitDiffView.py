class GitDiffView:
    def __init__ (self, window):
        self.window = window

    def generate(self):
        view = self.window.new_file()
        view.set_name("Git Diff View")
        view.settings().set("line_numbers", False)
        view.set_scratch(True)
        view.set_syntax_file('Packages/Diff/Diff.sublime-syntax')
        return view