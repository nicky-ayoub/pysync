from resource import Resource
from cStringIO import StringIO
import mimetypes
import os

class File(Resource):
    """A snapshot of a versioned file."""
    #def __init__(self):
    #    super(File, self).__init__()
    
    def get_data(self):
        """Return a binary blob of the file contents"""
        stream = StringIO()

        # The get_file method needs a file-like object to write into.
        self.ra_api.get_file(os.path.join(self.branch_path, self.path),
                             stream,
                             self.rev)

        return stream.getvalue()

    def _is_file(self):
        """ Overrides the method from parent (Resource) """
        return True

    def _mimetype(self):
        """ Identifies the mimetype of this File """
        type = mimetypes.guess_type(self.extension())[0]

        # NOTE: application/octet-stream is the generic "I don't know" mimetype.
        type = type or 'application/octet-stream'

        return type

    def _is_text(self):
        """ Determines whether this object is a textfile or not """
        return 'text' == self.mimetype().split('/')[0]

    def _is_image(self):
        """ Determines whether this object is an imagefile or not """
        return 'image' == self.mimetype().split('/')[0]

    def extension(self):
        return os.path.splitext(self.path)[-1]

    def type(self):
        return self.extension()[1:]



    data = property(get_data)


