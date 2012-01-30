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

#include "NumpyBitmapSource.h"
#include <zxing/Binarizer.h>
#include <zxing/common/HybridBinarizer.h>
#include <zxing/MultiFormatReader.h>
#include <zxing/BinaryBitmap.h>
#include <zxing/DecodeHints.h>

#include <cstdlib>

namespace zxing {

  NumpyBitmapSource::NumpyBitmapSource(unsigned char *data, 
				       int width, int height) : 
    data(data), width(width), height(height) {
  }

  NumpyBitmapSource::~NumpyBitmapSource() {
  }

  int NumpyBitmapSource::getWidth() const {
    return width;
  }

  int NumpyBitmapSource::getHeight() const {
    return height;
  }

  unsigned char* NumpyBitmapSource::getRow(int y, unsigned char* row) {
    if (row == NULL) row = new unsigned char[width];
    memcpy(row, data + y*width, width);
    return row;
  }

  /** This is a more efficient implementation. */
  unsigned char* NumpyBitmapSource::getMatrix() {
    unsigned char* matrix = new unsigned char[width*height];
    memcpy(matrix, data, width*height);
    return matrix;
  }

  bool NumpyBitmapSource::isRotateSupported() const {
    return false;
  }

  bool NumpyBitmapSource::isCropSupported() const{
    return false;
  }

  std::string decode(NumpyBitmapSource *_source, bool tryHarder) {
    Ref<NumpyBitmapSource> source(_source);
    Ref<Binarizer> binarizer(new HybridBinarizer(source));
    Ref<BinaryBitmap> binary(new BinaryBitmap(binarizer));
    DecodeHints hints(DecodeHints::DEFAULT_HINT);
    hints.setTryHarder(tryHarder);
    Ref<Reader> reader(new MultiFormatReader);
    Ref<Result> result(reader->decode(binary, hints));
    return result->getText()->getText();
  }
}
