import sched, time,random, os



new_data = 0
scheduler = sched.scheduler(time.time, time.sleep)


def schedule_covid_updates(update_interval, update_name):
    print("updating")
    new_data = update_name+str(random.random())+"\n"
    with open("output_from_data_server.txt", "w") as g:
        g.writelines(new_data)
    now = time.time()
    #scheduler.enterabs(now + update_interval, 1, update_stuff, (update_interval, update_name,))

def update_stuff(update_interval, update_name):
    now = time.time()
    scheduler.enterabs(now + update_interval, 1, update_stuff, (update_interval, update_name,))
    scheduler.run()

def daily_updates(update_name):
    schedule_covid_updates(60*60*24, update_name)


if __name__ == "__main__":
    schedule_covid_updates(10, "name")