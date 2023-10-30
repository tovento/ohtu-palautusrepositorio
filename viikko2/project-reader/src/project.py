class Project:
    def __init__(self, name, description, license_, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license_
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_collections(self, collection):
        return "\n- " + f"\n- ".join(collection) if len(collection) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}"
            f"\n\nAuthors: {self._stringify_collections(self.authors)}"
            f"\n\nDependencies: {self._stringify_collections(self.dependencies)}"
            f"\n\nDevelopment dependencies: {self._stringify_collections(self.dev_dependencies)}"
        )
