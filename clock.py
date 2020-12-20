from apscheduler.schedulers.background import BlockingScheduler
from intro import send_message
task = BlockingScheduler()
task.add_job(send_message, 'interval', seconds=10)
task.start()