import sys

guard_ID = 0
guard_asleep_minutes = dict()
max_sleep_minute_count = 0
max_sleep_minute = -1
max_sleeper_ID = 0
sleep_time = -1

def process_events(event):
  global guard_ID
  global guard_asleep_minutes
  global max_sleep_minute_count
  global max_sleep_minute
  global max_sleeper_ID
  global sleep_time

  #extract minutes
  time = int(event[15:17])
  new_guard = event.find("Guard #")
  wakes = event.find("wakes up")
  sleeps = event.find("falls")

  if new_guard != -1:
    ID_end = event.find("begins")-1
    guard_ID = int(event[26:ID_end])
    if guard_ID not in guard_asleep_minutes:
      # 61 is for total sleep minutes
      guard_asleep_minutes[guard_ID] = [0 for i in range(0, 60)]
    # print (guard_ID, " : ", time)

  if sleeps != -1:
    # print(guard_ID, ": sleeps : ", time)
    sleep_time = int(time)
  
  if wakes != -1:
    # print(guard_ID, ": wakes: ", time)
    for i in range(sleep_time, time):
      guard_asleep_minutes[guard_ID][i] += 1
      if max_sleep_minute_count < guard_asleep_minutes[guard_ID][i]:
        max_sleep_minute_count = guard_asleep_minutes[guard_ID][i]
        max_sleep_minute = i
        max_sleeper_ID = guard_ID
  
f = open(sys.argv[1], "r")

events = sorted(f.readlines())

map(process_events, events)

print(max_sleeper_ID * max_sleep_minute)