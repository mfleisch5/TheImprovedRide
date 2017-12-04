from geopy.distance import great_circle
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
geo_path = os.path.join(dir_path, 'geocodes.json')
fail_path = os.path.join(dir_path, 'failures.json')


def distance(x1, y1, x2, y2):
    """
    Returns the "great circle" distance between two points
    :param x1: X-coordinate of point 1
    :param y1: Y-coordinate of point 1
    :param x2: X-coordinate of point 2
    :param y2: Y-coordinate of point 2
    :return: The distance in miles
    """
    # Great-Circle distance
    return great_circle((x1, y1), (x2, y2)).miles


# converts the given time in seconds to a string military time hour, minutes
def seconds_to_time(seconds):
    """
    Converts seconds to a string "time" value
    :param seconds: the int time in seconds (0-86400)
    :return: Str -- the time value
    """
    minutes = seconds // 60
    hours = minutes // 60
    minutesRounded = minutes % 60
    time = 'AM'

    if hours >= 12:
        time = 'PM'
        hours = hours % 12
    if hours == 0:
        hours = 12
    if minutesRounded < 10:
        minutesRounded = '0' + str(minutesRounded)

    return '{0}:{1} {2}'.format(hours, minutesRounded, time)


def time_to_seconds(time):
    array = time.split()
    time = array[0]
    pm = array[1] == 'PM'
    time = time.split(":")

    hour = int(time[0])
    minutes = int(time[1])

    if pm and hour != 12:
        hour = int(hour) + 12
    if hour == 12 and not pm:
        hour = 0

    return hour * 60 * 60 + minutes * 60
