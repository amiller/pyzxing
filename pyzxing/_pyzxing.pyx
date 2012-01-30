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

__author__ = 'Andrew Miller <amiller@dappervision.com>'
__license__ = 'AGPL V3'

import numpy as np
cimport numpy as np


cdef extern from "string" namespace "std":
    cdef cppclass string:
        char *c_str()


cdef extern from "NumpyBitmapSource.h" namespace "zxing":
    cdef cppclass NumpyBitmapSource:
        NumpyBitmapSource(unsigned char *data, int width, int height)

    cdef string _decode "decode" (NumpyBitmapSource *source, int tryHarder) except +

def decode(np.ndarray[np.uint8_t, ndim=2, mode='c'] img, tryHarder=False):
    cdef int height = img.shape[0]
    cdef int width = img.shape[1]
    cdef int _tryHarder = 1 if tryHarder else 0
    cdef NumpyBitmapSource *c = new NumpyBitmapSource(<unsigned char *> img.data, 
                                                       width, height)
    return _decode(c, _tryHarder).c_str()
    
