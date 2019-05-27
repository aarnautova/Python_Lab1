import data.json_reader
import watering_period
from watering_period import WateringPeriod


class Storage:
    """ Class for data storage operations """
    def __init__(self, filename):
        """
        Create an object of Storage class
        >>> s1 = Storage("./data/data.json")
        >>> s2 = Storage("./data/data.json")
        >>> s3 = Storage("./data/data1.json")
        >>> s1.__eq__(s2)
        True
        >>> s1.__eq__(s3)
        False
        """
        self.filename = filename
        self.file_object = data.json_reader.load_dict(filename)
        self.localScheduleList = watering_period.list_from_dict(
            self.file_object.get("items"))
        self.nextId = self.file_object.get("nextId")

    def __eq__(self, other):
        """Compare objects of Storage class

        >>> s1 = Storage("./data/data.json")
        >>> s2 = Storage("./data/data.json")
        >>> s3 = Storage("./data/data1.json")
        >>> s1.__eq__(s2)
        True
        >>> s1.__eq__(s3)
        False
        """
        return self.filename == other.filename

    def create(self, wp: WateringPeriod):
        """ Adds new object to local list

        >>> wp = WateringPeriod("Test", 0, 0, [])
        >>> s = Storage("./data/data1.json")
        >>> s.create(wp).period_id == s.nextId - 1
        True
        >>> s.create(wp).period_id == s.nextId
        False
        """
        wp.period_id = self.nextId
        self.nextId = self.nextId + 1
        self.localScheduleList.append(wp)
        return wp

    def read_all(self):
        """
        Returns local list
        >>> s = Storage("./data/data1.json")
        >>> wp_list = [WateringPeriod("Test", "0", []), WateringPeriod("Test1", "12:20", [])]
        >>> s.read_all() == wp_list
        True

        """
        return self.localScheduleList

    def read(self, period_id):
        """
        Returns local list entity with id "period_id"
        >>> s = Storage("./data/data1.json")
        >>> wp1 = WateringPeriod("Test1", "12:20", [])
        >>> wp2 = WateringPeriod("Test", "12:20", [])
        >>> s.read(2).__eq__(wp1)
        True
        >>> s.read(2).__eq__(wp2)
        False
        """
        try:
            return next(
                filter(
                    lambda x: x.period_id == period_id,
                    self.localScheduleList))
        except StopIteration:
            raise Exception("there aren't such element")

    @staticmethod
    def update_ob(to_upd, kwargs):
        if kwargs.get('name'):
            to_upd.name = kwargs.get('name')
        if kwargs.get('time'):
            to_upd.time = kwargs.get('time')
        if kwargs.get('days'):
            to_upd.days = kwargs.get('days')
            return to_upd.period_id

    def update(self, period_id, **kwargs):
        """
        Updates local list entity with id "period_id"

        >>> s = Storage("./data/data1.json")
        >>> upd = s.update(1, time="12:20", days=[])
        >>> wp = WateringPeriod("Test", "12:20", [])
        >>> wp.__eq__(upd)
        True

        """
        try:
            to_upd = next(
                filter(
                    lambda x: x.period_id == period_id,
                    self.localScheduleList))
            self.update_ob(to_upd, kwargs)
            return to_upd
        except StopIteration:
            raise Exception("there aren't such element")

    def delete(self, period_id):
        """
        Deletes from local list entity with id "period_id"
         >>> s1 = Storage("./data/data1.json")
         >>> s2 = Storage("./data/data1.json")
         >>> s1.delete(1)
         >>> len(s1.read_all()) == len(s2.read_all())
         False
         >>> len(s1.read_all()) == 1
         True
         >>> len(s2.read_all()) == 2
         True

        """
        try:
            self.localScheduleList.remove(next(
                filter(
                    lambda x: x.period_id == period_id,
                    self.localScheduleList)))
        except StopIteration:
            raise Exception("there aren't such element")

    def delete_all(self):
        """
        Clears local list

         >>> s1 = Storage("./data/data1.json")
         >>> s2 = Storage("./data/data1.json")
         >>> s1.delete_all()
         >>> len(s1.read_all()) == len(s2.read_all())
         False
         >>> len(s1.read_all()) == 0
         True
         >>> len(s2.read_all()) == 2
         True
        """
        self.localScheduleList.clear()
        self.nextId = 0

    def save_session(self):
        """
        Saves local list to file
        """
        data.json_reader.write_file(
            self.filename,
            {"nextId": self.nextId,
             "items": [ob.__dict__() for ob in self.localScheduleList]})


# python -m doctest -v ./data/storage.py
if __name__ == "__main__":
    import doctest
    doctest.testmod()
