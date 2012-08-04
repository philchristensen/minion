from pygraph.classes.graph import graph

from minion import manifest

deps = None

def init_graph():
	global deps
	if(deps):
		return deps
	deps = digraph()
	for cls, lst in manifest.declarations.iteritems():
		for declaration_id, dec in lst.iteritems():
			deps.add_node(declaration_id, [('value', dec)])
			reqs = getattr(dec, 'require', [])
			if not(isinstance(reqs, (list, tuple))):
				reqs = [reqs]
			for req in reqs:
				deps.add_edge([declaration_id, req.declaration_id])
	return deps
