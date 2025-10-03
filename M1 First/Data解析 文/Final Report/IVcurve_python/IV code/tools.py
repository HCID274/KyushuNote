#!/usr/bin/env python
# Data解析 文\Final Report\IVcurve_python\IV code\tools.py
"""
    Utility tools

    function:
       strarr
       firstloc
       getlog
       loadtxt
       savetxt
    class:
       egio
    extension:
       setDefaultArguments
       setFileArguments

    Status
    ------
    Version 1.0.3

    Authour
    -------
    Shigeru Inagaki                                       
    Research Institute for Applied Mechanics 
    inagaki@riam.kyushu-u.ac.jp  
    
    Revision History
    ----------------
    [04-November-2016] Creation                   Ver 1.0
    [12-April-2017] Add strarr                    Ver 1.0.1 
    [14-April-2017] readtxt, writetxt renamed     Ver 1.0.2 
    [01-May-2017]   python 3 supported            Ver 1.0.3

    Copyright
    ---------
    2017 Shigeru Inagaki (inagaki@riam.kyushu-u.ac.jp)
    Released under the MIT, BSD, and GPL Licenses.

"""
import sys
import os
import re
import itertools
import warnings
import argparse
from time import gmtime, strftime
import numpy as np
from numpy.compat import asbytes
        
def strarr(shape, len=16):
    dtype = "|S{0:d}".format(len)
    return np.empty(shape, dtype)

def firstloc(mask, back=False):
    indx = np.where(mask)
    n = mask.ndim
    if back :
        i = -1
    else :
        i = 0
    if n == 1 :
        return indx[:][i]
    else :
        ans = []
        for j in range(n):
            ans.append(indx[j][i])
        return tuple(ans)
    
def getLog():
    argvs = sys.argv 
    log = "{0} Created by".format(strftime("%m-%d-%Y %H:%M", gmtime()))
    for val in argvs:
        log = log + " " + val
    return log

def readbin(binfile, buffsize, offset=0):
    import os
    try:
        if binfile.endswith('.gz'):
            import gzip
            import cStringIO 
            gid = gzip.open(binfile,'rb')
            gid.seek(offset*2, os.SEEK_SET)            
            str = cStringIO.StringIO()
            str = gid.read()
            raw = np.fromstring(str, np.int16, buffsize)
            gid.close()
        else:
            fid = open(binfile, 'rb')
            fid.seek(offset*2, os.SEEK_SET)
            raw = np.fromfile(fid, np.int16, buffsize)
            fid.close()
        return raw
    except Exception as ex:
         print("Error at readBin")
         print(ex.message)
         sys.exit(-1)   

