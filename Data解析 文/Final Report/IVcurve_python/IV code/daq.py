#!/usr/bin/env python
# Data解析 文\Final Report\IVcurve_python\IV code\daq.py
"""
    Read PANTA binary file into numpy.darray.

    class:
       pantaADC

    Status
    ------
    Version 1.0

    Authour
    -------
    Shigeru Inagaki                                       
    Research Institute for Applied Mechanics 
    inagaki@riam.kyushu-u.ac.jp  
    
    Revision History
    ----------------
    [09-June-2017] Creation

    Copyright
    ---------
    2017 Shigeru Inagaki (inagaki@riam.kyushu-u.ac.jp)
    Released under the MIT, BSD, and GPL Licenses.

"""
import numpy as np
import sys
import os
      
class pantaADC():
   def __init__(self):
      self.shot = 0
      self.subshot = 0
      self.tower = 0
      self.station = 0
      self.ch = 0
      self.basename =''
      self.formatversion = ''
      self.model = ''
      self.endian = ''
      self.dataformat = ''       
      self.groupnumber = 0
      self.tracetotalnumber = 0
      self.dataoffset = 0
      self.tracenumber = 0
      self.blocknumber = 0
      self.tracename = ''
      self.blocksize = 0
      self.vresolution = 0.0    
      self.voffset = 0.0
      self.vdatatype = ''
      self.vunit = ''
      self.vplusoverdata = 0
      self.vminusoverdata = 0   
      self.villegaldata = ''
      self.vmaxdata = 0.0
      self.vmindata = 0.0
      self.hresolution = 0.0
      self.hoffset = 0.0
      self.hunit = ''
      self.date = ''
      self.time = ''
      self.swap_endian = False


   def readHdr(self, hdrfile):
      try:
         fid = open(hdrfile, 'r')
         for line in fid:
            if line.find('/') >= 0 :
               continue
            if line.find('$') >= 0 :
               continue
            if len(line.strip()) == 0 :
               continue
            [key, val] = line.split(' ',1)
            key = key.strip()
            val = val.strip()
            if len(val) == 0 :
               continue
            if key == "FormatVersion":
               self.formatversion = val
               continue
            if key == "Model":
               self.model = val
               continue
            if key == "Endian":
               self.endian = val.lower()
               if self.endian == "ltl" : 
                  endian = "little"
               else :
                  endian = "big"
               if endian != sys.byteorder :
                  self.swap_endian = True
               else:
                  self.swap_endian = False                 
               continue
            if key == "DataFormat":
               self.dataformat = val
               continue
            if key == "GroupNumber":
               self.groupnumber = int(val)
               continue
            if key == "TraceTotalNumber":
               self.tracetotalnumber = int(val)
               continue
            if key == "DataOffset":
               self.dataoffset = int(val)
               continue
            if key == "TraceNumber":
               self.tracenumber = int(val)
               continue
            if key == "BlockNumber":
               self.blocknumber = int(val)
               continue
            if key == "TraceName":
               self.tracename = val
               continue      
            if key == "BlockSize":
               self.blocksize = int(val)
               continue
            if key == "VResolution":
               self.vresolution = float(val)
               continue
            if key == "VOffset":
               self.voffset = float(val)
               continue
            if key == "VDataType":
               self.vdatatype = val
               continue
            if key == "VUnit":
               self.vunit = val
               continue
            if key == "VPlusOverData":
               self.vplusoverdata = int(val)
               continue
            if key == "VMinusOverData":
               self.vminusoverdata = int(val)
               continue
            if key == "VIllegalData":
               self.villegaldata = val
               continue
            if key == "VMaxData":
               self.vmaxdata = float(val)
               continue
            if key == "VMinData":
               self.vmindata = float(val)
               continue
            if key == "HResolution":
               self.hresolution = float(val)
               continue
            if key == "HOffset":
               self.hoffset = float(val)
               continue
            if key == "HUnit":
               self.hunit = val
               continue
            if key == "Date":
               self.date = val
               continue
            if key == "Time":
               self.time = val
               continue
         fid.close()
      except Exception as ex:
         print("Error at readHdr")
         print(ex.message)
         sys.exit(-1)          



   def readDat(self, binfile, start=0, end=None, samplingtime=False):
      import tools as tl
      try:
         if end is None :
            end = self.blocksize - 1 
         else :
            if end > self.blocksize - 1 :
               raise ValueError       
         nread = end - start + 1
         raw = tl.readbin(binfile, nread, start)
         dat = np.zeros(nread, dtype=np.float64)
         if self.swap_endian:
            dat = self.vresolution*raw.byteswap() + self.voffset
         else :
            dat = self.vresolution*raw + self.voffset
         del raw
         if samplingtime :
            sampling_time = self.hresolution
            delay_time = self.hoffset*sampling_time
            t = sampling_time*(np.arange(start, end+1, dtype=np.float64) + 1.0) + delay_time
            return dat, t
         else :
            return dat
      except ValueError:
         print( "requested data size too large")
         sys.exit(-1) 

   def read(self, shot=None, subshot=None, tower=None, station=None, ch=None, dir=None, basename=None, gzipped=False,
            start=0, end=None, samplingtime=False):
      if basename is None :
         self.shot = shot
         self.subshot = subshot
         self.tower = tower
         self.station = station
         self.ch = ch
         self.basename = "{0}_{1}{2}{3}_{4}_{5}".format(shot, subshot, os.sep, tower, station, ch)
      else :
         self.basename = basename

      hdrfile = self.basename + ".hdr"
      if gzipped :
         binfile = self.basename + ".dat.gz"
      else :
         # binfile = self.basename + ".dat"     #old system
          binfile = self.basename + ".wvf"      #new system
      if dir is not None:
         if os.path.isdir(dir):
            path = os.path.normpath(dir)
         else:
            print("{0} is not found.".format(dir))
            sys.exit(-1)
         hdrfile = path + os.sep + hdrfile
         binfile = path + os.sep + binfile
         
      self.readHdr(hdrfile)
      return self.readDat(binfile, start, end, samplingtime)
