from ssm_document_generator.definition.definition import Definition


class DummyDefinition(Definition):
    def __init__(self, *args, **kwargs):
        super().__init__(name='testName', description='testDescription', *args, **kwargs)
