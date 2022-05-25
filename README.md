# python_time_extended
This repo contains extended time functions for python3.</br>

# Extended Functions:
* <b>getTime()</b>: Full date and time format (Wed, 01 Jan 2000, 12:00:00)
* <b>getToday()</b>: Only Date in format: (25/01/2000)
* <b>getTimeFromTimestamp(timestamp)</b>: Convert timestamp to Full date and time format (Wed, 01 Jan 2000, 12:00:00)
* <b>getTimeFromTimestamp_short(timestamp)</b>: Convert timestamp to simple time format (12:00)
* <b>getTimeFromTimestamp_pattern(timestamp,pattern)</b>: Convert timestamp to custom strf format
* <b>getNow()</b>: get current timestamp
* <b>getTimeDifFromTimestamps(after, before)</b>: Get time dif of two timestamps in seconds
* <b>minute_is_changed(timestamp1, timestamp2)</b>: Returns true if two timestamps are not in equal minutes
* <b>getElapsedTime(sec)</b>: Converts elapsed seconds to format: (?d, ?h:?m:?s)
* <b>getElapsedTimeFromTimeStamps(after, before)</b>: Calculates Elapsed time between two timestamps and returns in format: format: (?d, ?h:?m:?s)
* <b>get_time_checksum(timestamp)</b>: Returns sha1 hash of the given timestamp
