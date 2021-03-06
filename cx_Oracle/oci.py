try:
    from oci_generated_12 import *
except ImportError:
    try:
        from oci_generated_11 import *
    except ImportError:
        try:
            from oci_generated_10 import *
        except ImportError:
            raise Exception("Could not import oracle libraries version 12, 11 or 10. Giving up. Don't forget to set your ORACLE_HOME and LD_LIBRARY_PATH.")

ORACLE_10G = hasattr(locals(), 'OCI_ATTR_MODULE')
ORACLE_10GR2 = hasattr(locals(), 'OCI_MAJOR_VERSION')
ORACLE_11 = hasattr(locals(), 'OCI_ATTR_CONNECTION_CLASS')
ORACLE_12 = hasattr(locals(), 'OCI_ATTR_DML_ROW_COUNT_ARRAY')


# defines stuff that could not be generated by ctypesgen, or that were incorrectly generated

# broken because lhs is #defined first.
# /home/lameiro/projects/cx_oracle_on_ctypes/instantclient_11_2/sdk/include/oci.h: 1408
try:
    OCI_ATTR_ENV_NCHARSET_ID = OCI_ATTR_NCHARSET_ID
except:
    pass

# ctypesgen wrongly generated sb1 as char

sb1 = ctypes.c_byte

# ctypesgen did not include the OCITime in OCIDate (10, 11), and for 12, it generates wrong OCIDateTime field
# TODO: does this actually work? oci_generated have references to the old one? check the date type tests.
class OCIDate(Structure):
    _fields_ = [
        ('OCIDateYYYY', sb2),
        ('OCIDateMM', ub1),
        ('OCIDateDD', ub1),
        ('OCIDateTime', OCITime),
    ]
    
# ctypesgen could not generate these macros. how comes? it is probably not using gcc the way it should

def OCIDateGetDate(date):
    return date.OCIDateYYYY, date.OCIDateMM, date.OCIDateDD

def OCIDateSetDate(date, year, month, day):
    date.OCIDateYYYY, date.OCIDateMM, date.OCIDateDD = year, month, day

def OCIDateGetTime(date):
    time = date.OCIDateTime
    return time.OCITimeHH, time.OCITimeMI, time.OCITimeSS

def OCIDateSetTime(date, hour, minute, second):
    time = date.OCIDateTime
    time.OCITimeHH, time.OCITimeMI, time.OCITimeSS = hour, minute, second
