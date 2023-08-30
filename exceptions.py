class InvalidInput(Exception):
    def __init__(self, error_msge) -> None:
        self.error_msge = error_msge
        super().__init__(f"Invalid input: There's no option available for {error_msge}")  
    pass