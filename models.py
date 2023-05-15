class GenericResponse:
    def __init__(self, **kwargst) -> dict:
        self.success = kwargst.get('success')
        self.data = kwargst.get('data')
        self.message = kwargst.get('message')