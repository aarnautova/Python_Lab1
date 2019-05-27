from data.storage import Storage
import watering_period

storage = Storage("./data/data.json")

def get_all():
    """ Method for getting all information about watering periods"""

    list_ob = storage.read_all()
    response = [ob.info() for ob in list_ob]
    return response


def get_by_id(id):
    """ Method for getting all information about watering period by id

    >>> get_by_id(9)
    '9) Name: 1 Time: 12 '
    """
    return storage.read(id).info()


def add(name, time, days):
    """ Method for adding information about new watering period
    >>> r = add("1", "12", [])
    >>> r.split(' ', 1)[1]
    'Name: 1 Time: 12 '
    """
    result = storage.create(watering_period.WateringPeriod(name, time, days))
    storage.save_session()
    return result.info()


def update(id, time, days):
    """ Method for updating information of watering period """
    storage.update(id, days=days, time=time)
    storage.save_session()


def delete(id):
    """ Method for deleting information about watering period """
    storage.delete(id)
    storage.save_session()

# python -m doctest -v console_controller.py
if __name__ == "__main__":
    import doctest
    doctest.testmod