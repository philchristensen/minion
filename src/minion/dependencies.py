import logging

from pygraph.classes.digraph import digraph

from minion import manifest

logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger(__name__)
g = None

def init_graph():
	global g
	if(g):
		return g
	
	g = digraph()
	deps = []
	for cls, lst in manifest.declarations.iteritems():
		for declaration_id, dec in lst.iteritems():
			log.debug('adding node %r' % declaration_id)
			g.add_node(declaration_id)
			reqs = getattr(dec, 'require', [])
			if not(isinstance(reqs, (list, tuple))):
				reqs = [reqs]
			d = []
			for req in reqs:
				d.append([req.declaration_id, declaration_id])
			if(d):
				deps.append(d)
	
	for dep in deps:
		log.debug('adding edge %r' % dep)
		g.add_edge(*dep)
	
	return g
