declarations = dict()

def template(path):
	pass

class ImproperlyConfigured(Exception):
	pass

class DeclarationBase(type):
	def __getitem__(cls, declaration_id):
		return DeclarationReference(cls, declaration_id)

class Declaration(object):
	__metaclass__ = DeclarationBase
	
	def __init__(self, declaration_id, **kwargs):
		cls = self.__class__
		if(declaration_id in declarations.setdefault(cls, {})):
			raise ImproperlyConfigured("There's already a %r called %r" % (cls, declaration_id))
		declarations[cls][declaration_id] = self

class DeclarationReference(object):
	def __init__(self, klass, declaration_id):
		self.klass = klass
		self.declaration_id = declaration_id
	
	def resolve(self):
		return declarations[self.klass][self.declaration_id]

class Package(Declaration):
	pass

class Service(Declaration):
	pass

class File(Declaration):
	pass

class Exec(Declaration):
	pass

