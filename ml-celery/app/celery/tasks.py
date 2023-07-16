from celery  import Celery
from app.celery.base_task import MLTaskBase

celery_app = Celery(
    main="",
    broker="",
    backend=""
)
celery_app.config_from_object("config_file.py")


@celery_app.task(
    bind=True,
    base=MLTaskBase,
    name="{query}.{task_name}".format(
        query="",
        task_name="")
)
def ocr():
    res = self.model()
    return res
