from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)
        parsed_toml = toml.loads(content)
        # print(parsed_toml)
        # print('\n\n\n')

        project_name = parsed_toml['tool']['poetry']['name']

        if len(parsed_toml['tool']['poetry']['description']) == 0:
            project_description = '-'
        else:
            project_description = parsed_toml['tool']['poetry']['description']

        project_dependencies = parsed_toml['tool']['poetry']['dependencies'].keys()

        project_dev_dependencies = parsed_toml['tool']['poetry']['dev-dependencies'].keys()
        
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(project_name, project_description, project_dependencies, project_dev_dependencies)
