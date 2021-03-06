from views import NotFound404View


class Application:
	
	def get_wsgi_input_data(self, env):
		content_length_data = env.get('CONTENT_LENGTH')
		content_length = int(content_length_data) if content_length_data else 0
		data = env['wsgi.input'].read(content_length) if content_length > 0 else b''
		return data
	
	def parse_wsgi_input_data(self, data: bytes):
		result = {}
		if data:
			data_str = data.decode(encoding='utf-8')
			result = self.parse_input_data(data_str)
		return result
	
	def parse_input_data(self, data: str):
		result = {}
		if data:
			params = data.split('&')
			for item in params:
				k, v = item.split('=')
				result[k] = v
		return result
	
	def __init__(self, urlpatterns: dict, front_controllers: list):
		"""
		:param urlpatterns: словарь связок url: view
		:param front_controllers: список front controllers
		"""
		self.urlpatterns = urlpatterns
		self.front_controllers = front_controllers
	
	def __call__(self, env, start_response):
		path = env['PATH_INFO']
		
		if not path.endswith('/'):
			path = f'{path}/'
			
		method = env['REQUEST_METHOD']
		print(f'method - {method}')
		data = self.get_wsgi_input_data(env)
		print(f'data_1 - {data}')
		data = self.parse_wsgi_input_data(data)
		print(f'data_2 - {data}')
		
		query_string = env['QUERY_STRING']
		request_params = self.parse_input_data(query_string)
		
		if path in self.urlpatterns:
			# получаем view по url
			view = self.urlpatterns[path]
			request = {}
			request['method'] = method
			request['data'] = data
			request['request_params'] = request_params
			# добавляем в запрос данные из front controllers
			for controller in self.front_controllers:
				controller(request)
			# вызываем view, получаем результат
			code, text = view(request)
			# возвращаем заголовки
			start_response(code, [('Content-Type', 'text/html')])
			# возвращаем тело ответа
			return [text.encode('utf-8')]
		else:
			# Если url нет в urlpatterns - то страница не найдена
			start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
			return NotFound404View