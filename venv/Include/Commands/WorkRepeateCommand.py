from Include.static_methods import check_work_completed
from Include.Commands.ICommand import ICommand
from Include.Commands.WorkLessCommand import WorkLessCommand
from Include.Commands.StartWorkCommand import StartWorkCommand


class WorkRepeateCommand(ICommand):
    def execute(self):
        is_complete = check_work_completed()
        if is_complete:
            WorkLessCommand().execute()
            StartWorkCommand().execute()
