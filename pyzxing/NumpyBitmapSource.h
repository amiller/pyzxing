/*
 * Copyright (C) 2012 Andrew Miller <amiller@dappervision.com>
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as 
 * published by the Free Software Foundation, either version 3 of the 
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#ifndef __NUMPY_BITMAP_SOURCE_H_
#define __NUMPY_BITMAP_SOURCE_H_

#include <zxing/LuminanceSource.h>
#include <string>

namespace zxing {

class NumpyBitmapSource : public LuminanceSource {
private:
  unsigned char *data;
  int width;
  int height;

public:
  NumpyBitmapSource(unsigned char *data, int width, int height);
  ~NumpyBitmapSource();

  int getWidth() const;
  int getHeight() const;
  unsigned char* getRow(int y, unsigned char* row);
  unsigned char* getMatrix();
  bool isCropSupported() const;
  //Ref<LuminanceSource> crop(int left, int top, int width, int height);
  bool isRotateSupported() const;
  //Ref<LuminanceSource> rotateCounterClockwise();
};

  // Run the ZXing decode function using default parameters
  // Either returns the data or throws an exception
  std::string decode(NumpyBitmapSource *source, bool tryHarder=false);
}

#endif
