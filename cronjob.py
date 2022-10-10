from apscheduler.schedulers.blocking import BlockingScheduler
from main import write_data

scheduler = BlockingScheduler()
scheduler.add_job(write_data, "interval", seconds=10000000000)
scheduler.start()