def loadtxt(fname, dtype=float, comments='#', delimiter=',',
            converters=None, skiprows=0, usecols=None, unpack=False,
            ndmin=0, eoh=None):
    """
    Wrapper function of numpy.loadtxt
    Load data and list of lines commented out in header part of the text file.
    sys.stdin without eoh (end of header) is not allowed
    Each row in the text file must have the same number of values.
    Parameters
    ----------
    fname : file or str
        File, filename, or generator to read.  If the filename extension is
        ``.gz`` or ``.bz2``, the file is first decompressed. Note that
        generators should return byte strings for Python 3k.
    dtype : data-type, optional
        Data-type of the resulting array; default: float.  If this is a
        structured data-type, the resulting array will be 1-dimensional, and
        each row will be interpreted as an element of the array.  In this
        case, the number of columns used must match the number of fields in
        the data-type.
    comments : str or sequence, optional
        The characters or list of characters used to indicate the start of a
        comment;
        default: '#'.
    delimiter : str, optional
        The string used to separate values.  By default, this is any
        whitespace.
    converters : dict, optional
        A dictionary mapping column number to a function that will convert
        that column to a float.  E.g., if column 0 is a date string:
        ``converters = {0: datestr2num}``.  Converters can also be used to
        provide a default value for missing data (but see also `genfromtxt`):
        ``converters = {3: lambda s: float(s.strip() or 0)}``.  Default: None.
    skiprows : int, optional
        Skip the first `skiprows` lines; default: 0.
    usecols : sequence, optional
        Which columns to read, with 0 being the first.  For example,
        ``usecols = (1,4,5)`` will extract the 2nd, 5th and 6th columns.
        The default, None, results in all columns being read.
    unpack : bool, optional
        If True, the returned array is transposed, so that arguments may be
        unpacked using ``x, y, z = loadtxt(...)``.  When used with a structured
        data-type, arrays are returned for each field.  Default is False.
    ndmin : int, optional
        The returned array will have at least `ndmin` dimensions.
        Otherwise mono-dimensional axes will be squeezed.
        Legal values: 0 (default), 1 or 2.
        .. versionadded:: 1.6.0
    eoh : str, optional
        The string used to detect the end of header.
    Returns
    -------
    out : ndarray
        Data read from the text file.
    header : 
        The list of lines commented out
    See Also
    --------
    load, fromstring, fromregex
    genfromtxt : Load data with missing values handled as specified.
    scipy.io.loadmat : reads MATLAB data files
    Notes
    -----
    This function aims to be a fast reader for simply formatted files.  The
    `genfromtxt` function provides more sophisticated handling of, e.g.,
    lines with missing values.
    .. versionadded:: 1.10.0
    The strings produced by the Python float.hex method can be used as
    input for floats.
    Examples
    --------
    >>> from io import StringIO   # StringIO behaves like a file object
    >>> c = StringIO("0 1\\n2 3")
    >>> np.loadtxt(c)
    array([[ 0.,  1.],
           [ 2.,  3.]])
    >>> d = StringIO("M 21 72\\nF 35 58")
    >>> np.loadtxt(d, dtype={'names': ('gender', 'age', 'weight'),
    ...                      'formats': ('S1', 'i4', 'f4')})
    array([('M', 21, 72.0), ('F', 35, 58.0)],
          dtype=[('gender', '|S1'), ('age', '<i4'), ('weight', '<f4')])
    >>> c = StringIO("1,0,2\\n3,0,4")
    >>> x, y = np.loadtxt(c, delimiter=',', usecols=(0, 2), unpack=True)
    >>> x
    array([ 1.,  3.])
    >>> y
    array([ 2.,  4.])
    """
        
    def split_comment(line, regex_comments):
        """Chop off comments and strip.
        """
        buf = regex_comments.split(line, maxsplit=1)[0]
        buf = buf.strip('\r\n')
        if buf:
            return buf, ''
        else:
            line = regex_comments.split(line, maxsplit=1)[1]
            line = line.strip('\r\n')
            return None, line.lstrip()
    
    fown = False
    if isinstance(fname, str) :
        try :
            fd = open(fname, 'r')        
        except TypeError:
            raise ValueError('fname must be a filename')
        fown = True
    else :
        fd = fname
        
    offset = 0
    for i in range(skiprows):
        dummy = fd.readline()
        offset = offset + len(dummy)
        
    header = []

    if comments is not None:
        if isinstance(comments, (str, bytes)):
            _comments = [comments]
        else:
            _comments = [comment for comment in comments]

        # Compile regex for comments beforehand
        _comments = (re.escape(comment) for comment in _comments)
        regex_comments = re.compile('|'.join(_comments))

        first_vals = None
        try:
            while not first_vals:
                first_line = fd.readline()
                read_byte =  len(first_line)
                offset = offset + read_byte
                first_vals, commentout = split_comment(first_line, regex_comments)
                if commentout : header.append(commentout)
                if eoh :
                    if commentout.find(eoh) >= 0: break
            offset = read_byte - read_byte
        except StopIteration:
            # End of lines reached
            warnings.warn('readtxt: Empty input file: "%s"' % fname)
        if first_vals :
            try:
                fd.seek(offset)
            except TypeError:
                raise ValueError('sys.stdin without end_of_header not allowed')
    X = np.loadtxt(fd, dtype, comments, delimiter, converters, 0, usecols, unpack, ndmin)
    
    if fown : fd.close()

    return X, header
       
    
