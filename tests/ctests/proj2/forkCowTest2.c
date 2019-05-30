#include "types.h"
#include "stat.h"
#include "user.h"

#define N 30

void
forktest(void)
{
  int n, pid;

  printf(1, "fork test\n");
  char * dummy_mem = (char *) malloc(sizeof(char) * 100 * 1024 * 1024);

  for(n=0; n<N; n++){
    pid = fork();
    if(pid < 0)
      break;
    if(pid == 0)
      exit();
  }

  printf(1, "Hello, World\n");

  if(n != N){
    printf(1, "fork claimed to work N times!\n", N);
    printf(1, "TEST FAILED\n");
    exit();
  }

  for(; n > 0; n--){
    if(wait() < 0){
      printf(1, "wait stopped early\n");
      printf(1, "TEST FAILED\n");
      exit();
    }
  }

  if(wait() != -1){
    printf(1, "wait got too many\n");
    printf(1, "TEST FAILED\n");
    exit();
  }
  free(dummy_mem);
  printf(1, "TEST PASSED\n");
}

int
main(int argc, char *argv[])
{
  forktest();
  exit();
}
