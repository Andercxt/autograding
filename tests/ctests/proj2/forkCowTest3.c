#include "types.h"
#include "stat.h"
#include "user.h"

int
main(int argc, char *argv[])
{
  int dummy = 1;
  printf(1, "fork_cow_test\n");

  char * dummy_mem = (char *) malloc(sizeof(char) * 200 * 1024 * 1024);

  int pid = fork();
  if(pid < 0) {
    printf(1, "TEST FAILED\n");
    exit();
  }

  if(pid > 0) {
    int pid2 = fork();
    if(pid2 < 0) {
      printf(1, "TEST FAILED\n");
      exit();
    }

    if(pid2 == 0) {
      if (dummy != 1) {
        printf(1, "TEST FAILED\n");
        exit();
      }

      dummy = 3;
      if (dummy != 3) {
        printf(1, "TEST FAILED\n");
        exit();
      }
//    assert(dummy == 5);
      printf(1, "I'm child process, dummy = %d\n", dummy);
      sleep(2);
      exit();
    }
  }

  if(pid == 0) {
    if (dummy != 1) {
      printf(1, "TEST FAILED\n");
      exit();
    }

    dummy = 5;
    if (dummy != 5) {
      printf(1, "TEST FAILED\n");
      exit();
    }
//    assert(dummy == 5);
    printf(1, "I'm child process, dummy = %d\n", dummy);
    sleep(2);
    exit();
  }
  // parent
  if (dummy != 1) {
    printf(1, "TEST FAILED\n");
    exit();
  }
 // assert(dummy == 1);
  printf(1, "I'm parent process, dummy = %d\n", dummy);
  wait();
  if (dummy != 1) {
    printf(1, "TEST FAILED\n");
    exit();
  }
 // assert(dummy == 1);
  printf(1, "I'm parent process, dummy = %d\n", dummy);

  free(dummy_mem);

  printf(1, "TEST PASSED\n");
  exit();
}
