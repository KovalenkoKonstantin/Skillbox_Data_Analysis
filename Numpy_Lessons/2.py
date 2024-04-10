import numpy as np

a = np.array([1, 2, 3, 4])
a
# array([1, 2, 3, 4])
a = np.array([1, 2, 3, 4], 'float64')
a
# array([1., 2., 3., 4.])
np.sctypeDict
# {'?': numpy.bool_,
#  0: numpy.bool_,
#  'byte': numpy.int8,
#  'b': numpy.int8,
#  1: numpy.int8,
#  'ubyte': numpy.uint8,
#  'B': numpy.uint8,
#  2: numpy.uint8,
#  'short': numpy.int16,
#  'h': numpy.int16,
#  3: numpy.int16,
#  'ushort': numpy.uint16,
#  'H': numpy.uint16,
#  4: numpy.uint16,
#  'i': numpy.intc,
#  5: numpy.intc,
#  'uint': numpy.uint32,
#  'I': numpy.uintc,
#  6: numpy.uintc,
#  'intp': numpy.int64,
#  'p': numpy.int64,
#  9: numpy.int64,
#  'uintp': numpy.uint64,
#  'P': numpy.uint64,
#  10: numpy.uint64,
#  'long': numpy.int32,
#  'l': numpy.int32,
#  7: numpy.int32,
#  'ulong': numpy.uint32,
#  'L': numpy.uint32,
#  8: numpy.uint32,
#  'longlong': numpy.int64,
#  'q': numpy.int64,
#  'ulonglong': numpy.uint64,
#  'Q': numpy.uint64,
#  'half': numpy.float16,
#  'e': numpy.float16,
#  23: numpy.float16,
#  'f': numpy.float32,
#  11: numpy.float32,
#  'double': numpy.float64,
#  'd': numpy.float64,
#  12: numpy.float64,
#  'longdouble': numpy.longdouble,
#  'g': numpy.longdouble,
#  13: numpy.longdouble,
#  'cfloat': numpy.complex128,
#  'F': numpy.complex64,
#  14: numpy.complex64,
#  'cdouble': numpy.complex128,
#  'D': numpy.complex128,
#  15: numpy.complex128,
#  'clongdouble': numpy.clongdouble,
#  'G': numpy.clongdouble,
#  16: numpy.clongdouble,
#  'O': numpy.object_,
#  17: numpy.object_,
#  'S': numpy.bytes_,
#  18: numpy.bytes_,
#  'unicode': numpy.str_,
#  'U': numpy.str_,
#  19: numpy.str_,
#  'void': numpy.void,
#  'V': numpy.void,
#  20: numpy.void,
#  'M': numpy.datetime64,
#  21: numpy.datetime64,
#  'm': numpy.timedelta64,
#  22: numpy.timedelta64,
#  'b1': numpy.bool_,
#  'bool8': numpy.bool_,
#  'i8': numpy.int64,
#  'int64': numpy.int64,
#  'u8': numpy.uint64,
#  'uint64': numpy.uint64,
#  'f2': numpy.float16,
#  'float16': numpy.float16,
#  'f4': numpy.float32,
#  'float32': numpy.float32,
#  'f8': numpy.float64,
#  'float64': numpy.float64,
#  'c8': numpy.complex64,
#  'complex64': numpy.complex64,
#  'c16': numpy.complex128,
#  'complex128': numpy.complex128,
#  'object0': numpy.object_,
#  'bytes0': numpy.bytes_,
#  'str0': numpy.str_,
#  'void0': numpy.void,
#  'M8': numpy.datetime64,
#  'datetime64': numpy.datetime64,
#  'm8': numpy.timedelta64,
#  'timedelta64': numpy.timedelta64,
#  'int32': numpy.int32,
#  'i4': numpy.int32,
#  'uint32': numpy.uint32,
#  'u4': numpy.uint32,
#  'int16': numpy.int16,
#  'i2': numpy.int16,
#  'uint16': numpy.uint16,
#  'u2': numpy.uint16,
#  'int8': numpy.int8,
#  'i1': numpy.int8,
#  'uint8': numpy.uint8,
#  'u1': numpy.uint8,
#  'complex_': numpy.complex128,
#  'single': numpy.float32,
#  'csingle': numpy.complex64,
#  'singlecomplex': numpy.complex64,
#  'float_': numpy.float64,
#  'intc': numpy.intc,
#  'uintc': numpy.uintc,
#  'int_': numpy.int32,
#  'longfloat': numpy.longdouble,
#  'clongfloat': numpy.clongdouble,
#  'longcomplex': numpy.clongdouble,
#  'bool_': numpy.bool_,
#  'bytes_': numpy.bytes_,
#  'string_': numpy.bytes_,
#  'str_': numpy.str_,
#  'unicode_': numpy.str_,
#  'object_': numpy.object_,
#  'int': numpy.int32,
#  'float': numpy.float64,
#  'complex': numpy.complex128,
#  'bool': numpy.bool_,
#  'object': numpy.object_,
#  'str': numpy.str_,
#  'bytes': numpy.bytes_,
#  'a': numpy.bytes_,
#  'int0': numpy.int64,
#  'uint0': numpy.uint64}
a = np.array([1, 2, 3, 4], 'uintc')
a
# array([1, 2, 3, 4], dtype=uint32)
a = np.array([1, 2, 3, 4], 'str_')
a
# array(['1', '2', '3', '4'], dtype='<U1')
np.complex64(10)
# (10+0j)
np.int16(10.5)
# 10
a = np.array([1, 2, 5000, 1000], dtype='int8')
a
# array([   1,    2, -120,  -24], dtype=int8)
a = np.array([1, 2, 5000, 1000])
a
# array([   1,    2, 5000, 1000])
np.complex64(a)
# array([1.e+00+0.j, 2.e+00+0.j, 5.e+03+0.j, 1.e+03+0.j], dtype=complex64) # возвращается копия массива
a
# array([   1,    2, 5000, 1000])
b = np.complex64(a)
c = np.int32(b)
c
# array([   1,    2, 5000, 1000])

np.array((1, 2, 3))
# array([1, 2, 3])
np.array('Hello')
# array('Hello', dtype='<U5') # юникод содержащий пять символов

a = np.array([[1, 2], [3, 4], [5, 6]])
a
# array([[1, 2],
#        [3, 4],
#        [5, 6]])
a = np.array([[1, 2], [3, 4], [5, 6, 7]])
# The detected shape was (3,) + inhomogeneous part.
b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
b
# array([[[ 1,  2],
#         [ 3,  4]],
#        [[ 5,  6],
#         [ 7,  8]],
#        [[ 9, 10],
#         [11, 12]]])
b[0]
# array([[1, 2],
#        [3, 4]])
b[1]
# array([[5, 6],
#        [7, 8]])
b[2]
# array([[ 9, 10],
#        [11, 12]])
b[0, 0]
# array([1, 2])
b[0, 0, 0]
# 1
