import sublime, sublime_plugin
import os.path
import webbrowser

class FitnesseTestCommand(sublime_plugin.TextCommand):

	def _get_path_list(self, dir_path):
		basename = os.path.basename(dir_path)
		if basename == "FitNesseRoot":
			return []
		elif len(basename) <= 3:
			raise RuntimeError("not fount fitnesse path")
		else:
			names = self._get_path_list(os.path.dirname(dir_path))
			names.append(basename)
			return names
	
	def run(self, edit):
		# self.view.insert(edit, 0, url)
		path_template = "http://127.0.0.1:8081/%s?test"
		path_list = self._get_path_list(os.path.dirname(self.view.file_name()))
		url = path_template % ".".join(path_list)
		webbrowser.open(url)

	def is_enabled(self):
		return True

	def is_visible(self):
		return True

	def description(self):
		return None