def savetxt(X, fname=None, fmt='%.18e', delimiter=' ', newline='\n', headers=None,
             footer='', comments='# ', append=False):
    """
    Wrapper function of numpy.savetxt

    Save an array to a text file.
    Parameters
    ----------
    X : array_like
        Data to be saved to a text file.
    fname : filename or file handle
        If the filename ends in ``.gz``, the file is automatically saved in
        compressed gzip format.  `loadtxt` understands gzipped files
        transparently.
    fmt : str or sequence of strs, optional
        A single format (%10.5f), a sequence of formats, or a
        multi-format string, e.g. 'Iteration %d -- %10.5f', in which
        case `delimiter` is ignored. For complex `X`, the legal options
        for `fmt` are:
            a) a single specifier, `fmt='%.4e'`, resulting in numbers formatted
                like `' (%s+%sj)' % (fmt, fmt)`
            b) a full string specifying every real and imaginary part, e.g.
                `' %.4e %+.4j %.4e %+.4j %.4e %+.4j'` for 3 columns
            c) a list of specifiers, one per column - in this case, the real
                and imaginary part must have separate specifiers,
                e.g. `['%.3e + %.3ej', '(%.15e%+.15ej)']` for 2 columns
    delimiter : str, optional
        String or character separating columns.
    newline : str, optional
        String or character separating lines.
        .. versionadded:: 1.5.0
    headers : str or sequence, optional
        String that will be written at the beginning of the file.
        .. versionadded:: 1.7.0
    footer : str, optional
        String that will be written at the end of the file.
        .. versionadded:: 1.7.0
    comments : str, optional
        String that will be prepended to the ``header`` and ``footer`` strings,
        to mark them as comments. Default: '# ',  as expected by e.g.
        ``numpy.loadtxt``.
        .. versionadded:: 1.7.0
    append : bool, optional
        If True, the array is appended to the file.
    See Also
    --------
    save : Save an array to a binary file in NumPy ``.npy`` format
    savez : Save several arrays into an uncompressed ``.npz`` archive
    savez_compressed : Save several arrays into a compressed ``.npz`` archive
    Notes
    -----
    Further explanation of the `fmt` parameter
    (``%[flag]width[.precision]specifier``):
    flags:
        ``-`` : left justify
        ``+`` : Forces to precede result with + or -.
        ``0`` : Left pad the number with zeros instead of space (see width).
    width:
        Minimum number of characters to be printed. The value is not truncated
        if it has more characters.
    precision:
        - For integer specifiers (eg. ``d,i,o,x``), the minimum number of
          digits.
        - For ``e, E`` and ``f`` specifiers, the number of digits to print
          after the decimal point.
        - For ``g`` and ``G``, the maximum number of significant digits.
        - For ``s``, the maximum number of characters.
    specifiers:
        ``c`` : character
        ``d`` or ``i`` : signed decimal integer
        ``e`` or ``E`` : scientific notation with ``e`` or ``E``.
        ``f`` : decimal floating point
        ``g,G`` : use the shorter of ``e,E`` or ``f``
        ``o`` : signed octal
        ``s`` : string of characters
        ``u`` : unsigned decimal integer
        ``x,X`` : unsigned hexadecimal integer
    This explanation of ``fmt`` is not complete, for an exhaustive
    specification see [1]_.
    References
    ----------
    .. [1] `Format Specification Mini-Language
           <http://docs.python.org/library/string.html#
           format-specification-mini-language>`_, Python Documentation.
    Examples
    --------
    >>> x = y = z = np.arange(0.0,5.0,1.0)
    >>> np.savetxt('test.out', x, delimiter=',')   # X is an array
    >>> np.savetxt('test.out', (x,y,z))   # x,y,z equal sized 1D arrays
    >>> np.savetxt('test.out', x, fmt='%1.4e')   # use exponential notation
    """
    def setHeaders(headers):
        _header = ""
        for line in headers:
            _header = _header + line + '\n'
        _header = _header[:-1]
        return _header

    try:
        if headers is not None:
            headers = list(headers)
            header = setHeaders(headers) 
        else:
            header = ''

        #print(header)
        if fname is None:
           if sys.version_info[0] >= 3:
               np.savetxt(sys.stdout.buffer, X, fmt, delimiter, newline, header, footer, comments)
           else:
               np.savetxt(sys.stdout, X, fmt, delimiter, newline, header, footer, comments)
        else:
           if append:
              fout = open(fname,"a")
              np.savetxt(fout, X, fmt, delimiter, newline, header, footer, comments)
              fout.close()
           else:
              np.savetxt(fname, X, fmt, delimiter, newline, header, footer, comments)
    except TypeError:
        raise ValueError('fname must be a string, file handle, or generator')              

