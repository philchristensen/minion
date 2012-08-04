declarations = dict()

class DeclarationBase(type):
	def __getitem__(cls, declaration_id):
		return DeclarationReference(declaration_id)

class Declaration(object):
	__metaclass__ = DeclarationBase
	def __init__(self, declaration_id, **kwargs):
		pass

class DeclarationReference(object):
	def __init__(self, declaration_id):
		self.declaration_id = declaration_id

class ConfigValue(object):
	pass

class apt(ConfigValue):
	pass

class macports(ConfigValue):
	pass

class pip(ConfigValue):
	pass

class present(ConfigValue):
	pass

class running(ConfigValue):
	pass

class keep(ConfigValue):
	pass

class Package(Declaration):
	pass

class Service(Declaration):
	pass

class File(Declaration):
	pass

class Exec(Declaration):
	pass

