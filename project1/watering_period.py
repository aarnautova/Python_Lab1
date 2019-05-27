import json


class WateringPeriod:
    """ Class of watering period information """
    def __init__(self, name, time, days, period_id=0):
        """Create object of WateringPeriod class

        >>> wp1 = WateringPeriod("TEST", "12:00", ["Monday", "Tuesday"])
        >>> wp2 = WateringPeriod("TEST", "12:00", ["Monday", "Tuesday"])
        >>> wp3 = WateringPeriod("TEST1", "17:00", [])
        >>> wp1.__eq__(wp2)
        True
        >>> wp1.__eq__(wp3)
        False
        """
        self.period_id = period_id
        self.name = name
        self.time = time
        self.days = days

    def info(self):
        """Prints information about watering period object.

        >>> wp = WateringPeriod("TEST", "12:00", [])
        >>> wp.info()
        '0) Name: TEST Time: 12:00 '
        >>> wp1 = WateringPeriod("TEST", "12:00", ["Friday", "Monday"])
        >>> wp1.info()
        '0) Name: TEST Time: 12:00 (Friday) (Monday) '
        """
        result = "{}) Name: {} Time: {} ".format(self.period_id, self.name, self.time)
        for day in self.days:
            result += "(" + day + ") "
        return result

    def __dict__(self):
        """Convert WateringPeriod object to dict

        >>> wp = WateringPeriod("TEST", "12:00", [])
        >>> wp.__dict__()
        {'name': 'TEST', 'time': '12:00', 'period_id': 0, 'days': []}
        >>> wp = WateringPeriod("TEST", "12:00", ["Thursday", "Friday"])
        >>> wp.__dict__()
        {'name': 'TEST', 'time': '12:00', 'period_id': 0, 'days': ['Thursday', 'Friday']}
        """
        return {"name": self.name,
                "time": self.time,
                "period_id": self.period_id,
                "days": self.days}

    def __eq__(self, other):
        """Compare objects of WateringPeriod class

        >>> wp1 = WateringPeriod("TEST", "12:00", [])
        >>> wp2 = WateringPeriod("TEST", "12:00", [])
        >>> wp3 = WateringPeriod("TEST1", "12:00", [])
        >>> wp1.__eq__(wp2)
        True
        >>> wp1.__eq__(wp3)
        False
        """
        return self.name == other.name and self.days == other.days and self.time == other.time


class WateringPeriodEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, WateringPeriod):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


def ob_from_dict(d):
    """Convert dict to WateringPeriod object

    >>> d1 = {"name": "TEST", "time": 0, "period_id": 0, "days": []}
    >>> wp1 = WateringPeriod("TEST", "12:00", [])
    >>> wp1.__eq__(ob_from_dict(d1))
    False
    >>> d2 = {"name": "TEST", "time": "12:00", "period_id": 0, "days": ["Friday", "Thursday"]}
    >>> wp2 = WateringPeriod("TEST", "12:00", ["Friday", "Thursday"])
    >>> wp2.__eq__(ob_from_dict(d2))
    True
    """
    return WateringPeriod(d.get('name'),
                          d.get('time'),
                          d.get('days'),
                          d.get('period_id'))


def list_from_dict(dictionary):
    """Convert dict to list of WateringPeriod objects
    >>> d1 = [ {'name': "TEST", 'time': "23:00", 'period_id': 0, 'days': []}]
    >>> list_from_dict(d1) == [WateringPeriod("TEST", "23:00", [])]
    True
    """
    ob_list = list()
    for item in dictionary:
        ob_list.append(ob_from_dict(item))

    return ob_list


# python -m doctest -v watering_period.py
if __name__ == "__main__":
    import doctest
    doctest.testmod()