class egio():
    """
    egio() is pure python module for parsing eg data-format file.
 
    ex)
       eg = tools.egio()

    """
    def __init__(self):
        self.Name     = ''
        self.ShotNo   = 0
        self.SubNo    = 0
        self.Date     = ''
        self.DimNo    = 0
        self.DimSize  = []
        self.DimName  = []
        self.DimUnit  = []
        self.ValNo    = 0
        self.ValName  = []
        self.ValUnit  = []
        self.comments = []

    def clear(self):
        self.Name     = ''
        self.ShotNo   = 0
        self.SubNo    = 0
        self.Date     = ''
        self.DimNo    = 0
        self.DimSize  = []
        self.DimName  = []
        self.DimUnit  = []
        self.ValNo    = 0
        self.ValName  = []
        self.ValUnit  = []
        self.comments = []

    def new(self, headers):
        """
        parsing a line of header.
        """

        reobjItem  = re.compile(r'(.+)\s*=\s*(.+)')
        stat = False
        self.comments = []
        for line in headers:
            matchitem = reobjItem.match(line)
            if matchitem:
                key = matchitem.groups()[0].upper()
                key = key.strip()
                val = matchitem.groups()[1]
                if 'NAME' == key:
                    clm = val.strip()
                    clm = val.strip('\'')
                    self.Name = clm
                if 'SHOTNO' == key:
                    self.ShotNo = int(val)
                if 'SUBNO' == key:
                    self.SubNo = int(val)
                if 'DATE' == key:
                    clm = val.strip()
                    clm = val.strip('\'')
                    self.Date = clm
                if 'DIMNO' == key:
                    self.DimNo = int(val)
                if 'DIMSIZE' == key:
                    clm = val.split(',')
                    for i in range(self.DimNo):
                        self.DimSize.append(int(clm[i]))
                if 'DIMNAME' == key:
                    clm = val.split(',')
                    for i in range(self.DimNo):
                        clmd = clm[i].strip()
                        clmd = clmd.strip('\'')
                        self.DimName.append(clmd)
                if 'DIMUNIT' == key:
                    clm = val.split(',')
                    for i in range(self.DimNo):
                        clmd = clm[i].strip()
                        clmd = clmd.strip('\'')
                        self.DimUnit.append(clmd)
                if 'VALNO' == key:
                    self.ValNo = int(val)
                if 'VALNAME' == key:
                    clm = val.split(',')
                    for i in range(self.ValNo):
                        clmd = clm[i].strip()
                        clmd = clmd.strip('\'')
                        self.ValName.append(clmd)
                if 'VALUNIT' == key:
                    clm = val.split(',')
                    for i in range(self.ValNo):
                        clmd = clm[i].strip()
                        clmd = clmd.strip('\'')
                        self.ValUnit.append(clmd)
            else:
                if line.upper().find("[DATA]") >= 0:
                    break
                if line.upper().find("[COMMENTS]") >= 0:
                    stat = True
                    continue
                if stat :
                    self.comments.append(line)      

                   
    def load(self, fname = None, usecols=None):
        if fname is not None :
            X, headers = loadtxt(fname, delimiter=',', usecols=usecols)
        else :             
            X, headers = loadtxt(sys.stdin, delimiter=',', usecols=usecols, eoh="[Data]")
        self.new(headers)
        if fname is not None:
            line = "read from '{0}'".format(fname)
            self.comments.append(line)
        return X
   

    def save(self, X, fname=None, fmt='%.18e'):
        if fname is not None:
            line = "write to '{0}'".format(fname)
            self.comments.append(line)
        self.comments.append(getLog())
        self.Date = strftime("%m/%d/%Y %H:%M", gmtime())
        for i in range(self.DimNo):
             if i == 0:
                 dimname = "'{0}'".format(self.DimName[i])
                 dimsize = "{0:d}".format(self.DimSize[i])
                 dimunit = "'{0}'".format(self.DimUnit[i])
             else:
                 dimname = dimname + ", '{0}'".format(self.DimName[i])
                 dimsize = dimsize + ", {0:d}".format(self.DimSize[i])
                 dimunit = dimunit + ", '{0}'".format(self.DimUnit[i])

        for i in range(self.ValNo):
            if i == 0:
                valname = "'{0}'".format(self.ValName[i])
                valunit = "'{0}'".format(self.ValUnit[i])
            else:
                valname = valname + ", '{0}'".format(self.ValName[i])
                valunit = valunit + ", '{0}'".format(self.ValUnit[i])         

        _headers = []
        _headers.append("[Parameters]")
        _headers.append("Name = '{0}'".format(self.Name))
        _headers.append("ShotNo = {0:d}".format(self.ShotNo))
        _headers.append("SubNo = {0:d}".format(self.SubNo))
        _headers.append("Date = '{0}'".format(self.Date))
        _headers.append(" ")
        _headers.append("DimNo = {0:d}".format(self.DimNo))
        _headers.append("DimName = {0}".format(dimname))
        _headers.append("DimSize = {0}".format(dimsize))
        _headers.append("DimUnit = {0}".format(dimunit)) 
        _headers.append(" ")
        _headers.append("ValNo = {0:d}".format(self.ValNo))
        _headers.append("ValName = {0}".format(valname))
        _headers.append("ValUnit = {0}".format(valunit)) 
        _headers.append(" ")  
        _headers.append("[Comments]")
        for line in self.comments :
            _headers.append(line)
        _headers.append(" ")
        _headers.append("[Data]")
        if fname is not None:
            savetxt(X, fname=fname, fmt=fmt, delimiter=', ', headers=_headers, comments='# ')
        else :
            savetxt(X, fmt=fmt, delimiter=', ', headers=_headers, comments='# ')
        
    def setValNameFrom(self, source, unit = None):
        self.ValName = []
        self.ValUnit = []
        if unit is not None:
            unit = asbytes(unit)
        else:
            unit = ' '
        for val in source :
            self.ValName.append("{0.6E}".format(val))
            self.ValUnit.append(unit)

