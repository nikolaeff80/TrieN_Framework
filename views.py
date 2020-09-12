from mainlib.templator import render


class IndexView:
	def __call__(self, request):
		list = [{'name': 'Nikolai'}, {'name': 'Geekbrains'}]
		content = render('index.html', object_list=list)
		return '200 OK', content


class ContactsView:
	def __call__(self, request):
		content = render('contacts.html')
		return '200 OK', content


class NotFound404View:
	def __call__(self, request):
		content = [b'<p style="fontsize: 50px;">404 PAGE Not Found</p>']
		return '404 WHAT', content


class OtherView:
	def __call__(self, request):
		return '200 OK', [b'<h1>other</h1>']


class AboutView:
	def __call__(self, request):
		list = [{'name': 'Nikolai'}, {'name': 'Geekbrains'}]
		content = render('authors.html', object_list=list)
		return '200 OK', content
