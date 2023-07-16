from celery import Task

class MLTaskBase(Task):
    """
    Abstraction of Celery's Task class to support loading ML model.
    """
    abstract = True

    def __init__(self):
        super().__init__()
        self.model = None

    def __call__(self, *args, **kwargs):
        """
        Load model on first call
        Avoids the need to load model on each task request
        """
        if not self.model:
            logging.info("Loading model...")
            self.model = OCREngine()
            logging.info("Model loaded.")
        return self.run(*args, **kwargs)