def setDefaultArguments(self, version, timestamp):
    self.add_argument(
        '--version', 
        action='version', 
        version='Ver:{0} ({1})'.format(version, timestamp))

def setFileArguments(self, default_wfmt='%18.e'):
    self.add_argument(
        '--ownformat', 
        action='store_true',
        default = False,
        help='If True, own format is used [ False ]')

    self.add_argument(
        '--usecols',
        action='store',
        nargs='+',
        type=int,
        default = None,
        metavar = 'int',
        help='Set columns to read, with 0 being the first [ All ]')
    
    self.add_argument(
        '--comment', 
        action='store',
        type=str,
        default = '#',
        metavar = 'str',
        help='A character used to indicate the start of a comment [ # ]')

    self.add_argument(
        '--delimiter', 
        action='store',
        type=str,
        default = ' ',
        metavar = 'str',
        help='Set delimiter used to separate values [ , ]')

    self.add_argument(
        '--skiprows', 
        action='store',
        type=int,
        default = 0,
        metavar = 'int',
        help='Skip the first "skiprows" lines [ 0 ]')
    
    self.add_argument(
        '--keepskipped', 
        action='store_true',
        default = False,
        help='If True, skipped lines are saved in headers [ False ]')    

    self.add_argument(
        '--wfmt', 
        action='store',
        type=str,
        default = default_wfmt,
        metavar = 'str',
        help='A single format, a sequence of formats, or a multi-format string [ %%.18E ]')   
