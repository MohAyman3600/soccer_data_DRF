"""Base error handler mixin for celery tasks."""
from api.models import AsyncActionReport, TaskResult


class BaseErrorHandlerMixin:
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        '''
        exc – The exception raised by the task.
        task_id – Unique id of the failed task.
        args – Original arguments for the task that failed.
        kwargs – Original keyword arguments for the task that failed.
        '''
        AsyncActionReport.objects.create(status=AsyncActionReport.FAILED,
                                         error_message=str(exc),
                                         error_traceback=einfo)

    def on_success(self, retval, task_id, args, kwargs):
        '''
        retval – The return value of the task.
        task_id – Unique id of the executed task.
        args – Original arguments for the executed task.
        kwargs – Original keyword arguments for the executed task.
        '''
        report = AsyncActionReport.objects.create(status=AsyncActionReport.OK)
        for item, status in retval.items():
            TaskResult.objects.create(
                object_type=item,
                object_id=item.id,
                status=status,
                report=report
            )
