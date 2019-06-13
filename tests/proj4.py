# TODO need to modify autograder to allow 2 test programs so that we can shutdown the OS, then
#      restart it and see that tags have persisted.  Unfortunately, swapping out the tester file
#      causes the filesystem to be rebuilt, which causes tags to be lost.

'''
* The tagFile syscall must use the exact function signature that we have provided above:         NA
* The tagFile syscall must tag the file specified by the file descriptor with the key-value 
  pair that is passed in:                                                                        tagFile, tagFile2, tagFile3, tagFile4
* If the file already has a tag with the specified key, then the specified value will 
  overwrite the stored value.  In other words, if a file is tagged with "language": "English", 
  you should be able to use tagFile to change the tag to "language": "Java".                     tagFile5
* The tagFile syscall must validate the arguments passed in and return -1 as necessary 
  to indicate an error.  Some cases to consider:
  - The file descriptor must be opened in write mode in order to tag a file successfully.        tag-bad-fd
  - The key must be at least 2 bytes (including the null termination byte) and at most 10 
    bytes (including the null termination byte).                                                 tag-File-bad-key
  - You can restrict the disk space allotted to tags to 512 bytes per file.  In other words, 
    you can require that all tag information for a given file must fit within a single 512-byte 
    disk block.  If there isn't sufficient tag space for tagFile to complete, you can simply 
    return -1.                                                                                   tag-bad-val

* The removeFileTag syscall must use the exact function signature that we have provided 
  above.                                                                                          NA
* The removeFileTag syscall must remove the specified tag from the specified file.                removeFileTag
* The syscall should return -1 to indicate an error.  Here are some cases to consider:
  - If the tag specified by key cannot be found or is invalid, return -1.                         remove-bad-key
  - If the file descriptor is not open and writable, return -1.                                   remove-bad-fd
* The syscall should return 1 to indicate success.                                                NA

* The getFileTag syscall must use the exact function signature that we have provided above.       NA
* The syscall should return the length of the value part of the specified tag.  This 
  returned length should NOT include any null-terminating byte.  In fact, since the length 
  of the value is being passed around, you do not need to use a null-terminating byte at all.  
  If you do choose to use one, it should not be counted in the returned length.                   tagFile thru tagFile5
* The value of the specified tag should be written to buffer.                                     tagFile thru tagFile5
* If the length of the value is longer than length, the syscall should return the actual 
  length of the value.  This allows the user to decide whether to allocate a larger buffer 
  and try again.                                                                                  getTag-long-value
* The syscall should return -1 to indicate failure.  Here are some cases to consider:
  - If the key cannot be found or is invalid, return -1.                                          getTag-bad-key
  - If the file descriptor is not open and readable, return -1.                                   getTag-bad-fd

'''

import sys, os, inspect

import toolspath
from testing import Xv6Test, Xv6Build

ctestsDir = os.path.basename(__file__)[:-3]

curdir = os.path.realpath(os.path.dirname(inspect.getfile(inspect.currentframe())))
def get_description(name):
  cfile = os.path.join(curdir, 'ctests', ctestsDir, name + '.c')
  with open(cfile, 'r') as f:
    desc = f.readline()
    desc = desc.strip()

    if desc[:2] == "/*":
      desc = desc[2:]
    else:
      return "Description: None"

    desc = "Description:" + desc

    while not desc.endswith("*/"):
      this_line = f.readline()
      desc += " " + this_line.strip()

      if this_line == "":
        return desc.strip()

  desc = desc[:-2]
  return desc.strip()

test_values = [
  {'name': 'tagFile', 'point_value': 5, 'timeout': 120},
  {'name': 'tagFile2', 'point_value': 5, 'timeout': 120},
  {'name': 'tagFile3', 'point_value': 5, 'timeout': 120},
  {'name': 'tagFile4', 'point_value': 5, 'timeout': 120},
  {'name': 'tagFile5', 'point_value': 5, 'timeout': 120},
  {'name': 'tagFile6', 'point_value': 6, 'timeout': 120},
  {'name': 'tagFile-bad-fd', 'point_value': 6, 'timeout': 120},
  {'name': 'tagFile-bad-key', 'point_value': 6, 'timeout': 120},
  {'name': 'tagFile-bad-val', 'point_value': 6, 'timeout': 120},
  {'name': 'removeFileTag', 'point_value': 6, 'timeout': 120},
  {'name': 'remove-bad-key', 'point_value': 6, 'timeout': 120},
  {'name': 'remove-bad-fd', 'point_value': 6, 'timeout': 120},
  {'name': 'getTag-long-value', 'point_value': 6, 'timeout': 120},
  {'name': 'getTag-bad-fd', 'point_value': 6, 'timeout': 120},
  {'name': 'getTag-bad-key', 'point_value': 6, 'timeout': 120},
  {'name': 'ec-tagFile7', 'point_value': 2, 'timeout': 120},
  {'name': 'ec-getAllTags', 'point_value': 2, 'timeout': 120},
  {'name': 'ec-getAllTags2', 'point_value': 2, 'timeout': 120},
  {'name': 'ec-getFilesByTag', 'point_value': 2, 'timeout': 120},
  {'name': 'ec-getFilesByTag2', 'point_value': 2, 'timeout': 120},
  {'name': 'ec-arbitraryLength', 'point_value': 2, 'timeout': 120},
  {'name': 'ec-arbitraryLength2', 'point_value': 2, 'timeout': 120},
  {'name': 'ec-manyBlocks', 'point_value': 2, 'timeout': 120},
  {'name': 'ec-manyBlocks2', 'point_value': 2, 'timeout': 255},
  {'name': 'ec-manyBlocks3', 'point_value': 2, 'timeout': 120},
  # #{'name': 'tagPersistence-part1', 'point_value': 0, 'timeout': 10},
  # #{'name': 'tagPersistence-part2', 'point_value': 3, 'timeout': 10},
]

all_tests = []
build_test = Xv6Build
for test in test_values:
  testname = test['name']

  if 'point_value' in test.keys():
    point_value = test['point_value']
  else:
    point_value = 0

  if 'timeout' in test.keys():
    timeout = test['timeout']
  else:
    timeout = 10

  members = {
      'name': testname,
      'tester': 'ctests/' + ctestsDir + '/' + testname + '.c',
      'description': get_description(testname),
      'timeout': timeout,
      'point_value': point_value
      }
  newclass = type(testname, (Xv6Test,), members)
  all_tests.append(newclass)
  setattr(sys.modules[__name__], testname, newclass)

class usertests(Xv6Test):
  name = 'usertests'
  tester = 'ctests/' + ctestsDir + '/usertests.c'
  description = get_description('usertests')
  timeout = 240

# To include full regression test by running usertests, uncomment the line below.
#all_tests.append(usertests)

from testing.runtests import main
main(build_test, all_tests)
