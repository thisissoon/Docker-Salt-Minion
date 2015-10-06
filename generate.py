from jinja2 import Template
from os import mkdir, link
from os.path import exists

template = Template(open('Dockerfile.template').read())
for version in ["2014.7", "2015.5", "2015.8"]:
	if not exists(version):
		mkdir(version)
	open("%s/Dockerfile" % version, "w").write(template.render(version = version))
	if not exists("%s/run.sh" % version):
		link("run.sh", "%s/run.sh" % version)
