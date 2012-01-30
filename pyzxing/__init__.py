# 
# Copyright (C) 2012 Andrew Miller <amiller@dappervision.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""QRCode scanning library. Cython-based wrapper for Zebra-Crossing."""

from _pyzxing import decode
import numpy as np

# Works with PIL Images Requires PIL
def decode_image(img, *args, **kwargs):
    """Scans a QRCode contained in the image
    Args:
       img: a PIL Image (e.g. Image.open('example.jpg'))
    Returns:
       decoded data (a string) from the qrcode
    Throws:
       RuntimeError if no code was detected
    """
    img = img.convert('L')
    img = np.frombuffer(img.tostring(), 'u1').reshape(img.size[::-1])
    return decode(img, *args, **kwargs)
