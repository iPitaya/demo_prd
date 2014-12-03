
def check_permission(func):
	def _(self,*args,**kwargs):
		try:
			name = self.request.params.get('name','')
			if name == '' or name == None:
				raise KeyError
		except KeyError:
			print 'error'

		return func(self,*args,**kwargs)
	return _

		
