import json


class LongContents:
    def __init__(self, contents_id, contents_type, long_text, image):
        self.contents_id = contents_id
        self.contents_type = contents_type
        self.long_text = long_text
        self.image = image

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)

    def __repr__(self):
        return f'{self.__dict__}'

    def __eq__(self, other):
        if isinstance(other, LongContents) and \
                self.contents_id == other.contents_id and \
                self.contents_type == other.contents_type and \
                self.long_text == other.long_text and \
                self.image == other.image:
            return True
        return False
