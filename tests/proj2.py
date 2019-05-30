import toolspath
from testing import Xv6Build, Xv6Test

# Part 1
class deref_null(Xv6Test):
  name = "deref_null"
  description = "Part 1: Fork to create a child process and have the child attempt to dereference NULL pointer.  " + \
                 "Child process should be killed."
  tester = "ctests/proj2/" + name + ".c"
  make_qemu_args = "CPUS=1"
  point_value = 15
  timeout = 10

class deref_0x1000(Xv6Test):
  name = "deref_0x1000"
  description = "Part 1: Fork to create a child process and have the child attempt to dereference address 0x1000.  " + \
                 "Child process should survive and exit normally."
  tester = "ctests/proj2/" + name + ".c"
  make_qemu_args = "CPUS=1"
  point_value = 10
  timeout = 10

class alloc_155_pages(Xv6Test):
  name = "alloc_155_pages"
  description = "Part 1: Attempt to allocate up to the top of userspace (below shared memory)."
  tester = "ctests/proj2/" + name + ".c"
  make_qemu_args = "CPUS=1"
  point_value = 10
  timeout = 15

class whenTryingToAllocateAboveUsertop_sbrkShouldFail(Xv6Test):
  name = "whenTryingToAllocateAboveUsertop_sbrkShouldFail"
  description = "Part 1: Attempt to allocate up to the top of userspace (below shared memory).  " + \
                "Then try to allocate 6 more pages, which would blow through USERTOP.  sbrk should return -1."
  tester = "ctests/proj2/" + name + ".c"
  make_qemu_args = "CPUS=1"
  point_value = 2
  timeout = 10

class whenTryingToReallocateAPageNearUsertop_sbrkShouldSucceed(Xv6Test):
  name = "whenTryingToReallocateAPageNearUsertop_sbrkShouldSucceed"
  description = "Part 1: Attempt to allocate up to the top of userspace (below shared memory).  " + \
                "Then deallocate one page and reallocate one page.  Make sure both calls to sbrk succeed."
  tester = "ctests/proj2/" + name + ".c"
  make_qemu_args = "CPUS=1"
  point_value = 3
  timeout = 10

#Part 2
class forkLargeMemTest(Xv6Test):
  name = "forkLargeMemTest"
  description = "Part 2: Test the stability when forking a large bunch of memory."
  tester = "ctests/proj2/" + name + ".c"
  make_qemu_args = "CPUS=1"
  point_value = 15
  timeout = 10

class forkCowTest(Xv6Test):
  name = "forkCowTest"
  description = "Part 2: Test cpy-on-write folk."
  tester = "ctests/proj2/" + name + ".c"
  make_qemu_args = "CPUS=1"
  point_value = 10
  timeout = 10

class forkCowTest2(Xv6Test):
  name = "forkCowTest2"
  description = "Part 2: Test cpy-on-write folk: fork the parent 30 times."
  tester = "ctests/proj2/" + name + ".c"
  make_qemu_args = "CPUS=1"
  point_value = 10
  timeout = 60

class forkCowTest3(Xv6Test):
  name = "forkCowTest3"
  description = "Part 2: Test cpy-on-write folk: fork two children, make changes in both children. " + \
                "Test whether the memory content changed."
  tester = "ctests/proj2/" + name + ".c"
  make_qemu_args = "CPUS=1"
  point_value = 10
  timeout = 10


import toolspath
from testing.runtests import main
main(Xv6Build, [deref_null, deref_0x1000, alloc_155_pages, whenTryingToAllocateAboveUsertop_sbrkShouldFail,
               whenTryingToReallocateAPageNearUsertop_sbrkShouldSucceed,
               forkLargeMemTest, forkCowTest, forkCowTest2, forkCowTest3])
#main(Xv6Build, [shmem_access_communication])
