from datetime import datetime
import hashlib
import time

# Time Based
time_dict = {"time": "", "timestamp": 0}

# Full date and time format (Wed, 01 Jan 2000, 12:00:00)
def getTime():
    return str(time.strftime('%a, %d %b %Y, %H:%M:%S'))

# Only Date in this format (25/01/2000)
def getToday():
    now = datetime.now()
    return str(time.strftime("%d/%m/%Y"))

# Convert timestamp to Full date and time format (Wed, 01 Jan 2000, 12:00:00)
def getTimeFromTimestamp(timestamp):
    time = datetime.fromtimestamp(timestamp)
    return str(time.strftime('%a, %d %b %Y, %H:%M:%S'))

# Convert timestamp to simple time format
def getTimeFromTimestamp_short(timestamp):
    time = datetime.fromtimestamp(timestamp)
    return str(time.strftime('%H:%M'))

# Convert timestamp to custom strf format
def getTimeFromTimestamp_pattern(timestamp,pattern):
    try:
        time = datetime.fromtimestamp(timestamp)
        return str(time.strftime(pattern))
    except:
        return None
    
#get current timestamp
def getNow():
    return datetime.now().timestamp()

#get time dif oftwo timestamps in seconds
def getTimeDifFromTimestamps(after, before):
    return int(after - before)


def get_minute_from_timestamp(timestamp):
    return int(timestamp / 60)

# Returns true if two timestamps are not in equal minutes
def minute_is_changed(timestamp1, timestamp2):
    if get_minute_from_timestamp(timestamp1) != get_minute_from_timestamp(timestamp2):
        return True
    return False

# Converts elapsed seconds to format: ?d, ?h:?m:?s
def getElapsedTime(sec):
    s = int(sec) % 60
    m = int(sec / 60) % 60
    h = int(sec / 3600) % 24
    d = int(sec / (3600 * 24))
    dif = ""
    if (d > 0):
        dif += str(d) + "d, "
    dif += str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
    return dif

# Calculates Elapsed time between two timestamps and returns in format: format: ?d, ?h:?m:?s
def getElapsedTimeFromTimeStamps(after, before):
    sec = getTimeDifFromTimestamps(after, before)
    s = sec % 60
    m = int(sec / 60) % 60
    h = int(sec / 3600) % 24
    d = int(sec / (3600 * 24))
    dif = ""
    if (d > 0):
        dif += str(d) + "d, "
    dif += str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
    return dif

# Returns sha1 hash of the given timestamp
def get_time_checksum(timestamp):
    hsh=hashlib.sha1(str(timestamp).encode('utf-8'))
    return hsh.hexdigest()